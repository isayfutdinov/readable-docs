# Changelog

Versions of the `readable-docs` plugin. The same version is set in `plugins/readable-docs/.claude-plugin/plugin.json` and `plugins/readable-docs/.codex-plugin/plugin.json`.

## 0.2.0

- The skill `polishing-docs-for-reading` is renamed `review-text`; its contents are unchanged. Reinstall the plugin to pick up the new name. A writer skill, `write-text`, is planned for a later version.

## 0.1.0

- New skill `polishing-docs-for-reading`: reviews a document (one file or a set) for how it reads — order of parts, terms, missing facts, actions without an actor, warnings without a consequence — and returns one report in the language of the request with ready replacement text; the document itself is never edited. Role reviewers run as independent agents on a cheaper model; the summary gives a score per role and a verdict.
- Modes `human-pass` (answers to the user's remarks) and `second-opinion` (another model, separate report) ship untested in this version.

## 0.0.1

- Marketplace skeleton for Claude Code and Codex: one plugin, `readable-docs`, with a manifest for each platform. No skills yet.
- License: MIT. Every skill names the license and the author in its frontmatter and carries its own LICENSE.txt.
