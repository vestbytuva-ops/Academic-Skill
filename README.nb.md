# Academic Skill

[English](README.md) | Norsk bokmål

**NOTE!** Academic Skill er en norsk skill som også kan brukes på engelsk. Be om språket oppgaven krever.

Academic Skill hjelper elever og studenter med å forstå oppgaver, øve til eksamen, vurdere kilder og metode, bearbeide utkast og planlegge presentasjoner. Del oppgaven, materialet du vil jobbe med, og si hva du vil ha hjelp med.

## Installer for alle lokale prosjekter

Åpne Codex på maskinen der du bruker prosjektene dine, og lim inn denne meldingen én gang.

```text
Installer skillen fra https://github.com/vestbytuva-ops/Academic-Skill/ for alle mine lokale Codex-prosjekter.
```

Du kan også bruke `$skill-installer` med [lenken til skillmappen][skillmappe]. Ved manuell installasjon pakker du ut [academic-skill.zip][skill-zip] og legger mappen `academic-skill` i `~/.codex/skills/` (`%USERPROFILE%\.codex\skills` på Windows). Har du satt `CODEX_HOME`, bruker du mappen `skills` under den. Den installerte filen skal ligge på `skills/academic-skill/SKILL.md`.

Etter installasjonen åpner du en ny Codex-samtale og velger `$academic-skill`. For å bruke skillen bare i dette prosjektet kan du åpne repoet som et Codex-prosjekt.

## Bruk i ChatGPT Work

Last ned [academic-skill.zip][skill-zip]. Hvis arbeidsområdet støtter opplasting av skills, velger du **Plugins → Skills → Create → Upload from your computer** og laster opp ZIP-filen. Etter installasjonen åpner du en ny Work-samtale, skriver `@` og velger **Academic Skill**. [OpenAIs veiledning for opplasting][chatgpt-skills]

## Velg et arbeidsområde

De elleve arbeidsområdene på nettsiden kan brukes hver for seg. Repoet installerer én skill med navnet `academic-skill`. Velg skillen, nevn arbeidsområdet og beskriv oppgaven.

> Bruk $academic-skill. Fokuser på exam-preparation. Still meg ett spørsmål om gangen fra disse notatene. Vent på svaret mitt før du gir tilbakemelding.

| Navn på nettsiden | Dette kan du be om |
| --- | --- |
| `academic-core` | Bryt ned oppgaven og finn ut hva du bør avklare før du begynner. |
| `personal-voice` | Finn ordvalg, rytme og tone i en egen skriveprøve og bruk dem som stilgrunnlag. |
| `academic-writing` | Knytt problemstilling, argumenter, belegg og konklusjon sammen. |
| `humanizer` | Forbedre flyten i teksten og bevar meningen og skrivestemmen din. |
| `academic-critic` | Vurder et utkast mot kriteriene eller lærerens respons, og foreslå ett sted å revidere. |
| `research-integrity` | Sjekk hvilke påstander kildene og metoden støtter. |
| `learning-coach` | Forklar et faglig begrep, gi én øvelse og vent på svaret ditt. |
| `exam-preparation` | Still spørsmål fra notatene dine eller lag øvingskort til et tema. |
| `presentation-engine` | Planlegg lysbilder og talepunkter for målgruppen og taletiden. |
| `office-integration` | Bruk verktøyene i samtalen til å jobbe med utdrag eller filer fra Word, Excel eller PowerPoint. |
| `quality-assurance` | Sjekk utkastet mot oppgaven og pek ut sitater, tall eller påstander som bør kontrolleres. |

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
| [Instruksjonene](.agents/skills/academic-skill/SKILL.md) | Instruksjonene skillen bruker til å velge arbeidsform. |
| [Fagveiledningene](.agents/skills/academic-skill/references/) | Personlig stil, akademisk skriving, norskfaglig veiledning og forskningsmetode. |
| [Dokumentasjon](docs/) | [Utviklingsplan](docs/Arkitektur-og-plan.md), [kilderegister](docs/Kilderegister.md) og [resultater fra V2-piloten](docs/Testresultater.md). |
| [Tester og skriveprøver](tests/) | Sju skriveoppgaver med tilhørende svar og vurderingskriterier, samt automatiske tester. |

## Prøv V2 selv

Prøv én av [de sju oppgavene](tests/cases.json) i en ny samtale og sammenlign svaret med [vurderingsnøkkelen](tests/Vurderingsnokkel.md). Oppgavene bygger på oppdiktede skriveprøver.

Skriveveiledningen kan brukes uten Python eller Office. Den valgfrie [tekstkontrollen](.agents/skills/academic-skill/scripts/check_spans.py) bruker Python 3 til å telle forekomster av uttrykk du velger, for eksempel et sitat med sidetall. Vurder også betydningen uttrykkene har i sammenhengen.

Når du har lagret en endring i skillmappen i Git, bygger du ZIP-filen på nytt. Kjør begge kommandoene fra prosjektmappen.

```sh
git archive --format=zip --prefix=academic-skill/ --output=dist/academic-skill.zip HEAD:.agents/skills/academic-skill
python -B -m unittest discover -s tests -v
```

[skillmappe]: https://github.com/vestbytuva-ops/Academic-Skill/tree/main/.agents/skills/academic-skill
[skill-zip]: https://github.com/vestbytuva-ops/Academic-Skill/raw/refs/heads/main/dist/academic-skill.zip
[chatgpt-skills]: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
