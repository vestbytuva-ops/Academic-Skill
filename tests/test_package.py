"""Kontroller at Claude-pakken inneholder én komplett skill."""

import json
import unittest
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".claude" / "skills"
SKILL = SKILLS / "academic-skill"
ARCHIVE = ROOT / "dist" / "academic-skill.zip"
REQUIRED_FILES = {
    "SKILL.md",
    "references/english.md",
    "references/kildekontroll.md",
    "references/kritikk.md",
    "references/laering-og-eksamen.md",
    "references/norsk-skole.md",
    "references/office-filer.md",
    "references/oppgaveforstaelse.md",
    "references/personlig-stemme.md",
    "references/presentasjoner.md",
    "references/skriving.md",
    "references/sluttkontroll.md",
    "references/sprakvask.md",
    "scripts/sjekk_uttrykk.py",
    "evals/evals.json",
}


class SkillPackageTests(unittest.TestCase):
    def test_one_complete_claude_skill(self):
        self.assertEqual(list(SKILLS.rglob("SKILL.md")), [SKILL / "SKILL.md"])
        self.assertEqual(list((ROOT / ".agents").rglob("SKILL.md")), [])
        self.assertEqual(list(ARCHIVE.parent.glob("*.zip")), [ARCHIVE])
        for name in sorted(REQUIRED_FILES):
            with self.subTest(name=name):
                self.assertTrue((SKILL / name).is_file())
        self.assertFalse((SKILL / "agents").exists())

    def test_archive_matches_installable_directory(self):
        files = {
            path.relative_to(SKILLS).as_posix(): path
            for path in SKILL.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        with ZipFile(ARCHIVE) as archive:
            self.assertIsNone(archive.testzip())
            entries = archive.infolist()
            roots = {entry.filename.split("/", 1)[0] for entry in entries}
            self.assertEqual(roots, {SKILL.name})
            self.assertCountEqual(
                [entry.filename for entry in entries if not entry.is_dir()], files
            )
            for name, path in files.items():
                with self.subTest(name=name):
                    source = path.read_bytes()
                    packaged = archive.read(name)
                    # Git kan sjekke ut tekstfiler med CRLF på Windows.
                    if path.suffix in {".md", ".py", ".json"}:
                        source = source.replace(b"\r\n", b"\n")
                        packaged = packaged.replace(b"\r\n", b"\n")
                    self.assertEqual(source, packaged)

    def test_packaged_evals_have_unique_ids_and_complete_prompts(self):
        with ZipFile(ARCHIVE) as archive:
            suite = json.loads(archive.read("academic-skill/evals/evals.json"))
        self.assertEqual(suite["skill_name"], SKILL.name)
        cases = suite["evals"]
        self.assertGreaterEqual(len(cases), 10)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        for case in cases:
            with self.subTest(eval_id=case["id"]):
                self.assertTrue(case["prompt"].strip())
                self.assertTrue(case["expected_output"].strip())
                self.assertTrue(case["expectations"])
                for name in case.get("files", []):
                    self.assertTrue((SKILL / name).is_file())
