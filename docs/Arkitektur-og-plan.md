# Arkitektur og utviklingsplan

## Én inngang

Claude finner `academic-skill` under `.claude/skills/`. Hovedfilen velger språk, arbeidsform og referanser. Hver referanse dekker ett arbeidsområde, slik at en enkel bestilling kan løses med lite bakgrunnsstoff. En sammensatt bestilling kan for eksempel gå fra oppgavekrav til kildekontroll og videre til en presentasjon.

| Trinn | Hva som skjer |
| --- | --- |
| Oppgave | Avklar leveranse og avgrens belegg. Velg veiledning, forslag eller produksjon. |
| Arbeid | Les referansene oppgaven krever. Bruk stilgrunnlag fra relevant sjanger og språk når brukeren har delt det. |
| Leveranse | Sammenhold tekst, tabell eller presentasjon med kildene og oppgaven. Vurder virkningen av faglige endringer. |

Stilobservasjoner kan godkjennes, korrigeres, fjernes eller deaktiveres i samtalen. Arbeidsprofilen gjelder den aktuelle oppgaven. Ved motstrid mellom en preferanse og et sjangerkrav, vis konflikten og la brukeren velge der oppgaven åpner for det.

## Kjøring og verktøy

Den valgfrie tekstkontrollen bruker Python-standardbiblioteket og autoriserte tekstfiler. Ved manglende kodekjøring sammenlignes uttrykkene manuelt. Ved bestilt Office-leveranse, bruk verktøyene verten har tilgang til, kontroller at filen kan åpnes, og sjekk lesbarheten når den kan vurderes. Med et utdrag kan brukeren få et konkret forslag å overføre til filen.

## Videre prøver

- Gjenta evalene på lengre tekster og på begge språk i målverten. Bruk samme kilder og bestillinger i sammenligningen.
- Test filproduksjon med en uavhengig leser. Sammenlign DOCX, XLSX og PPTX med kildeinnholdet og se etter avskjæring og lesbarhetsfeil.
- Prøv at retting, fjerning og deaktivering i samtalen virker for ulike oppgaver og skrivestemmer.

[Kilderegister](Kilderegister.md) · [Historiske testresultater](Testresultater.md) · [Endringslogg og nye evalresultater](../CHANGELOG.md)
