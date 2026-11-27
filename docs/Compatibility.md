# Installation and compatibility

[English overview](../README.md) · [Norsk hurtigstart](../README.nb.md) · [Validation results](Validation.md)

The standard installation registers one skill called `academic-skill`. Describe the workflow in your request, for example “Quiz me from these notes” or “Draw a sequence diagram for the submission process”. The skill reads the relevant files from its own directory. Pixel art, draw.io and UML are available through the same command in Codex and Claude Code. [Visual workflow guide](../skills/academic-skill/references/visuelle-arbeidsmater.md)

| Client | Install or enable | Select it |
| --- | --- | --- |
| Codex | Install the directory for your project or user with the command below, or use the repository marketplace. | In a new chat, select `$academic-skill`. |
| ChatGPT Work | In a workspace offering GitHub plugin import, an administrator imports this repository through **Admin → Plugins**, then grants workspace access. Use the directory containing the root `plugin.json` as the plugin source. | Choose Academic Skill from the workspace's enabled plugins or skills. |
| Claude Code | Install the standalone skill with `-a claude-code`, or add the Claude marketplace below. | Use `/academic-skill` for the standalone install or `/academic-skill:academic-skill` for the namespaced plugin command. |
| Claude workspace | Build the release files and choose `academic-skill-claude-plugin.zip` in **Plugins → Upload a plugin**. | Enable the plugin for the intended workspace, then request Academic Skill. |
| Claude individual skill | Open the **Skills** area and choose **Upload a skill** with `academic-skill.zip`. | Enable Academic Skill and ask for the workflow. |
| Cursor | Use the same installer with `-a cursor`. | Choose the skill where offered or name it in an Agent request. |
| Gemini CLI | Use `-a gemini-cli` in a trusted project. | Check `/skills list` and ask to use `academic-skill`. |
| VS Code / GitHub Copilot | Use `-a github-copilot` in a client supporting Agent Skills. | In VS Code chat, choose the skill where offered or describe the task. |
| Other Agent Skills hosts | Install the complete [academic-skill directory](../skills/academic-skill) in the host's documented skill location. | Follow the host's invocation convention. |

File creation, web access, plugin imports and account-level enablement depend on the client. The [validation record](Validation.md) identifies which checks actually ran. [Official GitHub import guide for ChatGPT Work](https://learn.chatgpt.com/docs/enterprise/plugin-management) · [Claude Code skills](https://code.claude.com/docs/en/skills) · [Claude.ai skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Gemini CLI skills](https://geminicli.com/docs/cli/skills/)

## Project or user installation

With Node.js/npm available, run in the target project:

```sh
npx skills add https://github.com/vestbytuva-ops/Academic-Skill --skill academic-skill -a codex --copy -y
npx skills list -a codex
```

For a user installation across projects, add `-g` to both commands. To install a local version, replace the GitHub URL with the path to the checkout. Repeat the same add command to update the installed copy from that checkout. An example from a sibling project is `npx skills add ../Academic-Skill --skill academic-skill -a codex --copy -y`. Adjust the directory name to match the checkout. [Installer command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)

## Marketplace installation

For Codex clients with marketplace support:

```sh
codex plugin marketplace add vestbytuva-ops/Academic-Skill
codex plugin add academic-skill@academic-tools
codex plugin list --marketplace academic-tools --json
```

For Claude Code, use `/plugin marketplace add vestbytuva-ops/Academic-Skill` and then `/plugin install academic-skill@academic-tools`. Choose one installation method per client and scope to avoid duplicate registrations.

## Moving from version 3

Installing version 4 registers the integrated entry. Project- or user-level copies of version 3 installed independently may still appear. Inspect their source, path and scope with the client's skill manager or `npx skills list -a codex` (append `-g` for the user scope).

If you want to retire an old shortcut, first confirm that it came from this repository and save any local edits. For a confirmed version 3 installer copy, for example, use `npx skills remove exam-preparation -a codex` in the same scope. Repeat only for the specific obsolete names you intend to remove. Other skills, including `academic-skill-personlig`, are separate installations. A marketplace installation is updated in that marketplace.

## If the skill or upload is missing

- Check that the host sees `academic-skill/SKILL.md` in its configured skill root. Restart the chat or refresh its skill list after installation.
- In a Claude upload screen, select the archive for that screen directly. The two filenames and archive layouts are listed in the [release guide](Release.md).
- For “Zip cannot contain nested zip files”, remove the selected upload and choose the built Claude plugin ZIP. Windows includes ignored `dist/` files when it compresses a folder. A Git source archive contains only committed source files.
