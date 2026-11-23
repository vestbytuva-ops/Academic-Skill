"""Check the published format and the installed contents, independently of the builder."""
import json
import re
import struct
import unittest
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

import jsonschema
import yaml

from tools import build, verify_codex

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MAIN = SKILLS / "academic-skill"
NAMES = set("""academic-skill academic-core personal-voice academic-writing humanizer
academic-critic research-integrity learning-coach exam-preparation presentation-engine
office-integration quality-assurance""".split())
LINK = re.compile(r"\[[^\]]*\]\(([^ )]+)\)")


def document(path):
    return json.loads(path.read_text(encoding="utf-8"))


def inventory(base):
    return {p.relative_to(base).as_posix(): p for p in base.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"}


class AcademicPackages(unittest.TestCase):
    def test_exact_registry_and_metadata(self):
        self.assertEqual(set(build.CATALOG), NAMES)
        self.assertEqual({p.parent.name for p in SKILLS.rglob("SKILL.md")}, NAMES)
        descriptions = set()
        labels = set()
        for name in sorted(NAMES):
            with self.subTest(skill=name):
                base = SKILLS / name
                raw = (base / "SKILL.md").read_bytes()
                self.assertTrue(raw.startswith(b"---\n"))
                self.assertNotIn(b"\r", raw)
                _, header, body = raw.decode().split("---\n", 2)
                meta = yaml.safe_load(header)
                self.assertEqual(set(meta), {"name", "description"})
                self.assertEqual(meta["name"], name)
                self.assertTrue(1 <= len(meta["description"]) <= 200)
                self.assertLess(len(body.splitlines()), 300)
                self.assertIn("references/arbeidsgrunnlag.md", body)
                descriptions.add(meta["description"])
                ui = yaml.safe_load((base / "agents/openai.yaml").read_text(encoding="utf-8"))
                self.assertIs(ui["policy"]["allow_implicit_invocation"], True)
                label = ui["interface"]["display_name"]
                self.assertEqual(label, build.CATALOG[name]["display_name"])
                self.assertTrue(label.startswith("Academic "), label)
                labels.add(label)
                self.assertTrue(25 <= len(ui["interface"]["short_description"]) <= 64)
                self.assertIn("$" + name, ui["interface"]["default_prompt"])
        self.assertEqual(len(descriptions), 12)
        self.assertEqual(len(labels), len(NAMES))

    def test_standalone_umbrella_routes_all_specialists_to_their_packaged_guidance(self):
        common = {"references/arbeidsgrunnlag.md", "references/english.md", "references/norsk-skole.md"}
        with ZipFile(ROOT / "dist/academic-skill.zip") as package:
            entry = package.read("academic-skill/SKILL.md").decode()
            routes = re.findall(r"^\| `([a-z-]+)`[^\n]*", entry, re.MULTILINE)
            self.assertCountEqual(routes, NAMES - {MAIN.name})
            for name in routes:
                with self.subTest(skill=name):
                    row = next(line for line in entry.splitlines() if line.startswith(f"| `{name}`"))
                    self.assertIn(build.CATALOG[name]["display_name"], row)
                    specialist = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
                    guidance = {href for href in LINK.findall(specialist) if href.startswith("references/")} - common
                    self.assertTrue(guidance)
                    self.assertEqual(set(LINK.findall(row)), guidance)
                    for href in guidance:
                        self.assertEqual(package.read(f"academic-skill/{href}"), (SKILLS / name / href).read_bytes())

    def test_live_verifier_rejects_old_label_and_wrong_scope(self):
        name = "exam-preparation"
        catalog = {name: build.CATALOG[name]}
        expected = {"name": name, "scope": "user", "enabled": True,
                    "interface": {"displayName": catalog[name]["display_name"]}}
        old = {**expected, "interface": {"displayName": "Exam Preparation"}}
        other_scope = {**expected, "scope": "repo"}
        verify_codex.verify_labels([expected, other_scope], catalog, "user")
        with self.assertRaisesRegex(RuntimeError, "expected 'Academic Exam Preparation'"):
            verify_codex.verify_labels([old, other_scope], catalog, "user")
        with self.assertRaisesRegex(RuntimeError, "missing or disabled"):
            verify_codex.verify_labels([{**expected, "enabled": False}, other_scope], catalog, "user")

    def test_each_markdown_resource_resolves_inside_its_own_skill(self):
        for name in sorted(NAMES):
            base = SKILLS / name
            for doc in base.rglob("*.md"):
                for href in LINK.findall(doc.read_text(encoding="utf-8")):
                    if href.startswith(("https://", "#")):
                        continue
                    with self.subTest(skill=name, document=doc.name, href=href):
                        path = (doc.parent / href.split("#")[0]).resolve()
                        self.assertTrue(path.is_relative_to(base.resolve()))
                        self.assertTrue(path.is_file(), path)
            if base != MAIN:
                for folder in ("scripts", "references"):
                    for rel, path in inventory(base / folder).items():
                        self.assertEqual(path.read_bytes(), (MAIN / folder / rel).read_bytes(), path)

    def test_documentation_has_no_broken_repository_paths(self):
        pages = [ROOT / "README.md", ROOT / "README.nb.md", ROOT / "CHANGELOG.md"]
        pages.extend((ROOT / "docs").glob("*.md"))
        for page in pages:
            for href in LINK.findall(page.read_text(encoding="utf-8")):
                if href.startswith(("https://", "http://", "#")):
                    continue
                with self.subTest(document=page.name, target=href):
                    path = (page.parent / href.split("#")[0]).resolve()
                    self.assertTrue(path.is_relative_to(ROOT) and path.exists(), path)

    def test_schema_adapter_and_marketplaces(self):
        manifest = document(ROOT / "plugin.json")
        schema = document(ROOT / "tests/schemas/plugin-1.0.0.json")
        self.assertEqual(manifest["$schema"], schema["$id"])
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(schema).validate(manifest)
        ui = manifest["extensions"]["com.openai"]["interface"]
        self.assertEqual(ui["displayName"], "Academic Skill")
        self.assertLessEqual(len(ui["shortDescription"]), 30)
        self.assertLessEqual(len(ui["longDescription"]), 4000)
        for icon in ("logo", "composerIcon"):
            data = (ROOT / ui[icon]).read_bytes()
            self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
            width, height = struct.unpack(">II", data[16:24])
            self.assertEqual(width, height)
            self.assertGreaterEqual(width, 48)
        codex = document(ROOT / ".codex-plugin/plugin.json")
        self.assertEqual(codex["interface"], ui)
        self.assertEqual((ROOT / codex["skills"]).resolve(), SKILLS)
        for folder in [".claude-plugin", ".codex-plugin"]:
            adapter = document(ROOT / folder / "plugin.json")
            self.assertEqual((adapter["name"], adapter["version"]), (manifest["name"], manifest["version"]))
        for path in (".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json"):
            market = document(ROOT / path)
            self.assertEqual(market["name"], "academic-tools")
            plugin, = market["plugins"]
            self.assertEqual(plugin["name"], manifest["name"])
            source = plugin["source"]
            rel = source["path"] if isinstance(source, dict) else source
            self.assertEqual((ROOT / rel).resolve(), ROOT)

    def check_zip(self, archive, files):
        with ZipFile(archive) as package:
            self.assertIsNone(package.testzip())
            self.assertCountEqual(package.namelist(), files.keys())
            for name, source in files.items():
                self.assertNotIn("..", PurePosixPath(name).parts)
                self.assertNotIn("\\", name)
                self.assertEqual(package.read(name), source.read_bytes(), name)

    def test_all_uploads_match_source_files_byte_for_byte(self):
        plugin = {"plugin.json": ROOT / "plugin.json", "assets/icon.png": ROOT / "assets/icon.png"}
        for name in sorted(NAMES):
            with self.subTest(skill=name):
                files = {name + "/" + path: src for path, src in inventory(SKILLS / name).items()}
                self.assertIn(name + "/SKILL.md", files)
                single = ROOT / "dist" / ("" if name == MAIN.name else "individual") / (name + ".zip")
                self.check_zip(single, files)
                plugin.update({"skills/" + path: src for path, src in files.items()})
        self.check_zip(ROOT / "dist/academic-skill-plugin.zip", plugin)
        self.assertEqual(len(list((ROOT / "dist").rglob("*.zip"))), 13)

    def test_build_reproducibility_and_missing_sources(self):
        self.assertEqual(build.build(check=True), [])
        from unittest.mock import patch
        original = build.resources

        def with_missing(directory):
            resources = original(directory)
            if directory.name == "personal-voice":
                resources.add("references/mangler.md")
            return resources

        with patch.object(build, "resources", with_missing), self.assertRaisesRegex(FileNotFoundError, "mangler"):
            dict(build.generated_files())

    def test_behavior_suites_are_complete(self):
        suite = document(MAIN / "evals/evals.json")
        self.assertEqual(suite["skill_name"], MAIN.name)
        cases = suite["evals"]
        self.assertGreaterEqual(len(cases), 10)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        for case in cases:
            self.assertTrue(case["prompt"] and case["expected_output"] and case["expectations"])
            for resource in case.get("files", []):
                self.assertTrue((MAIN / resource).is_file())
        scenarios = document(ROOT / "tests/workflows.json")
        self.assertEqual({c["skill"] for c in scenarios["explicit"]}, NAMES)
        self.assertEqual(len(scenarios["explicit"]), 12)
        self.assertTrue(any(c["expect"] is None for c in scenarios["selection"]))
        for case in scenarios["explicit"]:
            self.assertTrue(case["prompt"] and case["language"] and case["check"])
