"""Check that both downloads match their installable skill directories."""

import unittest
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
SKILL_NAMES = {
    "academic-skill",
    "academic-core",
    "personal-voice",
    "academic-writing",
    "humanizer",
    "academic-critic",
    "research-integrity",
    "learning-coach",
    "exam-preparation",
    "presentation-engine",
    "office-integration",
    "quality-assurance",
}


class SkillPackageTests(unittest.TestCase):
    def test_archive_matches_installable_directory(self):
        main_skill = SKILLS / "academic-skill"
        self.assertTrue((main_skill / "SKILL.md").is_file())
        self.assertTrue((main_skill / "scripts" / "sjekk_uttrykk.py").is_file())
        self.assert_archive_matches("academic-skill.zip", main_skill)

    def test_suite_archive_has_all_twelve_skill_choices(self):
        self.assertEqual({path.parent.name for path in SKILLS.glob("*/SKILL.md")}, SKILL_NAMES)
        self.assert_archive_matches("academic-skill-suite.zip", SKILLS)

    def assert_archive_matches(self, archive_name, source_directory):
        files = {
            path.relative_to(SKILLS).as_posix(): path
            for path in source_directory.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        with ZipFile(ROOT / "dist" / archive_name) as archive:
            names = [item.filename for item in archive.infolist() if not item.is_dir()]
            self.assertCountEqual(names, files.keys())
            for name in names:
                with self.subTest(name=name):
                    source = files[name].read_bytes()
                    packaged = archive.read(name)
                    # Git can check out these text files with CRLF on Windows.
                    if files[name].suffix in {".md", ".yaml", ".py"}:
                        source = source.replace(b"\r\n", b"\n")
                        packaged = packaged.replace(b"\r\n", b"\n")
                    self.assertEqual(source, packaged)
