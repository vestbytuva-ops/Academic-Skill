# Academic Skill
>[!IMPORTANT]
>**THIS SKILL IS STILL BETA**
We are proud to announce this skill and have the opportunity to publish **Academic-Skill** publicly. Multiple tests have shown consistent results; for instance, both our humanizer and copywriting-style skills delivered great outcomes. We also tested the outputs of this skill using the AI detector GPTZero.


<img width="217" height="89" alt="image" src="https://github.com/user-attachments/assets/1b2c05f2-169c-423c-a1fc-713498d2abf2" />


[Les på norsk](README.nb.md) · [Installation and compatibility](docs/Compatibility.md) · [Validation results](docs/Validation.md)

Academic Skill supports academic work in Norwegian and English. Select `academic-skill` once and describe the task. It can turn a rubric into a plan, revise a draft in your voice, check what a source supports and turn the findings into a timed presentation. It follows the requested language and keeps quotations in their original language.

## Install in Codex

To install this checkout, run `npx skills add . --skill academic-skill -a codex --copy -y` from its root or pass its absolute path from another project. To install the version on GitHub's default branch, use Node.js and npm:

```sh
npx skills add https://github.com/vestbytuva-ops/Academic-Skill --skill academic-skill -a codex --copy -y
```

Add `-g` for a user installation across projects. Open a new Codex chat and select **Academic Skill** with `$academic-skill`. To install a local version before it reaches the default branch, replace the URL with the path to your checkout. For Claude and other clients, see the [platform guide](docs/Compatibility.md).

## What you can ask for

| Task | What the skill can do | Guidance |
| --- | --- | --- |
| Understand an assignment | Turn action verbs and marking criteria into concrete steps. | [Assignment and rubric](skills/academic-skill/references/oppgaveforstaelse.md) · [Norwegian schools](skills/academic-skill/references/norsk-skole.md) |
| Preserve your voice | Identify the choices in your own samples that you want to keep. | [Personal voice](skills/academic-skill/references/personlig-stemme.md) |
| Write an argument | Plan an essay or develop an argument and its counterargument. | [Academic writing](skills/academic-skill/references/skriving.md) · [English conventions](skills/academic-skill/references/english.md) |
| Copyedit | Improve clarity and flow while preserving meaning and uncertainty. | [Copyediting](skills/academic-skill/references/sprakvask.md) |
| Get feedback | Locate the strongest parts and priority revisions against the rubric. | [Critique](skills/academic-skill/references/kritikk.md) |
| Check sources | Compare each claim with a specific passage and distinguish unresolved claims. | [Research integrity](skills/academic-skill/references/kildekontroll.md) |
| Learn a concept | Work through an example and try a task yourself. | [Learning](skills/academic-skill/references/laering-og-eksamen.md) |
| Prepare for an exam | Practise oral questions, flashcards or retrieval from your notes. | [Exam practice](skills/academic-skill/references/laering-og-eksamen.md) |
| Plan a presentation | Arrange evidence into slides, speaking notes and a time budget. | [Presentations](skills/academic-skill/references/presentasjoner.md) |
| Work with Office files | Check a spreadsheet range, organise a report or produce a file when tools allow. | [Office](skills/academic-skill/references/office-filer.md) |
| Check a final draft | Catch changes in quotations, numbers, scope and assignment requirements. | [Final checks](skills/academic-skill/references/sluttkontroll.md) |

> Six of ten students preferred the glossary. Check whether my conclusion about all students follows, then plan a four-minute talk.

## Build and validate

From the repository root, with Python 3.10 or newer:

```sh
python -m pip install -r requirements-dev.txt
python tools/build.py
python -m unittest discover -s tests
python tools/build.py --check
```

The builder uses Python's standard library. The test suite also checks YAML metadata and the plugin JSON schema. With Node.js/npm available, run `python tools/smoke_install.py` to exercise the installer.

For Claude's **Upload a skill**, select `academic-skill.zip`. For **Upload a plugin**, select `academic-skill-claude-plugin.zip`. Both are generated in `dist/`. The source tree is distributed without release ZIPs. [Packaging and release instructions](docs/Release.md)
