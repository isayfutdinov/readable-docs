# AGENTS.md

Instructions for coding agents (Codex, Claude Code) that work in this repository.

## What this repository is

A plugin marketplace for Claude Code and Codex with one plugin, `readable-docs`. Each platform reads its own files:

| | Claude Code | Codex |
|---|---|---|
| Marketplace | `.claude-plugin/marketplace.json` | `.agents/plugins/marketplace.json` |
| Plugin manifest | `plugins/<plugin>/.claude-plugin/plugin.json` | `plugins/<plugin>/.codex-plugin/plugin.json` |
| Skills | `plugins/<plugin>/skills/<skill>/SKILL.md` | the same files |

## Rules

1. **Keep both platforms in step.** List every plugin in both marketplace files with the same name and the same `./plugins/<plugin>` path. Keep `name`, `version`, `description` and `author` the same in both plugin manifests. `scripts/manifests.py check` enforces this.
2. **One place for the version.** `version` lives only in the two `plugin.json` files, never in marketplace entries. Change it with `python3 scripts/manifests.py bump <plugin> <version>`.
3. **Every change users should get is a release.** Claude Code installs a new copy only when the version changes. Bump the patch version for wording fixes and the minor version for a new skill or changed behaviour, and add a `## <version>` section to `CHANGELOG.md` in the same commit.
4. **Skill format.** One folder per skill, `plugins/<plugin>/skills/<skill-name>/SKILL.md`, folder name equal to `name`. The frontmatter holds exactly these keys:

   ```yaml
   ---
   name: review-text
   description: Use when …
   license: MIT
   metadata:
     author: Ildar Sayfutdinov
   ---
   ```

   `name` is kebab-case, at most 64 characters. `description` has at most 1024 characters, is written in the third person, starts with "Use when…" and lists trigger conditions, not the process. `license` and `metadata.author` match the plugin manifests. Copy `LICENSE` into the skill folder as `LICENSE.txt`: people often copy one skill folder, and the license and the author must travel with it. Supporting files go to `references/` and `assets/` next to `SKILL.md` and are linked by relative path. Codex app metadata for a skill, if needed, goes to `agents/openai.yaml`.
5. **Platform-neutral text.** A skill must run unchanged in Claude Code and Codex. Do not name one platform's tools (Task tool, Agent tool, `subagent_type`, slash commands); describe the action instead, for example "an independent reviewer with a clean context". Write skill files in English; the skill itself answers in the language the request names, otherwise in the language of the request.
6. **Releases only.** The public repository receives one commit per release, published from a private development repository. An installed half-written skill fires on real requests, so publish a skill only when it is finished.
7. **No internal material.** No test corpora, eval runs, company documents, internal links or personal data. Evals live in the private development repository.
8. **Validate before committing.** Run `scripts/validate.sh`; after a change to any manifest also run `scripts/validate.sh --smoke`.
9. **License and credit.** The repository is MIT, copyright Ildar Sayfutdinov. Do not change the license or the copyright line. Keep the author in `CITATION.cff`, in both plugin manifests and in every skill's frontmatter.
