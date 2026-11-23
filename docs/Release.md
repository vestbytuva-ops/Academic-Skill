# Release and directory submission

## Files for release 3.1.0

| File | Audience | What the upload contains |
| --- | --- | --- |
| [academic-skill-plugin.zip](../dist/academic-skill-plugin.zip) | ChatGPT Work workspace administrators and OpenAI plugin reviewers | Root manifest, brand icon and twelve skills |
| [academic-skill.zip](../dist/academic-skill.zip) | Claude.ai and standalone clients | One umbrella skill with all workflows, reference texts, evaluations and the Norwegian text checker |
| [Individual ZIPs](../dist/individual) | People who want a specific specialist | One skill per ZIP, including its resources |
| [Repository sources](../skills) | Codex, Claude Code and other compatible clients | Twelve installable directories, OpenAI/Claude marketplace adapters and one shared source for the academic material |

The release candidate has no recorded public directory approval. Installing from a public Git repository, installing in a specific workspace, submitting to a directory and publishing an approved listing are separate actions. The collection requires no service account, API key or MCP server. Reading an attached document, creating an Office file or searching externally depends on the host and user permissions.

## Listing copy for review

| Field | Value |
| --- | --- |
| Name | Academic Skill |
| Publisher handle | vestbytuva-ops |
| Category | Productivity |
| English subtitle | Study, write and check sources |
| Norwegian subtitle | Studer, skriv og sjekk kilder |

**English description.** Interpret a rubric, revise a paragraph, check a claim against a supplied source, practise for an oral exam or turn findings into a timed presentation. The general skill combines workflows. Eleven specialists can be selected independently. Supports Norwegian and English.

**Norsk beskrivelse.** Tolk vurderingskriterier, forbedre et avsnitt, sjekk en påstand mot en vedlagt kilde eller øv til muntlig eksamen. Hovedskillen kombinerer arbeidsmåtene. Elleve spesialister kan velges hver for seg. Svarer på norsk eller engelsk etter oppgaven.

The upload includes the English listing, example prompts and a square 512-pixel icon. See the [manifest](../plugin.json), [website](https://academic-skill.netlify.app) and [support tracker](https://github.com/vestbytuva-ops/Academic-Skill/issues).

## Reviewer walkthrough

1. Install the plugin in an eligible test workspace. In a new chat, check that the umbrella and the eleven specialists are available. Try one exact selection, one natural request and one unrelated request. Record the host, version, account type and selected skill.
2. Pick Academic Research Integrity. Supply: “Page 3 says six of ten preferred A. I claim every participant preferred A.” The answer should identify the contradiction and cite page 3 of the supplied excerpt.
3. Pick Academic Exam Preparation. Supply: “Notat: Utvalget er deltakerne vi faktisk undersøker. Still ett spørsmål og vent.” Expect one Norwegian question, without the answer.
4. Give the umbrella the observation “9 of 14 felt more confident; no comparison group” and request a four-minute talk. Expect a four-minute plan that limits the conclusion to the participants.
5. Ask for a sales email or a C formatting example in a fresh chat without selecting a skill. Observe whether any academic skills activate. Repeat the other [explicit, implicit and out-of-scope trials](../tests/workflows.json).

## Owner steps for OpenAI

1. Choose the owning organization and project in the developer dashboard. The submitter needs organization ownership or **Apps Management Write**. Complete individual or business developer-identity verification.
2. Under **Plugins**, select **Upload new or existing plugin**. Select the verified identity and upload `dist/academic-skill-plugin.zip`. Confirm the parsed skill list, icon, descriptions and contact information. Resolve any dashboard findings, including any publisher-supplied policy or contact fields. Use the skills-only submission route.
3. Review the directory guidelines and complete the publisher's declarations in the dashboard. Submit for review. The dashboard is authoritative for review results.
4. After approval, choose **Publish** and check from a second account that can access the directory. For a later skill or metadata change, upload the new ZIP and follow the update flow.

[Official submission procedure](https://developers.openai.com/plugins/deploy/submission) · [Package specification and metadata](https://developers.openai.com/plugins/build/plugins)

For private workspace use, an eligible admin may upload the plugin and assign access independently of directory publication. The receiving user must have access and install or enable it there.

## License and Claude directory

No repository software license has been supplied. Claude Code's local plugin validation passes. Its separate directory-submission profile reports `LICENSE_MISSING`. The owner must choose the intended licensing terms before submitting to that directory. A maintained GitHub marketplace can be used independently. For a GitHub Release, merge the completed PR, tag the reviewed revision, attach the built ZIPs and record their checksums.
