# Academic Skill

English | [Norsk bokmål](README.nb.md)

**NOTE!** Academic Skill is a Norwegian skill that also works in English. Ask for the language your assignment requires.

Academic Skill helps students understand assignments, study for exams, evaluate sources and methods, revise drafts, and plan presentations. Share the assignment, the material you want to work with, and what you need help with.

<a id="installer-for-alle-lokale-prosjekter"></a>

## Install for all local Codex projects

Open Codex on the computer where you work and send this request once.

```text
Install the skill from https://github.com/vestbytuva-ops/Academic-Skill/ for all my local Codex projects.
```

You can also invoke `$skill-installer` and give it the [skill folder URL][skill-folder]. To install manually, extract [academic-skill.zip][skill-zip] and place the `academic-skill` folder in `~/.codex/skills/` (`%USERPROFILE%\.codex\skills` on Windows). If you set `CODEX_HOME`, use its `skills` folder. The installed file should be at `skills/academic-skill/SKILL.md`.

After installation, open a new Codex conversation and select `$academic-skill`. To use the skill in this repository alone, open the repository folder as a Codex project.

## Use in ChatGPT Work

Download [academic-skill.zip][skill-zip]. In a workspace that supports skill uploads, go to **Plugins → Skills → Create → Upload from your computer** and select the ZIP. After installation, open a new Work chat, type `@`, and select **Academic Skill**. [OpenAI's skill upload guide][chatgpt-skills]

## Choose a workflow

The website lists eleven areas you can request individually. This repository installs one skill called `academic-skill`. Select it, then name an area and describe what you want it to do.

> Use $academic-skill. Focus on exam-preparation. Quiz me on these notes in English, one question at a time. Wait for my answer before giving feedback.

| Website label | What to ask for |
| --- | --- |
| `academic-core` | Break down the assignment and identify what to clarify before you start. |
| `personal-voice` | Identify wording, rhythm, and tone in your own writing sample and use them as a guide. |
| `academic-writing` | Connect the research question, argument, evidence, and conclusion. |
| `humanizer` | Improve the flow of your text while preserving its meaning and your voice. |
| `academic-critic` | Evaluate a draft against the rubric or your teacher's feedback and suggest a revision. |
| `research-integrity` | Check which claims the supplied sources and methods support. |
| `learning-coach` | Explain a concept, give one exercise, and wait for your attempt. |
| `exam-preparation` | Quiz you from your notes or draft flashcards for a topic. |
| `presentation-engine` | Plan slides and speaking points for the audience and time limit. |
| `office-integration` | Work with excerpts or files from Word, Excel, or PowerPoint using the tools available in your session. |
| `quality-assurance` | Review a draft against the assignment and identify quotations, figures, or claims to verify. |

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
| [Skill instructions](.agents/skills/academic-skill/SKILL.md) | The Norwegian instructions that guide the skill. |
| [References](.agents/skills/academic-skill/references/) | Norwegian guidance on writing, personal voice, teaching, and research. |
| [Documentation](docs/) | The [development plan](docs/Arkitektur-og-plan.md), [source register](docs/Kilderegister.md), and [V2 pilot results](docs/Testresultater.md) in Norwegian. |
| [Tests and writing samples](tests/) | Seven example tasks, their scoring criteria, and automated checks. |

## Evaluate and test

Try one of the [seven example tasks](tests/cases.json) in a fresh conversation and compare the answer with the [scoring criteria](tests/Vurderingsnokkel.md). The examples use fictional writing samples.

The guidance workflows work without Python or Office. The optional [text checker](.agents/skills/academic-skill/scripts/check_spans.py) uses Python 3 to compare how many times selected expressions occur before and after an edit. Review their meaning in context as well.

After committing a change to the skill folder, rebuild the download. Run both commands from the repository root.

```sh
git archive --format=zip --prefix=academic-skill/ --output=dist/academic-skill.zip HEAD:.agents/skills/academic-skill
python -B -m unittest discover -s tests -v
```

[skill-folder]: https://github.com/vestbytuva-ops/Academic-Skill/tree/main/.agents/skills/academic-skill
[skill-zip]: https://github.com/vestbytuva-ops/Academic-Skill/raw/refs/heads/main/dist/academic-skill.zip
[chatgpt-skills]: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
