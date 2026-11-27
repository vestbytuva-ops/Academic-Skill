"""Verify source discovery, reference routing and both installable archives."""
import io
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree
from zipfile import ZipFile, is_zipfile

import jsonschema
import yaml

from tools import verify_codex

ROOT = Path(__file__).resolve().parents[1]
NAME = "academic-skill"
MAIN = ROOT / "skills" / NAME
SKILL_ZIP = "academic-skill.zip"
CLAUDE_ZIP = "academic-skill-claude-plugin.zip"
MANIFEST = ".claude-plugin/plugin.json"
ARCHIVES = {".zip", ".skill"}
LINK = re.compile(r"\[[^\]]*\]\((<[^>]+>|[^ )]+)\)")


def document(path):
    return json.loads(path.read_text(encoding="utf-8"))


def inventory(directory):
    return {p.relative_to(directory).as_posix(): p for p in directory.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"}


def run_build(root, *args, check=True):
    return subprocess.run([sys.executable, "-B", "-X", "utf8", str(root / "tools/build.py"), *args],
                          cwd=root, check=check, capture_output=True, encoding="utf-8")


class AcademicPackages(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        area = tempfile.TemporaryDirectory()
        cls.addClassCleanup(area.cleanup)
        cls.built = Path(area.name) / "package"
        cls.built.mkdir()
        for directory in ("skills", "tools", "assets", "labs"):
            shutil.copytree(ROOT / directory, cls.built / directory,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        shutil.copy2(ROOT / "plugin.json", cls.built / "plugin.json")
        run_build(cls.built)

    def test_exact_skill_registry_and_metadata(self):
        catalog = document(ROOT / "tools/catalog.json")
        self.assertEqual(set(catalog), {NAME})
        self.assertEqual({p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}, {NAME})
        self.assertEqual(list((ROOT / "skills").rglob("SKILL.md")), [MAIN / "SKILL.md"])
        raw = (MAIN / "SKILL.md").read_bytes()
        self.assertTrue(raw.startswith(b"---\n"))
        self.assertNotIn(b"\r", raw)
        _, header, body = raw.decode().split("---\n", 2)
        meta = yaml.safe_load(header)
        self.assertEqual(meta["name"], NAME)
        self.assertTrue(0 < len(meta["description"]) <= 200)
        self.assertLess(len(body.splitlines()), 300)
        ui = yaml.safe_load((MAIN / "agents/openai.yaml").read_text(encoding="utf-8"))
        self.assertTrue(ui["policy"]["allow_implicit_invocation"])
        self.assertEqual(ui["interface"]["display_name"], catalog[NAME]["display_name"])
        self.assertIn("$" + NAME, ui["interface"]["default_prompt"])
        self.assertTrue(25 <= len(ui["interface"]["short_description"]) <= 64)

    def test_verifier_checks_name_label_and_scope(self):
        catalog = document(ROOT / "tools/catalog.json")
        row = {"name": NAME, "scope": "user", "enabled": True,
               "interface": {"displayName": catalog[NAME]["display_name"]}}
        verify_codex.verify_labels([row, {**row, "name": "unrelated"}], catalog, "user")
        retired = {**row, "name": "humanizer", "interface": {"displayName": "Academic Copyediting"}}
        verify_codex.verify_labels([row, {**retired, "scope": "repo"}], catalog, "user")
        for extra in (row, retired):
            with self.subTest(extra=extra["name"]), self.assertRaises(RuntimeError):
                verify_codex.verify_labels([row, extra], catalog, "user")
        for changed in ({"name": "unrelated"}, {"enabled": False}, {"scope": "repo"},
                        {"interface": {"displayName": "Previous display name"}}):
            with self.subTest(changed=changed), self.assertRaises(RuntimeError):
                verify_codex.verify_labels([{**row, **changed}], catalog, "user")

    def test_markdown_links_and_routing(self):
        refs = {(p.relative_to(MAIN)).as_posix() for p in (MAIN / "references").glob("*.md")}
        routes = set(LINK.findall((MAIN / "SKILL.md").read_text(encoding="utf-8")))
        self.assertTrue(refs.issubset(routes), refs - routes)
        for doc in [*MAIN.rglob("*.md"), *ROOT.glob("*.md"), *(ROOT / "docs").glob("*.md")]:
            for link in LINK.findall(doc.read_text(encoding="utf-8")):
                url = urlsplit(link.strip("<>"))
                if url.scheme or not url.path:
                    continue
                with self.subTest(page=doc.name, link=link):
                    target = (doc.parent / unquote(url.path)).resolve()
                    if doc.is_relative_to(MAIN):
                        self.assertTrue(target.is_relative_to(MAIN) and target.is_file(), target)
                    else:
                        self.assertTrue(target.is_relative_to(ROOT) and target.exists(), target)

    def test_source_tree_and_git_index_are_archive_free(self):
        stray = []
        for directory, subdirs, files in os.walk(ROOT):
            if Path(directory) == ROOT:
                subdirs[:] = [d for d in subdirs if d not in {".git", "dist"}]
            stray.extend(str(Path(directory, f).relative_to(ROOT))
                         for f in files if Path(f).suffix.lower() in ARCHIVES)
        self.assertEqual(stray, [])
        if (ROOT / ".git").exists() and shutil.which("git"):
            cmd = ["git", "-C", str(ROOT), "ls-files", "-z"]
            tracked = subprocess.check_output(cmd).split(b"\0")
            self.assertFalse(any(p.lower().endswith((b".zip", b".skill")) for p in tracked),
                             "An archive is tracked; git archive would include it.")

    def test_manifests_marketplaces_and_icon(self):
        manifest = document(ROOT / "plugin.json")
        schema = document(ROOT / "tests/schemas/plugin-1.0.0.json")
        self.assertEqual(manifest["$schema"], schema["$id"])
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(schema).validate(manifest)
        ui = manifest["extensions"]["com.openai"]["interface"]
        self.assertEqual(ui["displayName"], "Academic Skill")
        self.assertLessEqual(len(ui["shortDescription"]), 30)
        self.assertLessEqual(len(ui["longDescription"]), 4000)
        for field in ("logo", "composerIcon"):
            data = (ROOT / ui[field]).read_bytes()
            self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
            width, height = struct.unpack(">II", data[16:24])
            self.assertEqual(width, height)
            self.assertGreaterEqual(width, 48)
        codex = document(ROOT / ".codex-plugin/plugin.json")
        self.assertEqual(codex["interface"], ui)
        self.assertEqual((ROOT / codex["skills"]).resolve(), ROOT / "skills")
        for path in (MANIFEST, ".codex-plugin/plugin.json"):
            adapter = document(ROOT / path)
            self.assertEqual((adapter["name"], adapter["version"]), (NAME, manifest["version"]))
        for path in (".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json"):
            market = document(ROOT / path)
            self.assertEqual(market["name"], "academic-tools")
            plugin, = market["plugins"]
            self.assertEqual(plugin["name"], NAME)
            source = plugin["source"]
            self.assertEqual((ROOT / (source["path"] if isinstance(source, dict) else source)).resolve(), ROOT)
        for path in (MANIFEST, ".claude-plugin/marketplace.json", ".codex-plugin/plugin.json",
                     ".agents/plugins/marketplace.json", "skills/academic-skill/agents/openai.yaml"):
            self.assertEqual((self.built / path).read_bytes(), (ROOT / path).read_bytes(), path)

    def test_both_archives_have_the_exact_upload_layout(self):
        dist = self.built / "dist"
        self.assertEqual(set(inventory(dist)), {SKILL_ZIP, CLAUDE_ZIP})
        files = inventory(MAIN)
        self.assertIn("SKILL.md", files)
        for archive, prefix in ((SKILL_ZIP, NAME + "/"), (CLAUDE_ZIP, "skills/" + NAME + "/")):
            expected = {prefix + path: source for path, source in files.items()}
            if archive == CLAUDE_ZIP:
                expected[MANIFEST] = ROOT / MANIFEST
            with self.subTest(archive=archive), ZipFile(dist / archive) as package:
                self.assertIsNone(package.testzip())
                self.assertCountEqual(package.namelist(), expected)
                for path, original in expected.items():
                    content = package.read(path)
                    self.assertNotIn(Path(path).suffix.lower(), ARCHIVES, path)
                    self.assertFalse(is_zipfile(io.BytesIO(content)), path)
                    self.assertEqual(content, original.read_bytes(), path)

    def test_visual_tools_work_from_both_upload_archives(self):
        for archive, prefix in ((SKILL_ZIP, NAME), (CLAUDE_ZIP, "skills/" + NAME)):
            with self.subTest(archive=archive), tempfile.TemporaryDirectory() as directory:
                location = Path(directory)
                with ZipFile(self.built / "dist" / archive) as package:
                    package.extractall(location)
                skill = location / prefix
                output = location / "result.drawio"
                subprocess.run(
                    [sys.executable, "-B", str(skill / "scripts/make_drawio.py"),
                     str(skill / "assets/kildearbeid.json"), str(output)],
                    check=True, capture_output=True,
                )
                graph = ElementTree.parse(output)
                self.assertTrue(graph.findall(".//mxCell[@vertex='1']"))
                self.assertTrue(graph.findall(".//mxCell[@edge='1']"))
                for resource in ("scripts/pixel_art.py", "scripts/render_plantuml.py",
                                 "assets/utkast-tilstand.mmd"):
                    self.assertTrue((skill / resource).is_file(), resource)

    def test_reproducible_build_and_rejection_of_stale_or_missing_resources(self):
        with tempfile.TemporaryDirectory() as directory:
            checkout = Path(directory) / "checkout"
            shutil.copytree(self.built, checkout)
            dist = checkout / "dist"
            expected = {name: p.read_bytes() for name, p in inventory(dist).items()}
            shutil.rmtree(dist)
            (checkout / "skills" / NAME / "scripts/pixel_art.py").unlink()
            run_build(checkout)
            self.assertEqual({name: p.read_bytes() for name, p in inventory(dist).items()}, expected)
            run_build(checkout, "--check")
            (dist / SKILL_ZIP).write_bytes(b"stale")
            self.assertNotEqual(run_build(checkout, "--check", check=False).returncode, 0)
            run_build(checkout)
            extra = dist / "retired.skill"
            extra.write_bytes(b"stray")
            self.assertNotEqual(run_build(checkout, "--check", check=False).returncode, 0)
            self.assertTrue(extra.exists())
            extra.unlink()
            (checkout / "skills" / NAME / "references/oppgaveforstaelse.md").unlink()
            self.assertNotEqual(run_build(checkout, check=False).returncode, 0)

    def test_behavior_cases_route_to_existing_references(self):
        available = {p.relative_to(MAIN).as_posix() for p in (MAIN / "references").glob("*.md")}
        suite = document(MAIN / "evals/evals.json")
        self.assertEqual(suite["skill_name"], NAME)
        self.assertEqual({case["id"] for case in suite["evals"]}, set(range(1, 13)))
        for case in suite["evals"]:
            self.assertTrue(case["prompt"] and case["expected_output"] and case["expectations"])
            self.assertEqual(bool(case["references"]), case.get("expect_skill", NAME) == NAME)
            self.assertTrue(set(case["references"]).issubset(available))
            for path in case["files"]:
                self.assertTrue((MAIN / path).is_file(), path)
        trials = document(ROOT / "tests/workflows.json")
        self.assertEqual(len(trials["explicit"]), 15)
        self.assertEqual(len(trials["selection"]), 8)
        self.assertEqual(sum(row["expect"] is None for row in trials["selection"]), 3)
        self.assertEqual({row["language"] for row in trials["explicit"]}, {"nb", "nn", "en"})
        covered = set()
        for row in trials["explicit"]:
            self.assertEqual(row["skill"], NAME)
            self.assertTrue(row["prompt"] and row["check"] and row["references"])
            covered.update(row["references"])
        self.assertEqual(covered, available - {"references/arbeidsgrunnlag.md"})
        for row in trials["selection"]:
            self.assertIn(row["expect"], {NAME, None})
            self.assertEqual(bool(row["references"]), row["expect"] == NAME)
            self.assertTrue(row["prompt"] and set(row["references"]).issubset(available))
        self.assertEqual(trials["missing"]["skill"], NAME)
        self.assertEqual(trials["missing"]["references"], ["references/kildekontroll.md"])
        self.assertTrue(trials["missing"]["prompt"] and trials["missing"]["expect"])
