# Readable Docs

Agent skills for documents that read as a coherent story: every term defined before it is used, no forward references, no gaps the reader has to fill in by guessing.

This repository is a plugin marketplace for both **Claude Code** and **Codex**. It holds one plugin, `readable-docs`, and the same skill files serve both platforms.

## Skills

**`write-text`** — writes a text with a reader (a decision paper, spec, runbook, handover, article, post, letter) from your materials and answers only; what is missing becomes a question to you, not a guess.

**`review-text`** — reviews an existing document from the roles of its readers and returns findings with replacement wording; it never edits the document.

Reports and texts come in the language the request names, otherwise in the language of the request.

## Install

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
  LICENSE                                  copy of the root LICENSE, shipped with the installed plugin
  skills/<skill-name>/SKILL.md             one folder per skill, shared by both platforms
LICENSE                                    MIT
CITATION.cff                               how to credit the author ("Cite this repository" on GitHub)
scripts/manifests.py                       check: manifests in step; bump: set the plugin version
scripts/validate.sh                        local and CI validation
```

## Development

Skills are written and evaluated in a separate private repository, because the test corpus contains internal documents. This repository receives one commit per release, with only the files users need. Rules for agents are in [AGENTS.md](AGENTS.md).

`scripts/validate.sh` checks the marketplace; `--smoke` also installs the plugin from a checkout into a throwaway Claude Code home, and into a throwaway Codex home when `CODEX_BIN` names the `codex` binary. CI runs `scripts/validate.sh --smoke` on every push to `main` and on every pull request.

## License

[MIT](LICENSE) © 2026 Ildar Sayfutdinov. You may use, change and share these skills, commercially too. Keep the license and the author's name in every copy. To credit the work, use **Cite this repository** on GitHub or link to https://github.com/isayfutdinov/readable-docs.
