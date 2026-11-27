"""Build or verify one academic skill and two reproducible upload archives."""
import argparse
import io
import json
import os
from pathlib import Path
import re
import sys
from tempfile import NamedTemporaryFile
from zipfile import ZIP_STORED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MAIN = SKILLS / "academic-skill"
DIST = ROOT / "dist"
CATALOG = json.loads((ROOT / "tools/catalog.json").read_text(encoding="utf-8"))
LAB_RESOURCES = {
    "academic-pixel-art": ("references/pikselkunst.md", "scripts/pixel_art.py"),
    "academic-drawio": ("assets/kildearbeid.json", "scripts/make_drawio.py"),
    "academic-uml": (
        "assets/innlevering-sekvens.puml",
        "assets/klassediagram.puml",
        "assets/utkast-tilstand.mmd",
        "references/uml-notasjon.md",
        "scripts/render_plantuml.py",
    ),
}


def json_bytes(document):
    return (json.dumps(document, indent=2, ensure_ascii=False) + "\n").encode()


def read_bytes(path):
    data = path.read_bytes()
    if path.suffix in {".md", ".yaml", ".json", ".py", ".mmd", ".puml"}:
        return data.replace(b"\r\n", b"\n")
    return data


def archive(entries):
    output = io.BytesIO()
    with ZipFile(output, "w", compression=ZIP_STORED) as package:
        for name, content in sorted(entries.items()):
            info = ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            package.writestr(info, content, compress_type=ZIP_STORED)
    return output.getvalue()


def generated_files():
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    name = manifest["name"]
    if name != MAIN.name or set(CATALOG) != {name}:
        raise ValueError("The plugin, catalog and skill directory must all identify academic-skill")
    identity = {k: manifest[k] for k in ("name", "version", "description", "author", "homepage", "repository", "keywords")}
    interface = manifest["extensions"]["com.openai"]["interface"]
    yield ROOT / ".codex-plugin/plugin.json", json_bytes(dict(identity, skills="./skills/", interface=interface))
    yield ROOT / ".claude-plugin/plugin.json", json_bytes(identity)
    yield ROOT / ".claude-plugin/marketplace.json", json_bytes({
        "name": "academic-tools", "description": manifest["description"], "owner": {"name": manifest["author"]["name"]},
        "plugins": [{"name": name, "source": "./", "description": manifest["description"]}],
    })
    yield ROOT / ".agents/plugins/marketplace.json", json_bytes({
        "name": "academic-tools", "interface": {"displayName": interface["displayName"]},
        "plugins": [{
            "name": name, "source": {"source": "local", "path": "./"},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": interface["category"],
        }],
    })
    entry = CATALOG[name]
    fields = {key: entry[key] for key in ("display_name", "short_description")}
    fields["default_prompt"] = f"Use ${name}. {entry['prompt_en']}"
    metadata = "interface:\n" + "".join(
        "  " + key + ": " + json.dumps(value, ensure_ascii=False) + "\n" for key, value in fields.items()
    )
    yield MAIN / "agents/openai.yaml", (metadata + "policy:\n  allow_implicit_invocation: true\n").encode()
    # The standalone lab folders are the source for assets used by both installs.
    for lab, resources in LAB_RESOURCES.items():
        for resource in resources:
            yield MAIN / resource, read_bytes(ROOT / "labs" / lab / resource)


def distributions(generated):
    paths = {MAIN / rel for rel in ("SKILL.md", "scripts/sjekk_uttrykk.py", "evals/evals.json")}
    paths.update((MAIN / "references").glob("*.md"))
    paths.update(path for path in generated if path.is_relative_to(MAIN))
    content = {p: generated[p] if p in generated else read_bytes(p) for p in sorted(paths)}
    for document in (p for p in paths if p.suffix == ".md"):
        for link in re.findall(r"\]\(([^ )]+)\)", content[document].decode("utf-8")):
            if link.startswith(("#", "https://", "http://")):
                continue
            linked = (document.parent / link.partition("#")[0]).resolve()
            if linked not in content:
                raise ValueError(f"Missing packaged resource: {document.relative_to(ROOT)} -> {link}")
    standalone = {p.relative_to(SKILLS).as_posix(): data for p, data in content.items()}
    yield DIST / "academic-skill.zip", archive(standalone)
    claude = {"skills/" + name: data for name, data in standalone.items()}
    claude[".claude-plugin/plugin.json"] = generated[ROOT / ".claude-plugin/plugin.json"]
    yield DIST / "academic-skill-claude-plugin.zip", archive(claude)


def write_output(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(dir=path.parent, delete=False) as staged:
        temporary = Path(staged.name)
        try:
            staged.write(data)
        except BaseException:
            staged.close()
            temporary.unlink(missing_ok=True)
            raise
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def build(check=False):
    generated = dict(generated_files())
    expected = {**generated, **dict(distributions(generated))}
    extras = {p for p in SKILLS.iterdir() if p.is_dir() and p != MAIN}
    extras.update(p for p in DIST.glob("*") if p not in expected)
    if extras:
        return ["Unexpected: " + str(p.relative_to(ROOT)) for p in sorted(extras)]
    errors = []
    for path, data in expected.items():
        if path.is_file() and read_bytes(path) == data:
            continue
        if check:
            errors.append("Stale or missing: " + str(path.relative_to(ROOT)))
        else:
            write_output(path, data)
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare generated files and archives without writing")
    try:
        issues = build(parser.parse_args().check)
    except (OSError, ValueError) as exc:
        sys.exit(str(exc))
    if issues:
        sys.exit("\n".join(issues))
    print("Verified academic-skill and both upload archives.")
