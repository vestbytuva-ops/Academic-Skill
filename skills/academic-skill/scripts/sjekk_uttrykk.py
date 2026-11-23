"""Sammenlign nøyaktig antall forekomster av valgte uttrykk i to lokale UTF-8-tekster.

Bruk:
    python sjekk_uttrykk.py original.txt revisjon.txt uttrykk.json

Filen uttrykk.json er en JSON-liste med tekststrenger som er hentet ordrett fra originalen,
for eksempel ["12 av 18", "«litt lettere» (Vedlegg A, s. 2)"].

Avslutningskoder:
    0  likt antall av alle uttrykk
    1  minst ett uttrykk har endret antall
    2  ugyldig grunnlag (manglende fil, ugyldig JSON, tomt uttrykk, uttrykk som ikke finnes i originalen)

Skriptet sammenligner bare bokstavelige tegnrekker. Det skriver aldri ut selve teksten
eller hvor i teksten uttrykket står, bare hvilken plass uttrykket har i JSON-listen.
"""

import json
import re
import sys
from pathlib import Path


def tell_forekomster(tekst, uttrykk):
    """Tell overlappende bokstavelige treff og avvis deler av tall i kantene.

    Starter uttrykket med et siffer, teller det ikke som treff når et siffer eller et
    desimalskilletegn mellom to siffer står rett foran. Slutter uttrykket med et siffer,
    gjelder det samme etter uttrykket. Da skilles «9 mg» fra «19 mg» og «2,9 mg».
    Et punktum som avslutter setningen er fortsatt tillatt.
    """
    venstre = r"(?<!\d)(?<!\d[.,])" if uttrykk[0].isdecimal() else ""
    hoyre = r"(?!\d|[.,]\d)" if uttrykk[-1].isdecimal() else ""
    moenster = re.compile(venstre + re.escape(uttrykk) + hoyre)
    antall = 0
    treff = moenster.search(tekst)
    while treff:
        antall += 1
        treff = moenster.search(tekst, treff.start() + 1)
    return antall


def sjekk_uttrykk(original, revisjon, uttrykk_liste):
    """Returner (avslutningskode, rapportlinjer). Indeksene teller fra null i JSON-listen."""
    if not isinstance(original, str) or not isinstance(revisjon, str):
        return 2, ["FEIL"]
    if not isinstance(uttrykk_liste, list) or not uttrykk_liste:
        return 2, ["FEIL"]

    avvik = []
    for indeks, uttrykk in enumerate(uttrykk_liste):
        if not isinstance(uttrykk, str) or not uttrykk:
            return 2, [f"FEIL indeks={indeks}"]
        antall_original = tell_forekomster(original, uttrykk)
        if antall_original == 0:
            return 2, [f"FEIL indeks={indeks} antall_original=0"]
        antall_revisjon = tell_forekomster(revisjon, uttrykk)
        if antall_revisjon != antall_original:
            avvik.append(
                f"FEIL indeks={indeks} antall_original={antall_original} "
                f"antall_revisjon={antall_revisjon}"
            )
    if avvik:
        return 1, avvik
    return 0, ["BESTÅTT"]


def les_utf8(sti):
    # Å lese bytes bevarer CR, LF og CRLF inne i sitert tekst.
    return Path(sti).read_bytes().decode("utf-8-sig")


def hovedprogram(argumenter):
    """Les tre stier: originaltekst, revidert tekst og JSON-liste med uttrykk."""
    if len(argumenter) != 3:
        print("FEIL")
        return 2
    try:
        original = les_utf8(argumenter[0])
        revisjon = les_utf8(argumenter[1])
        uttrykk_liste = json.loads(les_utf8(argumenter[2]))
    except (OSError, ValueError, RecursionError):
        print("FEIL")
        return 2
    status, linjer = sjekk_uttrykk(original, revisjon, uttrykk_liste)
    for linje in linjer:
        print(linje)
    return status


if __name__ == "__main__":
    sys.exit(hovedprogram(sys.argv[1:]))
