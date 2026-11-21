"""Exercise the offline span checker through its public command line."""

import codecs
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = (
    Path(__file__).resolve().parents[1]
    / ".agents" / "skills" / "academic-skill" / "scripts" / "check_spans.py"
)


class SpanCheckerTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        folder = Path(temporary.name)
        self.source = folder / "private-original.txt"
        self.revised = folder / "private-revision.txt"
        self.spans = folder / "private-selections.json"

    def prepare(self, source, revised, spans):
        self.source.write_bytes(source.encode("utf-8"))
        self.revised.write_bytes(revised.encode("utf-8"))
        self.spans.write_bytes(json.dumps(spans, ensure_ascii=False).encode("utf-8"))

    def expect(self, status, lines, *paths):
        result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), *map(str, paths)],
            capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(result.returncode, status)
        self.assertEqual(result.stdout.splitlines(), lines)
        self.assertEqual(result.stderr, "")

    def check(self, status, *lines):
        self.expect(status, list(lines), self.source, self.revised, self.spans)

    def test_norwegian_and_english_with_repeated_measurements(self):
        attribution = "«svak økning» (Åsen, 2022, s. 7)"
        quantity = "2,5 µg/L"
        term = "confidence interval"
        self.prepare(
            f"De skrev {attribution}. {quantity}, så {quantity}. The {term} was wide.",
            f"The {term} was wide. Forfatterne skrev {attribution}. {quantity} og {quantity}.",
            [attribution, quantity, term, quantity],
        )
        self.check(0, "PASS")

    def test_reports_missing_and_added_occurrences_by_index_only(self):
        self.prepare(
            "Holt (2020) found 9 mg. Holt (2020) confirmed 9 mg.",
            "Holt (2020) found 9 mg. Repeats: 9 mg, 9 mg.",
            ["Holt (2020)", "9 mg"],
        )
        self.check(
            1,
            "FAIL index=0 source_count=2 revised_count=1",
            "FAIL index=1 source_count=2 revised_count=3",
        )

    def test_reports_an_altered_quote_without_printing_it(self):
        self.prepare("«hemmelig» (A, s. 4)", "«hemmelig» (A, s. 5)", ["«hemmelig» (A, s. 4)"])
        self.check(1, "FAIL index=0 source_count=1 revised_count=0")

    def test_unicode_and_newlines_are_exact(self):
        for before, after in [
            ("café", "cafe\u0301"),
            ("3\u00a0kg", "3 kg"),
            ("A\r\nB", "A\nB"),
            ("A\rB", "A\nB"),
        ]:
            with self.subTest(before=before):
                self.prepare(before, before, [before])
                self.check(0, "PASS")
                self.prepare(before, after, [before])
                self.check(1, "FAIL index=0 source_count=1 revised_count=0")

    def test_counts_overlapping_matches(self):
        self.prepare("aaaa", "aaa", ["aa"])
        self.check(1, "FAIL index=0 source_count=3 revised_count=2")

    def test_optional_bom_on_each_input_preserves_interior_content(self):
        for path in [self.source, self.revised, self.spans]:
            with self.subTest(path=path.name):
                self.prepare("A\ufeffB", "A\ufeffB", ["\ufeff", "A\ufeffB"])
                path.write_bytes(codecs.BOM_UTF8 + path.read_bytes())
                self.check(0, "PASS")

    def test_numeric_spans_do_not_match_larger_integers_or_decimals(self):
        for span, revised in [
            ("12 av 18", "112 av 18"),
            ("12 av 18", "12 av 180"),
            ("12 av 18", "112 av 180"),
            ("12 av 18", "12 av 18,5"),
            ("12 av 18", "12 av 18.5"),
            ("9 mg", "2,9 mg"),
            ("9 mg", "2.9 mg"),
            ("9 mg", "٤9 mg"),
        ]:
            with self.subTest(revised=revised):
                self.prepare(span, revised, [span])
                self.check(1, "FAIL index=0 source_count=1 revised_count=0")

    def test_sentence_punctuation_and_complete_decimal_match(self):
        self.prepare(
            "12 av 18. Dose 2,9 mg.",
            "Dose 2,9 mg. Hos 12 av 18, med oppfølging.",
            ["12 av 18", "2,9 mg"],
        )
        self.check(0, "PASS")

    def test_number_fragment_absent_in_source_is_invalid(self):
        self.prepare("2,9 mg", "9 mg", ["9 mg"])
        self.check(2, "FAIL index=0 source_count=0")

    def test_empty_revision_loses_all_selected_text(self):
        self.prepare("private datum", "", ["private datum"])
        self.check(1, "FAIL index=0 source_count=1 revised_count=0")

    def test_span_absent_from_source_takes_precedence(self):
        self.prepare("private datum", "new datum", ["private datum", "new datum"])
        self.check(2, "FAIL index=1 source_count=0")

    def test_invalid_manifest_shape(self):
        for value in [[], {}, None, "private datum"]:
            with self.subTest(value=value):
                self.prepare("source", "revised", value)
                self.check(2, "FAIL")
        for value in ["", 17, None, ["nested"]]:
            with self.subTest(value=value):
                self.prepare("source", "source", ["source", value])
                self.check(2, "FAIL index=1")

    def test_malformed_json_and_missing_file(self):
        self.prepare("private datum", "private datum", [])
        self.spans.write_bytes(b'["private datum",]')
        self.check(2, "FAIL")
        self.spans.unlink()
        self.check(2, "FAIL")

    def test_invalid_utf8_in_each_input(self):
        for path in [self.source, self.revised, self.spans]:
            with self.subTest(path=path.name):
                self.prepare("private datum", "private datum", ["private datum"])
                path.write_bytes(b"private content\xff")
                self.check(2, "FAIL")

    def test_wrong_argument_count_does_not_echo_paths(self):
        self.expect(2, ["FAIL"], self.source)
        self.expect(2, ["FAIL"], self.source, self.revised, self.spans, "private extra argument")


if __name__ == "__main__":
    unittest.main()
