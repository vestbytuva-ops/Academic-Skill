# Installation, invocation and compatibility

[English overview](../README.md) · [Norsk hurtigstart](../README.nb.md) · [What was actually tested](Validation.md)

A `SKILL.md` declares a workflow. Install it in the user or project directory read by the client, or install the collection as a plugin. Explicit selection and automatic matching happen in that client. Workspace enablement and public directory review are separate steps.

| Host | Installation and discovery | Explicit request | Automatic selection | Evidence for 3.0.0 |
| --- | --- | --- | --- | --- |
| Codex CLI / IDE | Project `.agents/skills/`; personal `~/.agents/skills/`; or the repository marketplace | Type `$` and choose a skill. `/skills` lists available skills. | Matches the descriptions | Linux CLI enumerated 12 project and 12 user entries as enabled. Local marketplace plugin installed. Graphical IDE menu unverified. |
| ChatGPT Work | Admin console → Plugins → Add → Upload plugin in an eligible workspace. Assign access, then install or enable in the receiving account. | Type `@` and choose an installed skill from the picker. | Available skills may be selected for relevant work. | Package schema and assets validated. Workspace upload, picker on a second account and public listing unverified. |
| Claude Code | `-a claude-code` installs to `.claude/skills/`; personal `~/.claude/skills/` or install as a plugin. | Standalone `/exam-preparation`; plugin `/academic-skill:exam-preparation`. | Description matching | Official Claude CLI recognized 12 namespaced commands. No authenticated Claude model turn. |
| Claude.ai | Upload one single-skill ZIP in Customize → Skills. Enable file creation in Settings → Capabilities if required. | Name an enabled skill or choose it where offered. | Relevant enabled skills can be selected automatically. | All 12 single-skill ZIPs checked. Upload and routing in Claude.ai unverified. |
| Cursor | `-a cursor`; project `.agents/skills/` or `.cursor/skills/`; personal `~/.cursor/skills/`. | Type `/` then the name. | Relevant skills are available to Agent. | Real installer wrote project files. Desktop UI unverified. |
| Gemini CLI | `-a gemini-cli`; uses trusted workspace `.agents/skills/` or `.gemini/skills/`. The native CLI also provides `gemini skills install`. | `/skills list` inside a session or `gemini skills list --all` in the shell. Ask for the skill by name. | Agent requests activation; approve when prompted. | Native CLI listed all twelve enabled in a trusted workspace. An untrusted workspace omitted them. |
| VS Code with Copilot | `-a github-copilot`; shared project `.agents/skills/` or native `.github/skills/`. Personal skills can live in `~/.copilot/skills/`. | Use `/exam-preparation` in VS Code chat. | Matches descriptions. | Project installation checked. Editor UI unverified. |
| Other GitHub Copilot clients | A supported client can load the project's `.github/skills/`, `.agents/skills/` or `.claude/skills/`. | Name the skill in the task. Shortcuts depend on the client. | Matches supported agent tasks. | Documented support; no cloud-agent session tested. |
| Other Agent Skills hosts | Import one complete directory under `skills/` or its matching single-skill ZIP using the host guide. | Host-specific | Host-specific | Open Agent Skills reference validator passed all twelve. |

## Command-line installation

With Node.js/npm installed, run the following in the target project. Substitute `codex`, `claude-code`, `cursor`, `gemini-cli` or `github-copilot` after `-a`. Keep the quotes around the asterisk on every operating system. Use `-g` for a personal installation. Cross-platform CI is configured for Windows, macOS and Linux.

```sh
npx skills add https://github.com/vestbytuva-ops/Academic-Skill --skill "*" -a codex --copy -y
npx skills list -a codex
```

Choose `--skill personal-voice` for one specialist or `--skill academic-skill` for the umbrella. The plain `npx skills add https://github.com/vestbytuva-ops/Academic-Skill` opens the installer's selection flow where interactive prompts are supported. Pasting a GitHub URL into another user's chat does not itself install a plugin in that account.

## Marketplace installation

For Codex clients with plugin support, run these in a shell. Use either the marketplace installation or standalone skills in the same scope to avoid duplicate entries.

```sh
codex plugin marketplace add vestbytuva-ops/Academic-Skill
codex plugin add academic-skill@academic-tools
codex plugin list --marketplace academic-tools --json
```

For Claude Code, enter `/plugin install academic-skill --marketplace vestbytuva-ops/Academic-Skill` on version 2.1.275 or later. The two-step form is `/plugin marketplace add vestbytuva-ops/Academic-Skill` followed by `/plugin install academic-skill@academic-tools`. Use the plugin manager to update or uninstall it.

For ChatGPT Work, upload [academic-skill-plugin.zip](../dist/academic-skill-plugin.zip). It has a root `plugin.json` and twelve directories under `skills/`.

In Claude's **Plugins → Upload a plugin**, choose [academic-skill-claude-plugin.zip](../dist/academic-skill-claude-plugin.zip). It contains one Claude manifest and the twelve skill directories. If the screen says “Zip cannot contain nested zip files”, remove the selected file and choose this ZIP directly. GitHub's **Code → Download ZIP** contains the entire project, including the ZIPs in `dist/`. [Anthropic's upload requirements](https://platform.claude.com/docs/en/manage-claude/plugins-api#upload-requirements)

For the individual **Upload a skill** workflow, use [academic-skill.zip](../dist/academic-skill.zip) or a [specialist ZIP](../dist/individual). Each contains a single top-level skill directory. The umbrella can perform every workflow on its own.

## Update or remove

For a GitHub-backed install, use `npx skills update` in the project, or `npx skills update -g` for user skills. For a local checkout, pull the new files and repeat your add command. For the Codex marketplace, run `codex plugin marketplace upgrade academic-tools`, then check the installed version and reinstall the plugin if needed. To remove it use `codex plugin remove academic-skill@academic-tools`, then `codex plugin marketplace remove academic-tools` if that catalog is no longer needed.

To remove just this collection while keeping unrelated skills, use its twelve names. Add `-g` if you installed globally and substitute the same agent flag you installed with.

```sh
npx skills remove academic-skill academic-core personal-voice academic-writing humanizer academic-critic research-integrity learning-coach exam-preparation presentation-engine office-integration quality-assurance -a codex -y
```

For ZIP uploads, disable or delete the previous copy via the host's Skills or Plugins settings and upload the new version. A workspace administrator controls distribution of updates to members.

## If the skill is missing

The 3.0.0 catalogue had eight labels containing “Academic”. The four labels for personal voice, research integrity, learning and exams now share that prefix. Update or reinstall the collection in the scope you use. In clients that filter by command ID, try `personal-voice`, `research-integrity`, `learning-coach` or `exam-preparation`. A short suggestion list can also require a narrower query. Opening the umbrella makes these workflows available inside the conversation. Only installing the individual entries or collection registers separate menu items.

1. Check which application, machine, working directory and account you are using. Install in that environment. Check project and global entries separately with `npx skills list -a codex` and `npx skills list -a codex -g`.
2. Look for `<skill-id>/SKILL.md` in the relevant root. An extra enclosing ZIP directory, incorrect filename or installing only the umbrella prevents independent entries. Check the actual spelling, UTF-8 and YAML if you edited a skill.
3. Open a new session. In Gemini, trust your own project first. In Work, check workspace enablement and use the `@` picker. A matching GitHub link in autocomplete indicates a link suggestion.
4. Check duplicate project, personal and plugin installations by path. Keep your edits before removing an older copy. Note the client version (`codex --version` or equivalent), OS, scope and paths if reporting a failure.

[Open Agent Skills specification](https://agentskills.io/specification) · [Codex and ChatGPT skills](https://developers.openai.com/codex/skills) · [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins) · [Claude Code](https://code.claude.com/docs/en/skills) · [Claude.ai](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Cursor](https://cursor.com/docs/skills) · [Gemini CLI](https://geminicli.com/docs/cli/skills/) · [VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills) · [GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) · [skills installer](https://github.com/vercel-labs/skills)
