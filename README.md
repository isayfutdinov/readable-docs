# Readable Docs

Agent skills for documents that read as a coherent story: every term defined before it is used, no forward references, no gaps the reader has to fill in by guessing.

This repository is a plugin marketplace for both **Claude Code** and **Codex**. It holds one plugin, `readable-docs`, and the same skill files serve both platforms.

## Skills

| Skill | What it does | Status |
|---|---|---|
| `polishing-docs-for-reading` | Reviews an existing document, one file or a set of files. Proposes a reading order with a TL;DR, scores the text from the roles that will read it, gives replacement wording for each issue and growth areas for the document as a whole. Reports only; it never edits the document. | In development |
| `writing-docs-for-reading` | Drafts a document from source material without inventing facts, then reviews the draft with `polishing-docs-for-reading`. | Planned |

Reports come in the language the request names, otherwise in the language of the request.

## Install

The repository is private for now. Installation uses your git credentials (`gh auth login` or an SSH key) and needs read access to `isayfutdinov/readable-docs`.

If your default GitHub credentials belong to another account, add the marketplace by an SSH URL that uses a host alias for the right key, for example `git@github-personal:isayfutdinov/readable-docs.git`, in place of `isayfutdinov/readable-docs` in the commands below.

### Claude Code

In a session:

```
/plugin marketplace add isayfutdinov/readable-docs
/plugin install readable-docs@readable-docs
```

Or from the shell:

```bash
claude plugin marketplace add isayfutdinov/readable-docs
claude plugin install readable-docs@readable-docs
```

Skills show up as `readable-docs:<skill-name>`.

To update, run `/plugin marketplace update readable-docs`, or turn on auto-update for this marketplace under `/plugin` → Marketplaces. Claude Code installs a new copy only when the plugin version changes.

### Codex CLI

```bash
codex plugin marketplace add isayfutdinov/readable-docs
codex plugin add readable-docs@readable-docs
```

Or type `/plugins` in a Codex session and install Readable Docs from the list.

To update, run `codex plugin marketplace upgrade readable-docs`.

### Codex app

Add the marketplace with the CLI command above, restart the app, open **Plugins** and install Readable Docs.

### Remove

```bash
claude plugin marketplace remove readable-docs
```

```bash
codex plugin remove readable-docs@readable-docs
```

```bash
codex plugin marketplace remove readable-docs
```

## Repository layout

```
.claude-plugin/marketplace.json            marketplace for Claude Code
.agents/plugins/marketplace.json           marketplace for Codex
plugins/readable-docs/
  .claude-plugin/plugin.json               plugin manifest for Claude Code
  .codex-plugin/plugin.json                plugin manifest for Codex, with the app interface
  assets/icon.svg                          icon in the Codex app
  skills/<skill-name>/SKILL.md             one folder per skill, shared by both platforms
  skills/<skill-name>/LICENSE.txt          copy of LICENSE, travels with the skill folder
LICENSE                                    MIT
CITATION.cff                               how to credit the author ("Cite this repository" on GitHub)
scripts/manifests.py                       check: manifests in step; bump: set the plugin version
scripts/validate.sh                        local and CI validation
```

## Development

Skills are written and evaluated in a separate private repository, because the test corpus contains internal documents. This repository receives one commit per release, with only the files users need. Rules for agents are in [AGENTS.md](AGENTS.md).

`scripts/validate.sh` checks the marketplace; `--smoke` also installs the plugin from a checkout into throwaway Claude Code and Codex homes. Set `CODEX_BIN` if `codex` is not on your `PATH`. CI runs `scripts/validate.sh --smoke` on every push to `main` and on every pull request.

## License

[MIT](LICENSE) © 2026 Ildar Sayfutdinov. You may use, change and share these skills, commercially too. Keep the license and the author's name in every copy, including a single copied skill folder. To credit the work, use **Cite this repository** on GitHub or link to https://github.com/isayfutdinov/readable-docs.
