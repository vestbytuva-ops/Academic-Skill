# Academic Skill

[Norsk](#norsk) · [English](#english)

## Norsk

Én Claude-skill for elever og studenter som vil forstå en oppgave, skrive og revidere, kontrollere kilder, øve til eksamen eller planlegge en presentasjon. Bokmål er utgangspunktet for veiledningen. Svar og leveranser følger språket og sjangeren oppgaven krever.

### Installer i Claude.ai

1. Last ned [academic-skill.zip](dist/academic-skill.zip).
2. Sjekk at **Innstillinger → Funksjoner** tillater kodekjøring og filoppretting. I det oppdaterte grensesnittet heter innstillingen **Create and edit files**.
3. Åpne **Tilpass → Skills** (**Customize → Skills**), velg **+ Create skill → Upload a skill**, og velg ZIP-filen. Aktiver `academic-skill` i lista. [Veiledning for Skills i Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

### Installer i Claude Code

Pakk ut ZIP-filen i `~/.claude/skills/`, slik at `~/.claude/skills/academic-skill/SKILL.md` finnes. Åpne en økt, beskriv oppgaven eller velg `/academic-skill`. Åpner du dette repoet direkte som prosjekt, ligger skillen allerede i `.claude/skills/academic-skill/`. [Veiledning for Skills i Claude Code](https://code.claude.com/docs/en/skills)

### Prøv med din oppgave

Del oppgaveteksten og materialet som trengs. Be om veiledning hvis du vil prøve selv, forslag hvis du vil vurdere et grep eller produksjon hvis du vil ha et utkast, en revisjon eller en presentasjon. Du kan kombinere arbeidsmåtene.

> Bryt ned vurderingskriteriene, og gi meg ett grep jeg kan prøve i mitt eget avsnitt.

> Sjekk påstandene mine mot kildeutdraget, og lag en disposisjon for en presentasjon på fire minutter.

> Quiz meg på disse notatene, ett spørsmål om gangen. Vent på svaret mitt.

Del en kort skriveprøve du har rett til å bruke hvis du vil bevare trekk fra egen stil. Du kan se, rette eller legge bort stilobservasjonene i samtalen. Den valgfrie [tekstkontrollen](.claude/skills/academic-skill/references/sluttkontroll.md) bruker Python 3 og skriver `BESTÅTT` ved like antall eller `FEIL` ved avvik eller ugyldig grunnlag. Veiledningen har en manuell reserve.

### Bygg og test

Etter at endringer i skillmappen er lagt inn i en commit, bygg ZIP-filen på nytt og kjør testene fra repoets rot.

```sh
git archive --format=zip --output=dist/academic-skill.zip HEAD:.claude/skills
python -m unittest discover -s tests
```

Se [evalpromptene](.claude/skills/academic-skill/evals/evals.json) og [endringsloggen](CHANGELOG.md) for forventninger og observerte resultater.

## English

Academic Skill is a single Claude skill for school and university assignments, academic writing and copyediting, source checks, exam practice, presentations, and academic material in Word, Excel, and PowerPoint. Its core instructions are written in Norwegian, and it follows English academic conventions when the task calls for English.

### Install in Claude.ai

1. Download [academic-skill.zip](dist/academic-skill.zip).
2. In **Settings → Capabilities**, enable code execution and file creation. The updated settings layout calls this **Create and edit files**.
3. Open **Customize → Skills**, choose **+ Create skill → Upload a skill**, and select the ZIP. Enable `academic-skill` in the list. [Claude's guide to Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

### Install in Claude Code

Extract the ZIP into `~/.claude/skills/`. Check that `~/.claude/skills/academic-skill/SKILL.md` exists. Start a session and describe your task, or use `/academic-skill`. If you open this repository as a project, the skill is already in `.claude/skills/academic-skill/`. [Claude Code's guide to Skills](https://code.claude.com/docs/en/skills)

### Try it with your own material

Share the assignment, rubric, and material the task depends on. Ask for coaching, feedback on specific choices, or a draft or revision.

> Turn this rubric into a paragraph plan for my essay draft. Help me narrow the thesis statement and give me one step I can try myself.

> Check my citations against the excerpts I supplied, then outline a four-minute presentation using the supported findings.

> Revise my paragraph in British English. Keep my own voice, the direct quote, and the limit on what the evidence can show.

The optional [text checker](.claude/skills/academic-skill/references/sluttkontroll.md) uses Python 3. It prints `BESTÅTT` for equal counts and `FEIL` for a difference or invalid input. The skill can compare the wording by hand when Python or code execution is unavailable.

See [build and test](#bygg-og-test), the [evaluation prompts](.claude/skills/academic-skill/evals/evals.json), and the [changelog](CHANGELOG.md).
