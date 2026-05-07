#!/usr/bin/env bash
# scripts/cowork-commit-push.sh
# Run this from your Mac terminal: bash scripts/cowork-commit-push.sh
# Handles the stale .git/index.lock + commits + pushes the brand-bundle migration.

set -euo pipefail

cd "$(dirname "$0")/.."

echo "→ Clearing stale .git/index.lock if present..."
rm -f .git/index.lock

echo "→ git remote -v"
git remote -v

echo "→ git status (current state)"
git status --short | head -30
echo "..."

echo "→ git add -A"
git add -A

echo "→ Final secrets sweep on the staged diff..."
if git diff --cached | grep -nE '(sk_live_|pk_live_|AKIA[A-Z0-9]{16}|ghp_[A-Za-z0-9]{36}|xoxb-|BEGIN (RSA |EC )?PRIVATE KEY)' >/dev/null 2>&1; then
  echo "⚠ ABORT — secret pattern detected in staged diff. Aborting commit."
  echo "Review with: git diff --cached"
  exit 1
fi
echo "  ✓ clean"

echo "→ git commit -F .commit-msg.txt"
git commit -F .commit-msg.txt

echo "→ Last commit:"
git log --oneline -1

echo "→ git push -u origin main"
git push -u origin main

echo ""
echo "✓ Done. Repo is now in sync with origin/main."
echo "  Verify at: https://github.com/kritsotakis/metis-cortex"
