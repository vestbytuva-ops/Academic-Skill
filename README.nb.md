# Academic Skill

[English](README.md) · [Installasjon for hver agent](docs/Compatibility.md) · [Testresultater](docs/Validation.md)

**MERK! Dette er en norsk skillsamling som også kan brukes på engelsk.** Del oppgaven, vurderingskriteriene, notatene eller et kildeutdrag. Be om veiledning hvis du vil prøve selv, forslag hvis du vil vurdere en endring, eller en ferdig revisjon når det er det du trenger. Svar og leveranser følger språket i oppgaven, og sitater beholder originalspråket.

## Installer i Codex

Kjør kommandoen i prosjektmappen med Node.js og npm installert. Den bruker hovedgrenen. Før den nye versjonen er slått sammen, bruk oppskriften for arbeidsgrenen i [engelsk README](README.md#install-in-codex).

```sh
npx skills add https://github.com/vestbytuva-ops/Academic-Skill --skill "*" -a codex --copy -y
```

Legg til `-g` hvis de tolv valgene skal være tilgjengelige i alle **lokale** prosjekter. Åpne en ny Codex-økt, skriv `$` og velg fra listen. Du kan også åpne `/skills`. Bytt ut `"*"` med navnet på én skill hvis du bare vil installere den.

| Velg | Hva den hjelper deg med |
| --- | --- |
| `academic-skill` | Kombiner flere deler av en oppgave, fra kriterier til innlevering eller muntlig presentasjon. |
| `academic-core` | Tolk oppgaven, avgrens problemstillingen og gjør kravene konkrete. |
| `personal-voice` | Finn trekk i dine egne skriveprøver. Behold, rett eller fjern dem for oppgaven. |
| `academic-writing` | Bygg opp en fagtekst og knytt belegg til argumentene dine. |
| `humanizer` | Språkvask tekst og behold mening, sitater og forbehold. |
| `academic-critic` | Få begrunnet tilbakemelding på bestemte steder i et utkast. |
| `research-integrity` | Kontroller påstander og henvisninger mot kilden, og vurder metoden. |
| `learning-coach` | Lær et begrep gjennom en forklaring og en oppgave du løser selv. |
| `exam-preparation` | Lag øvingskort, planlegg lesingen eller tren muntlig med ett spørsmål om gangen. |
| `presentation-engine` | Lag disposisjon, talepunkter og tidsplan for presentasjonen. |
| `office-integration` | Arbeid med Word, Excel og PowerPoint. Du kan også lime inn et utdrag. |
| `quality-assurance` | Sjekk krav, tall, sitater og kildehenvisninger før innlevering. |

> Vi har fire minutter. Hjelp meg å sjekke hva undersøkelsen viser og lage en disposisjon med talepunkter.

> Sjekk påstanden mot side 3 i kilden jeg legger ved. Vis hvilke ord som går lenger enn belegget.

> Eg øver til munnleg. Bruk notata mine, still eitt spørsmål og vent på svaret.

## I andre agenter

- **ChatGPT Work**. I et arbeidsområde med støtte kan en administrator laste opp [pluginen med alle tolv](dist/academic-skill-plugin.zip). Installer den, skriv `@` og velg ønsket skill i listen.
- **Claude Code**. Skriv `/plugin install academic-skill --marketplace vestbytuva-ops/Academic-Skill`. Velg eksempelvis `/academic-skill:exam-preparation`. Installerer du frittstående med `-a claude-code`, bruker du `/exam-preparation`.
- **Claude.ai**. Åpne **Tilpass → Skills → + Create skill → Upload a skill**. Last opp og aktiver [hovedskillen](dist/academic-skill.zip) for å bruke alle arbeidsmåtene. Vil du ha egne oppføringer, last opp de [enkelte ZIP-filene](dist/individual).
- **Cursor**. Bytt til `-a cursor` i installasjonskommandoen. Velg for eksempel `/exam-preparation`.
- **Gemini CLI**. Bruk `-a gemini-cli`. Åpne et klarert prosjekt, skriv `/skills list` og be om skillen med navn.
- **VS Code med GitHub Copilot**. Bruk `-a github-copilot`. I VS Code-chatten kan du skrive `/exam-preparation`. Andre støttede Copilot-klienter velger ut fra oppgaven.

## Oppdater, fjern eller feilsøk

Kjør `npx skills list -a codex` for prosjektet. Legg til `-g` for brukermappen. Normal sti er `.agents/skills/<navn>/SKILL.md` eller `~/.agents/skills/<navn>/SKILL.md`, også på Windows under brukermappen. Åpne en ny økt hvis menyen viser gamle opplysninger. Velg én installasjonsmåte hvis du ser duplikater.

Bruk `npx skills update` ved installasjon fra GitHub. For én enkelt skill kan du bruke `npx skills remove exam-preparation -a codex -y`. For alle tolv, kopier den navngitte kommandoen i [installasjonsguiden](docs/Compatibility.md). ZIP-filer oppdateres ved å installere den nye pakken på samme sted. I et administrert arbeidsområde avgjør administratoren hvilke skills som er tilgjengelige.

Se [bygging og tester](README.md#build-and-validate), [evaloppgaver](tests/workflows.json), [historiske evalresultater](CHANGELOG.md) og [publiseringsveiledning](docs/Release.md).
