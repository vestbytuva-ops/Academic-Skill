# Academic Skill

[English](README.md) | Norsk bokmål

**NOTE!** Academic Skill er en norsk skill som også kan brukes på engelsk. Be om språket oppgaven krever.

Academic Skill hjelper elever og studenter med å forstå oppgaver, øve til eksamen, vurdere kilder og metode, bearbeide utkast og planlegge presentasjoner. Del oppgaven, materialet du vil jobbe med, og si hva du vil ha hjelp med.

## Installer for alle lokale prosjekter

Åpne Codex på maskinen der du bruker prosjektene dine, og lim inn denne meldingen én gang.

```text
Installer alle 12 skills fra https://github.com/vestbytuva-ops/Academic-Skill/ i standardmappen til Codex. Oppdater eventuelle eksisterende kopier fra dette repoet der de ligger.
```

For manuell installasjon laster du ned [academic-skill-suite.zip][suite-zip] og pakker de 12 mappene direkte ut i `~/.codex/skills/` (`%USERPROFILE%\.codex\skills` på Windows). Har du satt `CODEX_HOME`, bruker du mappen `skills` under den. For eksempel skal eksamensskillen ligge på `skills/exam-preparation/SKILL.md`.

Etter installasjonen åpner du en ny Codex-samtale og skriver `$` for å velge en skill. Vil du installere én skill, kan du gi `$skill-installer` mappelenken fra tabellen nedenfor. Du kan også åpne repoet som et Codex-prosjekt for å bruke alle tolv i dette prosjektet.

## Bruk i ChatGPT Work

Last ned hovedskillen som [academic-skill.zip][skill-zip]. Hvis arbeidsområdet støtter opplasting av skills, velger du **Plugins → Skills → Create → Upload from your computer** og laster opp ZIP-filen. Åpne deretter en ny Work-samtale, skriv `@` og velg **Academic Skill** for å bruke arbeidsområdene under hver for seg eller sammen. [OpenAIs veiledning for opplasting][chatgpt-skills]

## Velg et arbeidsområde

Velg **`$academic-skill`** for å kombinere flere områder i samme bestilling. Hovedskillen kan for eksempel sjekke kildene før den lager en presentasjon og kontrollerer resultatet mot oppgaven.

> Bruk $academic-skill. Sjekk påstandene i utkastet mot disse kildene, og lag så fem lysbilder med funnene som har støtte.

For ett område velger du den egne kommandoen og beskriver oppgaven.

> Bruk $exam-preparation. Still meg ett spørsmål om gangen fra disse notatene. Vent på svaret mitt før du gir tilbakemelding.

| Kommando i Codex | Dette kan du be om |
| --- | --- |
| [`$academic-core`](.agents/skills/academic-core/) | Bryt ned oppgaven og finn ut hva du bør avklare før du begynner. |
| [`$personal-voice`](.agents/skills/personal-voice/) | Finn ordvalg, rytme og tone i en egen skriveprøve og bruk dem som stilgrunnlag. |
| [`$academic-writing`](.agents/skills/academic-writing/) | Knytt problemstilling, argumenter, belegg og konklusjon sammen. |
| [`$humanizer`](.agents/skills/humanizer/) | Forbedre flyten i teksten og bevar meningen og skrivestemmen din. |
| [`$academic-critic`](.agents/skills/academic-critic/) | Vurder et utkast mot kriteriene eller lærerens respons, og foreslå ett sted å revidere. |
| [`$research-integrity`](.agents/skills/research-integrity/) | Sjekk hvilke påstander kildene og metoden støtter. |
| [`$learning-coach`](.agents/skills/learning-coach/) | Forklar et faglig begrep, gi én øvelse og vent på svaret ditt. |
| [`$exam-preparation`](.agents/skills/exam-preparation/) | Still spørsmål fra notatene dine eller lag øvingskort til et tema. |
| [`$presentation-engine`](.agents/skills/presentation-engine/) | Planlegg lysbilder og talepunkter for målgruppen og taletiden. |
| [`$office-integration`](.agents/skills/office-integration/) | Bruk verktøyene i samtalen til å jobbe med utdrag eller filer fra Word, Excel eller PowerPoint. |
| [`$quality-assurance`](.agents/skills/quality-assurance/) | Sjekk utkastet mot oppgaven og pek ut sitater, tall eller påstander som bør kontrolleres. |

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
| [Skillmappene](.agents/skills/) | Hovedskillen og elleve egne skills. |
| [Fagveiledningene](.agents/skills/academic-skill/references/) | Personlig stil, akademisk skriving, norskfaglig veiledning og forskningsmetode. |
| [Dokumentasjon](docs/) | [Utviklingsplan](docs/Arkitektur-og-plan.md), [kilderegister](docs/Kilderegister.md) og [resultater fra V2-piloten](docs/Testresultater.md). |
| [Tester og skriveprøver](tests/) | Sju skriveoppgaver med tilhørende svar og vurderingskriterier, samt automatiske tester. |

## Prøv V2 selv

Prøv én av [de sju oppgavene](tests/cases.json) i en ny samtale og sammenlign svaret med [vurderingsnøkkelen](tests/Vurderingsnokkel.md). Oppgavene bygger på oppdiktede skriveprøver.

Skriveveiledningen kan brukes uten Python eller Office. Den valgfrie [tekstkontrollen](.agents/skills/academic-skill/scripts/sjekk_uttrykk.py) bruker Python 3 til å telle forekomster av uttrykk du velger, for eksempel et sitat med sidetall. Den skriver `BESTÅTT` når antallet er likt og `FEIL` ved avvik eller ugyldig grunnlag. Vurder også betydningen uttrykkene har i sammenhengen.

Når du har lagret en endring i skillmappene i Git, bygger du ZIP-filene på nytt og kjører testene fra prosjektmappen.

```sh
git archive --format=zip --prefix=academic-skill/ --output=dist/academic-skill.zip HEAD:.agents/skills/academic-skill
git archive --format=zip --output=dist/academic-skill-suite.zip HEAD:.agents/skills
python -B -m unittest discover -s tests -v
```

[skill-zip]: https://github.com/vestbytuva-ops/Academic-Skill/raw/refs/heads/main/dist/academic-skill.zip
[suite-zip]: https://github.com/vestbytuva-ops/Academic-Skill/raw/refs/heads/main/dist/academic-skill-suite.zip
[chatgpt-skills]: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
