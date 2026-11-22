# Academic Skill

English | [Norsk bokmål](README.nb.md)

**NOTE!** Academic Skill is a Norwegian skill that also works in English. Ask for the language your assignment requires.

Academic Skill helps students understand assignments, study for exams, evaluate sources and methods, revise drafts, and plan presentations. Share the assignment, the material you want to work with, and what you need help with.

<a id="installer-for-alle-lokale-prosjekter"></a>

## Install for all local Codex projects

Open Codex on the computer where you work and send this request once.

```text
Install all 12 skills from https://github.com/vestbytuva-ops/Academic-Skill/ into Codex's default skills folder. Update any existing copies from this repo in place.
```

For manual installation, download [academic-skill-suite.zip][suite-zip] and extract its 12 folders directly into `~/.codex/skills/` (`%USERPROFILE%\.codex\skills` on Windows). If you set `CODEX_HOME`, use its `skills` folder. For example, the exam skill should be at `skills/exam-preparation/SKILL.md`.

After installation, open a new Codex conversation and type `$` to choose a skill. For a single skill, you can give `$skill-installer` its folder link from the table below. Opening this repository as a Codex project also makes all 12 choices available in that project.

## Use in ChatGPT Work

Download the main skill as [academic-skill.zip][skill-zip]. In a workspace that supports skill uploads, go to **Plugins → Skills → Create → Upload from your computer** and select the ZIP. After installation, open a new Work chat, type `@`, and select **Academic Skill** to use any combination of the workflows below. [OpenAI's skill upload guide][chatgpt-skills]

## Choose a workflow

Choose **`$academic-skill`** to combine several areas in a single request. The main skill can use the workflow outputs together, for example by checking the evidence before drafting slides and reviewing the result against the assignment.

> Use $academic-skill. Check the claims in my draft against these sources, then turn the supported findings into a five-slide presentation in English.

For one area, select its own command and describe the task.

> Use $exam-preparation. Quiz me on these notes in English, one question at a time. Wait for my answer before giving feedback.

| Codex command | What to ask for |
| --- | --- |
| [`$academic-core`](.agents/skills/academic-core/) | Break down the assignment and identify what to clarify before you start. |
| [`$personal-voice`](.agents/skills/personal-voice/) | Identify wording, rhythm, and tone in your own writing sample and use them as a guide. |
| [`$academic-writing`](.agents/skills/academic-writing/) | Connect the research question, argument, evidence, and conclusion. |
| [`$humanizer`](.agents/skills/humanizer/) | Improve the flow of your text while preserving its meaning and your voice. |
| [`$academic-critic`](.agents/skills/academic-critic/) | Evaluate a draft against the rubric or your teacher's feedback and suggest a revision. |
| [`$research-integrity`](.agents/skills/research-integrity/) | Check which claims the supplied sources and methods support. |
| [`$learning-coach`](.agents/skills/learning-coach/) | Explain a concept, give one exercise, and wait for your attempt. |
| [`$exam-preparation`](.agents/skills/exam-preparation/) | Quiz you from your notes or draft flashcards for a topic. |
| [`$presentation-engine`](.agents/skills/presentation-engine/) | Plan slides and speaking points for the audience and time limit. |
| [`$office-integration`](.agents/skills/office-integration/) | Work with excerpts or files from Word, Excel, or PowerPoint using the tools available in your session. |
| [`$quality-assurance`](.agents/skills/quality-assurance/) | Review a draft against the assignment and identify quotations, figures, or claims to verify. |

## Choose how to work

| When you want to … | Ask for | What you get |
| --- | --- | --- |
| practice or keep writing yourself | **Coaching** | One concrete step to try, based on your draft or feedback. |
| evaluate a wording choice | **Suggestions** | An alternative and an explanation of what it changes. |
| draft, revise, or copyedit | **A draft, revision, or copyedit** | Text in the requested language and genre. You can ask to see the changes. |

For style feedback, share a short sample of your own writing and say which features to preserve. The style profile applies to the current task. For source checks, share the claims and evidence. You can also ask for external sources, help choosing a method, or analysis of data you supply.

## Project files

| File or folder | Contents |
| --- | --- |
| [START-HERE.md](START-HERE.md) | A first example and tips for working with your own writing style. |
| [Skill folders](.agents/skills/) | The main skill and eleven standalone skills. |
| [References](.agents/skills/academic-skill/references/) | Norwegian guidance on writing, personal voice, teaching, and research. |
| [Documentation](docs/) | The [development plan](docs/Arkitektur-og-plan.md), [source register](docs/Kilderegister.md), and [V2 pilot results](docs/Testresultater.md) in Norwegian. |
| [Tests and writing samples](tests/) | Seven example tasks, their scoring criteria, and automated checks. |

## Evaluate and test

Try one of the [seven example tasks](tests/cases.json) in a fresh conversation and compare the answer with the [scoring criteria](tests/Vurderingsnokkel.md). The examples use fictional writing samples.

The guidance workflows work without Python or Office. The optional [text checker](.agents/skills/academic-skill/scripts/check_spans.py) uses Python 3 to compare how many times selected expressions occur before and after an edit. Review their meaning in context as well.

After committing changes to the skill folders, rebuild the downloads and run the tests from the repository root.

```sh
git archive --format=zip --prefix=academic-skill/ --output=dist/academic-skill.zip HEAD:.agents/skills/academic-skill
git archive --format=zip --output=dist/academic-skill-suite.zip HEAD:.agents/skills
python -B -m unittest discover -s tests -v
```

[skill-zip]: https://github.com/vestbytuva-ops/Academic-Skill/raw/refs/heads/main/dist/academic-skill.zip
[suite-zip]: https://github.com/vestbytuva-ops/Academic-Skill/raw/refs/heads/main/dist/academic-skill-suite.zip
[chatgpt-skills]: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
