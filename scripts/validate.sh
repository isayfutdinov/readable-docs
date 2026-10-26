#!/usr/bin/env bash
# Validate the marketplace before a commit or a release.
#   scripts/validate.sh           manifest consistency + `claude plugin validate --strict`
#   scripts/validate.sh --smoke   also install every plugin from this checkout into throwaway
#                                 Claude Code and Codex homes; your own configs are not touched.
# Needs python3; `claude` for validation; `codex` for --smoke (CODEX_BIN overrides the binary).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SMOKE=0
[ "${1:-}" = "--smoke" ] && SMOKE=1
CODEX_BIN="${CODEX_BIN:-codex}"

python3 "$ROOT/scripts/manifests.py" check "$ROOT"

if command -v claude >/dev/null; then
  claude plugin validate --strict "$ROOT"
  for plugin in "$ROOT"/plugins/*/; do
    claude plugin validate --strict "$plugin"
  done
elif [ "$SMOKE" = 1 ]; then
  echo "error: claude CLI not found" >&2
  exit 1
else
  echo "warning: claude CLI not found, skipped claude plugin validate" >&2
fi

[ "$SMOKE" = 1 ] || exit 0

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/claude" "$TMP/codex"
MARKETPLACE="$(python3 -c 'import json, sys; print(json.load(open(sys.argv[1]))["name"])' "$ROOT/.claude-plugin/marketplace.json")"
PLUGINS="$(python3 -c 'import json, sys; print(" ".join(p["name"] for p in json.load(open(sys.argv[1]))["plugins"]))' "$ROOT/.claude-plugin/marketplace.json")"

CLAUDE_CONFIG_DIR="$TMP/claude" claude plugin marketplace add "$ROOT"
CODEX_HOME="$TMP/codex" "$CODEX_BIN" plugin marketplace add "$ROOT"
for plugin in $PLUGINS; do
  CLAUDE_CONFIG_DIR="$TMP/claude" claude plugin install "$plugin@$MARKETPLACE"
  CODEX_HOME="$TMP/codex" "$CODEX_BIN" plugin add "$plugin@$MARKETPLACE"
  ls -d "$TMP/codex/plugins/cache/$MARKETPLACE/$plugin"/*/skills >/dev/null \
    || { echo "error: Codex cache has no skills/ for $plugin" >&2; exit 1; }
done
echo "smoke ok: $PLUGINS installed from $MARKETPLACE in Claude Code and Codex"
