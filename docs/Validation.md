# Validation of Academic Skill 4.0.0

## Reproduce the package checks

From the repository root, install the test dependencies with `python -m pip install -r requirements-dev.txt`, then run:

```sh
python tools/build.py
python -m unittest discover -s tests
python tools/build.py --check
```

The builder and the Norwegian text checker use the Python standard library. The test suite also uses PyYAML for frontmatter and jsonschema for the published root manifest schema. The package tests build a clean fixture so they also work after the release ZIPs have been moved to a sibling directory. Run the build again before comparing on-disk release files with `--check`.

On Windows, all 25 tests passed (eight package and routing tests and 17 text-checker tests). The build and final archive comparison passed. In two local prompt trials, a four-minute talk used the 9/14 finding without attributing it to the exercise, and an English proposal retained 40 invitations as a plan and 20% as a target. These were agent trials with visible criteria.

| Check | What it establishes |
| --- | --- |
| Single entry and routing | The catalog, directory, manifest identities and Codex label identify `academic-skill`. The description fits the 200-character upload limit. Every linked local resource exists in the installed skill. |
| Source and release boundaries | The source tree outside the build directory contains zero ZIP or skill archives. In Git the test also checks the index, including tracked files under ignored paths. |
| Upload contents | Both uploads contain exactly the expected source bytes. The skill archive has `academic-skill/SKILL.md`. The plugin has `.claude-plugin/plugin.json` at the root and `skills/academic-skill/SKILL.md`. Entries are checked for nested archives by filename and payload. |
| Reproducibility | A second build in a clean directory produces the same bytes. A missing reference, stale archive or unexpected package fails validation. |
| Text checker | The 17 original CLI tests exercise quotations, references, Norwegian and English text, decimal commas, repeated measurements and exit codes. |

## Installation trials on Windows

The pinned skills installer (1.9.0) installed one skill from the local source in a disposable project and one in an isolated user installation. The reference files and text checker were present in both. To repeat with Node.js, npm and Git, run `python tools/smoke_install.py`.

The native Codex app server found exactly one enabled Academic Skill with the expected display name in a project using `.agents/skills/` and in an unrelated project using an isolated `CODEX_HOME/skills/`. Both returned zero discovery errors. Run `python tools/verify_codex.py PATH` to inspect project scope or add `--scope user` for user scope.

## Academic behavior and remaining host checks

The [workflow cases](../tests/workflows.json) retain the original 12 explicit requests, eight selection prompts and the missing-source case. The [12 evaluations](../skills/academic-skill/evals/evals.json) retain their prompts and assessment criteria. The expected academic selections identify the single skill and the references it should consult. The unrelated requests keep their exclusion criteria. Automated tests verify the fixtures and their routes. To assess answer quality, run a prompt in a fresh chat with its supplied material and grade the actual response against its expectations.

A signed-in Claude workspace upload and any organization-specific review must be verified in the target account. Previous cross-client behavior and platform versions are recorded in the [3.1 validation record](https://github.com/vestbytuva-ops/Academic-Skill/blob/8c664eff4bfe1839683e50ffe03edf0f403d7d1b/docs/Validation.md).
