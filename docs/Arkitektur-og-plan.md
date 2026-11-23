# Arkitektur og utviklingsplan

## Én ferdighet med flere arbeidsmåter

[SKILL.md](../skills/academic-skill/SKILL.md) styrer språk, arbeidsform og hvilke referanser som leses. Oppgaven kan kreve én arbeidsmåte eller flere i rekkefølge. Et fireminutters foredrag om en undersøkelse kan for eksempel kreve kildekontroll før lysbildene planlegges. [Oversikt over arbeidsmåtene](../README.nb.md)

| Trinn | Hva som skjer |
| --- | --- |
| Oppgave | Avklar leveranse, vurderingskriterier og belegg. Velg veiledning, forslag eller produksjon. |
| Arbeid | Les de relevante filene i `references/`. Bruk skriveprøver og preferanser brukeren har oppgitt for oppgaven. |
| Leveranse | Sammenhold utkastet med kildene. Ved en filbestilling, kontroller dokumentet med verktøy som er tilgjengelige og autoriserte. |

Stilobservasjoner kan godkjennes, korrigeres, fjernes eller deaktiveres i samtalen. Arbeidsprofilen gjelder den aktuelle oppgaven. Ved motstrid mellom en preferanse og et sjangerkrav, gjør konflikten synlig og la brukeren velge der oppgaven åpner for det.

## Kilder og pakking

Fagtekstene vedlikeholdes under [references](../skills/academic-skill/references). Læringsveiledning og eksamensøving deler én referanse. Norsk skole og engelsk akademisk skriving har egne språk- og sjangerråd. Den valgfrie [uttrykkskontrollen](../skills/academic-skill/scripts/sjekk_uttrykk.py) sammenligner brukerens godkjente tekstgrunnlag ved sluttkontroll.

[Katalogen](../tools/catalog.json) beskriver brukerens ene menyvalg. [Rotmanifestet](../plugin.json) gir identitet og metadata til klientadapterne. Byggeskriptet genererer disse og pakker skillens filer i to arkiver, ett for skillimport og ett for Claudes pluginimport. Ferdige arkiver distribueres utenfor Git-kildetreet. [Bygging og distribusjon](Release.md)

## Videre prøver

- Kjør de samme [testoppgavene](../tests/workflows.json) før og etter endringer. Registrer hvilken referanse oppgaven krever, og vurder selve svaret mot kriteriene.
- Prøv lengre tekster på begge språk i målverten. Ved dokumentproduksjon, åpne DOCX, XLSX eller PPTX i en uavhengig leser og sammenlign med grunnlaget.
- Prøv retting, fjerning og deaktivering av stilvalg i en samtale. Undersøk om stemme, tall og sitater blir bevart.

[Kilderegister](Kilderegister.md) · [Tidligere evalresultater](Testresultater.md) · [Teststatus](Validation.md) · [Endringslogg](../CHANGELOG.md)
