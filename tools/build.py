"""Build self-contained skills and reproducible release files using only Python's stdlib."""
import argparse
import io
import json
import re
import sys
from pathlib import Path
from zipfile import ZIP_STORED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MAIN = SKILLS / "academic-skill"
DIST = ROOT / "dist"
CATALOG = json.loads((ROOT / "tools/catalog.json").read_text(encoding="utf-8"))
RESOURCE = re.compile(r"\]\(((?:references|scripts)/[a-z0-9_-]+\.(?:md|py))\)")


def json_bytes(document):
    return (json.dumps(document, indent=2, ensure_ascii=False) + "\n").encode()


def skill_files(directory):
    """Use an allowlist so editor files, caches and personal files never enter a release."""
    paths = [directory / "SKILL.md", directory / "agents/openai.yaml"]
    if directory == MAIN:
        paths.extend(sorted((directory / "references").glob("*.md")))
        paths.extend([directory / "scripts/sjekk_uttrykk.py", directory / "evals/evals.json"])
    else:
        paths.extend(directory / name for name in sorted(resources(directory)))
    return paths


def resources(directory):
    return set(RESOURCE.findall((directory / "SKILL.md").read_text(encoding="utf-8")))


def read_bytes(path):
    data = path.read_bytes()
    if path.suffix in {".md", ".yaml", ".json", ".py"}:
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
    identity = {k: manifest[k] for k in ("name", "version", "description", "author", "homepage", "repository", "keywords")}
    interface = manifest["extensions"]["com.openai"]["interface"]
    yield ROOT / ".codex-plugin/plugin.json", json_bytes(dict(identity, skills="./skills/", interface=interface))
    yield ROOT / ".claude-plugin/plugin.json", json_bytes(identity)
    claude_market = {
        "name": "academic-tools", "description": manifest["description"], "owner": {"name": manifest["author"]["name"]},
        "plugins": [{"name": manifest["name"], "source": "./", "description": manifest["description"]}],
    }
    yield ROOT / ".claude-plugin/marketplace.json", json_bytes(claude_market)
    for name, entry in CATALOG.items():
        base = SKILLS / name
        prompt = "Use $" + name + ". " + entry["prompt_en"]
        fields = {key: entry[key] for key in ("display_name", "short_description")}
        fields["default_prompt"] = prompt
        metadata = "interface:\n" + "".join(
            "  " + key + ": " + json.dumps(value, ensure_ascii=False) + "\n" for key, value in fields.items()
        )
        metadata += "policy:\n  allow_implicit_invocation: true\n"
        yield base / "agents/openai.yaml", metadata.encode()
        if base != MAIN:
            for resource in sorted(resources(base)):
                yield base / resource, read_bytes(MAIN / resource)


def distributions(generated):
    skill_entries = {}
    for name in CATALOG:
        base = SKILLS / name
        entries = {}
        for path in skill_files(base):
            content = generated[path] if path in generated else read_bytes(path)
            key = path.relative_to(SKILLS).as_posix()
            entries[key] = content
            skill_entries["skills/" + key] = content
        target = DIST / ("academic-skill.zip" if base == MAIN else "individual/" + name + ".zip")
        yield target, archive(entries)
    openai_files = {p: read_bytes(ROOT / p) for p in ("plugin.json", "assets/icon.png")}
    yield DIST / "academic-skill-plugin.zip", archive({**openai_files, **skill_entries})
    claude_manifest = ".claude-plugin/plugin.json"
    yield DIST / "academic-skill-claude-plugin.zip", archive({
        claude_manifest: generated[ROOT / claude_manifest],
        **skill_entries,
    })


def build(check=False):
    generated = dict(generated_files())
    expected = {**generated, **dict(distributions(generated))}
    # Unexpected files are reported separately, never removed on the user's behalf.
    actual_zips = set(DIST.rglob("*.zip"))
    extra = actual_zips.difference(expected)
    for base in SKILLS.iterdir():
        if not base.is_dir():
            continue
        if base.name not in CATALOG:
            extra.add(base)
        else:
            for section in ("references", "scripts"):
                for path in (base / section).glob("*"):
                    if path.is_file() and path not in skill_files(base):
                        extra.add(path)
    errors = ["Unexpected: " + str(p.relative_to(ROOT)) for p in sorted(extra)]
    for path, data in expected.items():
        if path.is_file() and read_bytes(path) == data:
            continue
        if check:
            errors.append("Stale or missing: " + str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare all builds without writing")
    issues = build(parser.parse_args().check)
    if issues:
        sys.exit("\n".join(issues))
    print(f"{len(CATALOG)} skills and {len(list(DIST.rglob('*.zip')))} distributions are consistent.")
