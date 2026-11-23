# Arkitektur og utviklingsplan

## Hovedskill og elleve spesialister

Kilden ligger i `skills/`, med én mappe for hvert av de tolv navnene. Installeren kopierer den til banen verten leser. Hovedfilen velger språk, arbeidsform og referanser. Hver referanse dekker ett arbeidsområde, slik at en enkel bestilling kan løses med lite bakgrunnsstoff. En sammensatt bestilling kan for eksempel gå fra oppgavekrav til kildekontroll og videre til en presentasjon.

| Trinn | Hva som skjer |
| --- | --- |
| Oppgave | Avklar leveranse og avgrens belegg. Velg veiledning, forslag eller produksjon. |
| Arbeid | Les referansene oppgaven krever. Bruk stilgrunnlag fra relevant sjanger og språk når brukeren har delt det. |
| Leveranse | Sammenhold tekst, tabell eller presentasjon med kildene og oppgaven. Vurder virkningen av faglige endringer. |

Stilobservasjoner kan godkjennes, korrigeres, fjernes eller deaktiveres i samtalen. Arbeidsprofilen gjelder den aktuelle oppgaven. Ved motstrid mellom en preferanse og et sjangerkrav, vis konflikten og la brukeren velge der oppgaven åpner for det.

## Felles kilder og pakking

Rediger fagreferanser og uttrykkskontrollen i `skills/academic-skill/`. Frittstående spesialister peker på relevante filer i sin egen mappe. Byggeskriptet henter disse fra hovedskillens kilder og lager versjonerte ZIP-filer uten symlenker. Endre visningsnavn og eksempler i `tools/catalog.json`. Kjør `python tools/build.py` og `python tools/build.py --check` etter endringer. Ressursene fungerer også når en bruker installerer bare én spesialist.

Rotmanifestet er kilden til plugin-identiteten og klientadapterne. Codex og Claude Code har separate markedsplassformater. ChatGPT Work importerer pluginpakken. Claude.ai importerer ett skillarkiv per oppføring. [Installasjon og kompatibilitet](Compatibility.md)

## Kjøring og verktøy

Den valgfrie tekstkontrollen bruker Python-standardbiblioteket og autoriserte tekstfiler. Ved manglende kodekjøring sammenlignes uttrykkene manuelt. Ved bestilt Office-leveranse, bruk verktøyene verten har tilgang til, kontroller at filen kan åpnes, og sjekk lesbarheten når den kan vurderes. Med et utdrag kan brukeren få et konkret forslag å overføre til filen.

## Videre prøver

- Gjenta evalene på lengre tekster og på begge språk i målverten. Bruk samme kilder og bestillinger i sammenligningen.
- Test filproduksjon med en uavhengig leser. Sammenlign DOCX, XLSX og PPTX med kildeinnholdet og se etter avskjæring og lesbarhetsfeil.
- Prøv at retting, fjerning og deaktivering i samtalen virker for ulike oppgaver og skrivestemmer.

[Kilderegister](Kilderegister.md) · [Historiske testresultater](Testresultater.md) · [Endringslogg og nye evalresultater](../CHANGELOG.md)
