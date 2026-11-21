"""Check that the download installs as one complete, up-to-date skill."""

import unittest
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "academic-skill"


class SkillPackageTests(unittest.TestCase):
    def test_archive_matches_installable_directory(self):
        files = {
            path.relative_to(SKILL.parent).as_posix(): path
            for path in SKILL.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        self.assertIn("academic-skill/SKILL.md", files)
        with ZipFile(ROOT / "dist" / "academic-skill.zip") as archive:
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
