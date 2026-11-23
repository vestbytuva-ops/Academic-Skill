# Validation of the twelve-skill collection

## Version 3.1 (23 November 2026)

The 3.0 catalog had eight display names containing `Academic`. In 3.1 all twelve contain the search term. The eleven specialist commands keep their original IDs. On Windows, the Codex app server returned all twelve as enabled, with the expected display names and scope, first in an isolated project and then from a user installation of the plugin ZIP in an unrelated project. The graphical suggestion list was not observed.

The Windows Python suite passed 26 tests. The package checks cover all eleven routes available from an umbrella-only install and reject stale display names and incorrect discovery scope. The generated files and all thirteen distribution archives passed the reproducible build check.

Two additional umbrella-only trials used supplied material. In Norwegian, the reviewer counted the preprint and final article as one study, retained their different figures and page references, and left the result from a separate abstract unresolved. In English, it preserved a proposed 20% change as a target and asked for the baseline and the meaning of the percentage. These cases and their expected outcomes are in the [workflow suite](../tests/workflows.json). The earlier platform observations below apply to version 3.0.

## Diagnosis

Revision `64c2442` shipped a single valid skill in `.claude/skills/academic-skill/`. Its UTF-8 frontmatter parsed and its name matched the directory. Its tests explicitly required one ZIP, no skill metadata under `agents/` and no independent skills. The previously published eleven topic names were absent as installed packages. The subsequent merge `e7942bd` removed the Claude source directory and retained the old ZIP. The restored sources here retain the last complete academic content and the text checker.

TasteDesign was inspected at `f6b7657` as a packaging reference. Its checkout placed the skill under `skills/` and offered marketplace adapters. This collection uses its own academic instructions and the portable root manifest supported by the current OpenAI specification.

## Executed checks

| Check | Observation |
| --- | --- |
| Agent Skills reference validator | Passed for all 12 directories. Each name matches its directory and each description fits the Claude.ai upload limit used here. |
| Manifest | Validated the root manifest against the vendored official Agent Plugins 1.0.0 JSON Schema. Additional checks cover OpenAI display fields, marketplace paths and both 512 × 512 PNG icon references. |
| Release files | All 13 ZIPs matched their source files byte for byte after a fresh build. Generated metadata and standalone copies matched their canonical sources. A missing-reference regression produces an error with the missing path. |
| Python suite | 24 tests passed: 17 text-checker tests and seven distribution and documentation tests. They cover Norwegian letters, decimal commas, protected spans and exit codes. Run from the repository root with `python -m unittest discover -s tests`. |
| Installer 1.9.0, Linux | In three clean project folders, the full install exposed 12 entries, the single research specialist exposed one, and the umbrella alone exposed one. A user install wrote the twelve directories to `~/.agents/skills/`. |
| Codex CLI 0.172.0-alpha.2 | `skills/list` returned all 12 enabled with scope `repo`, and 12 enabled with scope `user`. In an empty project it still returned the 12 user entries. No discovery errors. Local `codex plugin marketplace add`, `codex plugin add` and `codex plugin list` reported Academic Skill 3.0.0 installed and enabled. |
| Claude Code 2.1.330 | The official CLI validated the local marketplace and enumerated all 12 namespaced commands. Separate optional directory validation reports a missing license. |
| Gemini CLI 0.70.0 | Native `gemini skills list --all` enumerated 12 enabled skills in the trusted test project. The initial untrusted project omitted workspace skills. |
| Cursor and GitHub Copilot | The real installer wrote project files for the corresponding agent flags. No editor interaction or model run was observed in those clients. |

The Codex CLI's first attempt to start a full chat turn in the managed Linux environment failed when its filesystem helper could not open a network-namespace socket. The discovery results above come from the actual app server. They do not establish that a graphical picker rendered or that an authenticated Codex model answered. Claude.ai upload and a separate ChatGPT Work account were also outside the runtime tests.

After installation, run `python tools/verify_codex.py /path/to/project` for the project scope, or append `--scope user` for the personal installation. This uses the local app-server and prints only the result for the known academic skill names.

## Academic behavior

Independent agent trials used the instructions and supplied academic material. The table records the observed behaviors. These trials exercise the instructions separately from vendor-specific menus or cloud-account entitlements. [Reusable prompts and expectations](../tests/workflows.json) · [Original ten umbrella evals](../skills/academic-skill/evals/evals.json)

| Skill | What the trial demonstrated |
| --- | --- |
| academic-skill | Combined an evidence-limited conclusion with a spoken opening. |
| academic-core | Broke a comparative assignment into criteria covering both sources and gave the student a first step. |
| personal-voice | Separated teacher wording from the student's samples and withdrew a preference on request. |
| academic-writing | Built an English paragraph with the 6/10 result and a counterargument about omitted technical terms. |
| humanizer | Preserved nynorsk, figures, the direct quote and uncertainty during copyediting. |
| academic-critic | Quoted the words about waiting and proposed an edit addressing the criterion. |
| research-integrity | Identified a supported, a contradicted and an unresolved English claim against the supplied source on page 3. |
| learning-coach | Explained a concept, showed a worked example and left the exercise for the learner. |
| exam-preparation | Asked a single relevant question and withheld the answer. |
| presentation-engine | Allocated four minutes and limited the interpretation of the 9/14 result. |
| office-integration | Kept an empty cell distinct from zero and calculated 2.5 for the two observations. The input was a pasted range. |
| quality-assurance | Flagged 2,9 → 29 and the lost hedge. Left the contents of the missing table unresolved. |

In a separate selection trial with descriptions and no preselected skill, the reviewer chose academic-critic, research-integrity and exam-preparation for three targeted prompts. It chose no academic skill for a C question, a commercial email and small talk. These six observations do not estimate a platform-wide trigger rate. The earlier controlled with/without umbrella evaluations and their shortcomings are recorded in the [changelog](../CHANGELOG.md).

## Repeat on a target host

1. Install using the [platform instructions](Compatibility.md). Record version, scope and whether the workspace or project is trusted. Compare the 12 names against the [catalog](../tools/catalog.json).
2. In a fresh chat, explicitly select a specialist. Record the exact choice and test its row from the prompt suite. Repeat with just that specialist installed.
3. Begin a separate chat without selecting a skill. Run each selection test and record the actual choice, including false positives. Try both Norwegian and English and the nynorsk case.
4. Omit the cited source or an attachment. Check that the agent identifies the missing material, limits its claim, and does not invent findings. With Python unavailable, check the manual comparison is disclosed.
5. Repeat on a second account where permitted. Record actual Office files opened or exported separately from pasted-excerpt trials. GitHub Actions runs the packaging and installer smoke tests on Linux, macOS and Windows; the live checks on the PR show each runner's result.
