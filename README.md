# Academic Skill

Academic Skill er en skrive- og læringsveileder for elever og studenter som bruker Codex. Gi den oppgaven, et avsnitt du har skrevet, og si hva du vil ha hjelp med. Du kan be om et spørsmål som hjelper deg å skrive videre selv, få forslag til én formulering eller få hele utkastet språkvasket.

## Kom i gang

1. Last ned prosjektet med **Code → Download ZIP** på GitHub og pakk ut arkivet. Har du allerede klonet repoet, kan du hente V2 med `git pull --ff-only`.
2. Åpne mappen som inneholder `README.md` og `START-HER.md` som prosjekt i Codex.
3. Start en ny samtale og prøv denne bestillingen.

> Bruk $academic-skill. I metodedelen skrev jeg «Intervjuene viste hva alle studentene mente». Jeg intervjuet to studenter. Gi meg én mer presis formulering, og forklar hva du endret.

Her kan veilederen foreslå «Intervjuene viste hva de to studentene mente». Ordet «to» avgrenser påstanden til dem som faktisk deltok. Vil du finne formuleringen selv, kan du avslutte bestillingen med «Still meg ett spørsmål, så prøver jeg igjen».

## Velg hvordan du vil jobbe

| Når du vil … | Be om | Hva du får |
| --- | --- | --- |
| skrive videre selv | **Veiledning** | Ett grep å prøve i ditt eget avsnitt, gjerne knyttet til en kommentar fra læreren. |
| vurdere en formulering | **Forslag** | Et konkret alternativ og en forklaring på hvordan det påvirker teksten. Du velger hva du vil bruke. |
| få et utkast eller bearbeide en tekst | **Utkast, revisjon eller språkvask** | En tekst i ønsket sjanger og målform. Ved revisjon kan du se hva som er endret. |

**Din skrivestemme.** Del noen setninger du selv har skrevet, og fortell hvilken sjanger de tilhører. Du kan be om å få se hvilke trekk veilederen har lagt merke til, rette en observasjon eller be den legge trekket til side. Stilprofilen gjelder oppgaven du jobber med.

**Kilder og forskning.** Som utgangspunkt bruker veilederen materialet du deler. Ber du om kildekontroll, viser den hvor en påstand har støtte, hvor materialet motsier den, eller hva som fortsatt er uavklart. Du kan også be om eksterne kilder, hjelp til å velge metode eller en tolkning av data du har delt.

## Finn fram i prosjektet

| Fil eller mappe | Hva du finner der |
| --- | --- |
| [START-HER.md](START-HER.md) | En kort bruksguide og tips til å prøve din egen skrivestemme. |
| [Ferdigheten](.agents/skills/academic-skill/SKILL.md) | Instruksjonene Codex leser og bruker til å velge arbeidsform. |
| [Fagveiledningene](.agents/skills/academic-skill/references/) | Personlig stil, akademisk skriving, norskfaglig veiledning og forskningsmetode. |
| [Dokumentasjon](docs/) | [Utviklingsplan](docs/Arkitektur-og-plan.md), [kilderegister](docs/Kilderegister.md) og [resultater fra V2-piloten](docs/Testresultater.md). |
| [Tester og skriveprøver](tests/) | Sju skriveoppgaver med tilhørende svar og vurderingskriterier, samt automatiske tester av tekstkontrollen. |

## Prøv V2 selv

For å vurdere skriveveiledningen kan du velge én av [de sju oppgavene](tests/cases.json), prøve den i en ny samtale og sammenligne svaret med [vurderingsnøkkelen](tests/Vurderingsnokkel.md). Oppgavene bygger på oppdiktede skriveprøver.

Skriveveiledningen kan brukes uten Python eller Office. Den valgfrie [tekstkontrollen](.agents/skills/academic-skill/scripts/check_spans.py) bruker Python 3 til å telle forekomster av uttrykk du selv velger, for eksempel et sitat med sidetall. Et sitat kan fortsatt ha skiftet betydning i sammenhengen selv om ordlyden og antallet stemmer.

Kjør de 15 automatiske testene av tekstkontrollen fra prosjektmappen med

```sh
python -B -m unittest discover -s tests -v
```
