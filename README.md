# Academic Skill

[Les på norsk](README.nb.md) · [Installation and compatibility](docs/Compatibility.md) · [Validation results](docs/Validation.md)

**NOTE! This is a Norwegian skill collection that also works in English.** Use it to unpack a rubric, revise an argument, check a claim against a source you supply, or prepare for an oral exam. The assistant follows the language of the task and keeps quotations in their original language. English assignments use English academic conventions.

Install the collection for twelve selectable skills in supported clients. Choose **academic-skill** for a task with several stages, such as checking a survey result and turning it into a timed presentation. Each specialist also works when installed on its own.

## Install in Codex

Run this in your project folder with Node.js and npm available. It works in Bash, PowerShell and Command Prompt. The public repository command targets the default branch. When testing a pull request before it is merged, use the checkout instructions below.

```sh
npx skills add https://github.com/vestbytuva-ops/Academic-Skill --skill "*" -a codex --copy -y
```

Add `-g` for all your local projects. Open a new Codex session, type `$`, and select a skill, or open `/skills`. For a single specialist, replace `"*"` with `research-integrity`. For the umbrella alone use `academic-skill`. A bare repository URL in a conversation can be passed to an installation tool if that client has one. The install needs to happen in the environment where you use the skills.

All twelve display names start with **Academic**. In a picker that searches display names, type `$academic` or narrow the search, for example to `Academic Research Integrity`. Clients that index command IDs use the names in the table below, such as `$research-integrity`. The umbrella includes all eleven workflows even when installed by itself. Installing all twelve also gives you eleven separate shortcuts.

To test a checked-out branch before release, run the installer from a clean project and pass the path to that checkout.

```sh
npx skills add ../Academic-Skill --skill "*" -a codex --copy -y
```

## Choose a workflow

| Skill | Use it when you want to… |
| --- | --- |
| `academic-skill` | Combine a brief, draft, evidence check and presentation or study session. |
| `academic-core` | Translate the assignment and its rubric into things you can actually deliver. |
| `personal-voice` | Identify choices in your own writing samples and keep or drop them for this task. |
| `academic-writing` | Build an argument, outline a paper, or revise the connection between evidence and thesis. |
| `humanizer` | Copyedit a passage while preserving its meaning, quotations and degree of certainty. |
| `academic-critic` | Find the strongest and weakest parts of a draft against specific criteria. |
| `research-integrity` | Check each claim and citation against the source and assess methodological limits. |
| `learning-coach` | Understand a concept through an example and a short exercise. |
| `exam-preparation` | Practise an oral exam, make flashcards, or take a quiz one question at a time. |
| `presentation-engine` | Turn findings into slides, speaker notes and a plan that fits the time available. |
| `office-integration` | Work with academic Word, Excel or PowerPoint material and check changes against the file. |
| `quality-assurance` | Catch changed numbers, quotations, references and missed requirements before submission. |

> Six of ten participants preferred the glossary. Check whether my conclusion about all students follows, then plan a four-minute talk.

> Revise my paragraph in British English. Keep the quoted sentence, the figures and my uncertainty about the cause.

> Quiz me on these notes. Ask one question and wait for my answer.

## Choose your platform

| Platform | Install | Select a specialist |
| --- | --- | --- |
| Codex CLI / IDE | The command above installs separate entries. The repository also provides a [Codex marketplace](docs/Compatibility.md). | `$research-integrity` or task matching |
| ChatGPT Work | In an eligible workspace an admin uploads the [plugin ZIP](dist/academic-skill-plugin.zip) and enables it for members. | Type `@`, select the installed skill in the picker, then send your material. |
| Claude workspace | Download the [Claude plugin ZIP](https://github.com/vestbytuva-ops/Academic-Skill/raw/refs/heads/main/dist/academic-skill-claude-plugin.zip). In **Plugins → Upload a plugin**, select the ZIP as downloaded. It includes all twelve skills. | Ask to use an included skill by name. |
| Claude Code | `/plugin install academic-skill --marketplace vestbytuva-ops/Academic-Skill` | `/academic-skill:research-integrity` as a plugin, or `/research-integrity` as a standalone skill |
| Claude.ai | **Customize → Skills → + Create skill → Upload a skill**. Enable the [umbrella ZIP](dist/academic-skill.zip), or upload [individual ZIPs](dist/individual) to obtain separate entries. | Ask naturally or name an enabled skill. |
| Cursor | Use the install command with `-a cursor`. | `/research-integrity` or task matching |
| Gemini CLI | Use `-a gemini-cli` and open a trusted project. | Run `/skills list`, then ask to use the skill by name. |
| VS Code / GitHub Copilot | Use `-a github-copilot`. | `/research-integrity` in VS Code chat. In other supported Copilot clients describe the task or name the skill. |

Update the installed collection with `npx skills update` (add `-g` for a global install). For a checkout-based install, pull updates in the checkout and repeat the add command. Remove only this collection with the named removal command in the guide. The guide covers ZIP downloads, other platforms, reinstalls, public distribution status and troubleshooting. [Platform guide](docs/Compatibility.md)

## Build and validate

From the repository root with Python 3.10+ and Node.js 22+:

```sh
python -m pip install -r requirements-dev.txt
python tools/build.py
python tools/build.py --check
python -m unittest discover -s tests
python tools/smoke_install.py
```

The shared texts and optional Python checker are maintained under `skills/academic-skill/`. The builder copies only the resources each specialist needs. Runtime use of the Markdown skills requires no Python packages. File creation and access to external sources depend on the host. [Architecture](docs/Arkitektur-og-plan.md) · [Changelog](CHANGELOG.md) · [Publication and review](docs/Release.md)
