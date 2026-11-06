# Changelog

Versions of the `readable-docs` plugin. The same version is set in `plugins/readable-docs/.claude-plugin/plugin.json` and `plugins/readable-docs/.codex-plugin/plugin.json`.

## 0.3.1

- The installed plugin folder `plugins/readable-docs/` now carries the full MIT license text (`LICENSE`, identical to the root one); `scripts/manifests.py` checks that the copy is there and matches.
- README: the install section starts with the commands; the note on GitHub accounts and SSH host aliases is removed.

## 0.3.0

- New skill `write-text`: writes a text with a reader — a decision paper, spec, plan, runbook, task description, handover, article, post, cover letter, client notice — from the materials the user gives and the user's answers, and nothing else. Gaps go to the user in one batch of questions, or stay in the text as open questions with who decides them; the text is planned from the reader's way to the result; every statement gets a line in a sources map; an independent source check and reader check run until no blocking problem remains; a form review by `review-text` runs only on request. Companion files next to the text: `sources-map.md` and `cycle-report.md` (`plan.md` on request). Mode `revise` applies remarks to an existing text under the same rules.
- `review-text`: every finding is marked blocking or wording, and a next round is recommended only after a blocking finding; Intake sets the purpose and the readers and picks the reviewer set; the TL;DR is written only when the opening does not give the main point; a person who acts or decides is named with their role; the rules dropped their old numbering, history and repeated text.
- The license and the author live only in the root `LICENSE`, `CITATION.cff` and the plugin manifests; skill folders no longer carry `LICENSE.txt` or `license` and `metadata.author` in the frontmatter.
- `scripts/validate.sh --smoke` installs into Codex only when `CODEX_BIN` names the `codex` binary; CI sets it.

## 0.2.0

- The skill `polishing-docs-for-reading` is renamed `review-text`; its contents are unchanged. Reinstall the plugin to pick up the new name. A writer skill, `write-text`, is planned for a later version.

## 0.1.0

- New skill `polishing-docs-for-reading`: reviews a document (one file or a set) for how it reads — order of parts, terms, missing facts, actions without an actor, warnings without a consequence — and returns one report in the language of the request with ready replacement text; the document itself is never edited. Role reviewers run as independent agents on a cheaper model; the summary gives a score per role and a verdict.
- Modes `human-pass` (answers to the user's remarks) and `second-opinion` (another model, separate report) ship untested in this version.

## 0.0.1

- Marketplace skeleton for Claude Code and Codex: one plugin, `readable-docs`, with a manifest for each platform. No skills yet.
- License: MIT. Every skill names the license and the author in its frontmatter and carries its own LICENSE.txt.
