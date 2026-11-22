"""Test det frakoblede uttrykksskriptet gjennom kommandolinjen."""

import codecs
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = (
    Path(__file__).resolve().parents[1]
    / ".agents" / "skills" / "academic-skill" / "scripts" / "sjekk_uttrykk.py"
)


class UttrykkskontrollTester(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        folder = Path(temporary.name)
        self.source = folder / "privat-original.txt"
        self.revised = folder / "privat-revisjon.txt"
        self.spans = folder / "privat-uttrykk.json"

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

    def test_norsk_og_engelsk_med_gjentatte_maalinger(self):
        attribution = "«svak økning» (Åsen, 2022, s. 7)"
        quantity = "2,5 µg/L"
        term = "confidence interval"
        self.prepare(
            f"De skrev {attribution}. {quantity}, så {quantity}. The {term} was wide.",
            f"The {term} was wide. Forfatterne skrev {attribution}. {quantity} og {quantity}.",
            [attribution, quantity, term, quantity],
        )
        self.check(0, "BESTÅTT")

    def test_manglende_og_nye_forekomster_rapporteres_med_indeks(self):
        self.prepare(
            "Holt (2020) found 9 mg. Holt (2020) confirmed 9 mg.",
            "Holt (2020) found 9 mg. Repeats: 9 mg, 9 mg.",
            ["Holt (2020)", "9 mg"],
        )
        self.check(
            1,
            "FEIL indeks=0 antall_original=2 antall_revisjon=1",
            "FEIL indeks=1 antall_original=2 antall_revisjon=3",
        )

    def test_endret_sitat_rapporteres_uten_sitattekst(self):
        self.prepare("«hemmelig» (A, s. 4)", "«hemmelig» (A, s. 5)", ["«hemmelig» (A, s. 4)"])
        self.check(1, "FEIL indeks=0 antall_original=1 antall_revisjon=0")

    def test_unicode_og_linjeskift_sammenlignes_noeyaktig(self):
        for before, after in [
            ("café", "cafe\u0301"),
            ("3\u00a0kg", "3 kg"),
            ("A\r\nB", "A\nB"),
            ("A\rB", "A\nB"),
        ]:
            with self.subTest(before=before):
                self.prepare(before, before, [before])
                self.check(0, "BESTÅTT")
                self.prepare(before, after, [before])
                self.check(1, "FEIL indeks=0 antall_original=1 antall_revisjon=0")

    def test_teller_overlappende_treff(self):
        self.prepare("aaaa", "aaa", ["aa"])
        self.check(1, "FEIL indeks=0 antall_original=3 antall_revisjon=2")

    def test_bom_i_starten_bevarer_tegn_inne_i_teksten(self):
        for path in [self.source, self.revised, self.spans]:
            with self.subTest(path=path.name):
                self.prepare("A\ufeffB", "A\ufeffB", ["\ufeff", "A\ufeffB"])
                path.write_bytes(codecs.BOM_UTF8 + path.read_bytes())
                self.check(0, "BESTÅTT")

    def test_talluttrykk_treffes_ikke_i_stoerre_tall(self):
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
                self.check(1, "FEIL indeks=0 antall_original=1 antall_revisjon=0")

    def test_tegnsetting_og_komplette_desimaltall(self):
        self.prepare(
            "12 av 18. Dose 2,9 mg.",
            "Dose 2,9 mg. Hos 12 av 18, med oppfølging.",
            ["12 av 18", "2,9 mg"],
        )
        self.check(0, "BESTÅTT")

    def test_tallfragment_som_mangler_i_originalen_er_ugyldig(self):
        self.prepare("2,9 mg", "9 mg", ["9 mg"])
        self.check(2, "FEIL indeks=0 antall_original=0")

    def test_tom_revisjon_mangler_alle_valgte_uttrykk(self):
        self.prepare("private datum", "", ["private datum"])
        self.check(1, "FEIL indeks=0 antall_original=1 antall_revisjon=0")

    def test_ugyldig_grunnlag_har_fortrinn_framfor_avvik(self):
        self.prepare("private datum", "new datum", ["private datum", "new datum"])
        self.check(2, "FEIL indeks=1 antall_original=0")

    def test_ugyldig_uttrykksliste(self):
        for value in [[], {}, None, "private datum"]:
            with self.subTest(value=value):
                self.prepare("source", "revised", value)
                self.check(2, "FEIL")
        for value in ["", 17, None, ["nested"]]:
            with self.subTest(value=value):
                self.prepare("source", "source", ["source", value])
                self.check(2, "FEIL indeks=1")

    def test_ugyldig_json_og_manglende_fil(self):
        self.prepare("private datum", "private datum", [])
        self.spans.write_bytes(b'["private datum",]')
        self.check(2, "FEIL")
        self.spans.unlink()
        self.check(2, "FEIL")

    def test_ugyldig_utf8_i_hver_inndatafil(self):
        for path in [self.source, self.revised, self.spans]:
            with self.subTest(path=path.name):
                self.prepare("private datum", "private datum", ["private datum"])
                path.write_bytes(b"private content\xff")
                self.check(2, "FEIL")

    def test_feil_antall_argumenter_viser_ikke_filstier(self):
        self.expect(2, ["FEIL"], self.source)
        self.expect(2, ["FEIL"], self.source, self.revised, self.spans, "private extra argument")

    def test_norske_bokstaver_og_kommatall(self):
        self.prepare(
            "Ærlig talt: «Øyvind fant 2,9 mg» (Åse, s. 3). Så 12 av 18 på Ås.",
            "På Ås: 12 av 18. «Øyvind fant 2,9 mg» (Åse, s. 3). Ærlig talt.",
            ["Ærlig talt", "«Øyvind fant 2,9 mg» (Åse, s. 3)", "2,9 mg", "12 av 18", "Ås"],
        )
        self.check(0, "BESTÅTT")

    def test_komma_i_tall_endrer_betydning(self):
        self.prepare("Dose 2,9 mg.", "Dose 29 mg.", ["2,9 mg"])
        self.check(1, "FEIL indeks=0 antall_original=1 antall_revisjon=0")


if __name__ == "__main__":
    unittest.main()
