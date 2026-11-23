# Release 4.0.0

The repository ships one installable directory at [skills/academic-skill](../skills/academic-skill). The [root manifest](../plugin.json) supplies the identity used by the Codex and Claude marketplaces. Markdown references, evaluation prompts and the optional Norwegian text checker live within the skill.

## Build the uploads

From the root of the reviewed checkout:

```sh
python tools/build.py
python -m unittest discover -s tests
python tools/build.py --check
```

The package tests use the dependencies in `requirements-dev.txt`. Both archives are generated under the ignored `dist/` directory.

| Filename | Upload screen | First relevant paths in the ZIP |
| --- | --- | --- |
| `academic-skill.zip` | Claude **Upload a skill** or a compatible single-skill importer | `academic-skill/SKILL.md`, then the skill's `agents/`, `references/`, `scripts/` and `evals/` files |
| `academic-skill-claude-plugin.zip` | Claude **Upload a plugin** | `.claude-plugin/plugin.json` at the archive root and the skill under `skills/academic-skill/` |

Choose the matching ZIP as built. Both contain the academic workflows. Academic Skill 4.0.0 has no separate OpenAI plugin ZIP. For Codex, install the skill or the source marketplace. For ChatGPT Work, use GitHub import in an eligible workspace. Public directory approval and workspace enablement are handled by the host. [Platform instructions](Compatibility.md) · [Claude's upload requirements](https://platform.claude.com/docs/en/manage-claude/plugins-api#upload-requirements)

## Share the files separately from the source

After `--check` succeeds, move the two ZIPs from `dist/` to a sibling directory such as `../Academic-Skill-ferdig/`. This leaves the checkout free of built archives. Running the builder again recreates both ZIPs locally. A GitHub Release can attach the two reviewed files as assets.

Git ignores `dist/` when adding files to the repository. Windows **Compress to ZIP** includes files that remain in the directory you select, even when Git ignores them. For a Git source snapshot, write the archive outside the checkout, for example with `git archive --format=zip --output=../Academic-Skill-source.zip HEAD`. This exports committed files and omits the local build products.

## Review a release

1. Select Academic Skill in the target client and supply “Page 3 says six of ten preferred A. I claim everyone preferred A.” Check that the response identifies the contradiction and the passage it used.
2. Ask for oral practice from a short note and request one question at a time. Check that the student can answer before seeing the solution.
3. Ask for a four-minute presentation based on “9 of 14 felt more confident, no comparison group”. Check that the timings add up and the interpretation stays within the evidence.
4. In a new chat without an explicit selection, try the unrelated C programming and sales-copy cases. Record the actual result and host. [Workflow cases](../tests/workflows.json) · [Validation record](Validation.md)

The project has no declared repository software license. The owner should resolve the licensing choice before a submission that requires one. [Source and attribution register](Kilderegister.md)
