#!/usr/bin/env bash
# scripts/cowork-verify-push.sh
# Runs the three verification checks after the GitHub Desktop push.
# All three must pass to declare Task 2 complete.

set -uo pipefail

cd "$(dirname "$0")/.."

EXPECTED_SHA="7343bef"
PASS=0
FAIL=0

echo "===================="
echo "Verification suite — commit $EXPECTED_SHA"
echo "===================="

echo ""
echo "→ 1. Local HEAD"
LOCAL_SHA=$(git log --pretty=format:%h -1)
echo "   Local HEAD: $LOCAL_SHA"
if [ "${LOCAL_SHA:0:7}" = "$EXPECTED_SHA" ]; then
  echo "   ✓ matches expected $EXPECTED_SHA"
  PASS=$((PASS+1))
else
  echo "   ✗ mismatch (expected $EXPECTED_SHA, got $LOCAL_SHA)"
  FAIL=$((FAIL+1))
fi

echo ""
echo "→ 2. Remote origin/main SHA via git ls-remote"
REMOTE_LINE=$(git ls-remote origin main 2>&1 | head -1)
REMOTE_SHA=$(echo "$REMOTE_LINE" | awk '{print $1}' | cut -c1-7)
echo "   Remote origin/main: $REMOTE_SHA"
if [ "$REMOTE_SHA" = "$EXPECTED_SHA" ]; then
  echo "   ✓ matches expected $EXPECTED_SHA"
  PASS=$((PASS+1))
else
  echo "   ✗ mismatch or empty (expected $EXPECTED_SHA, got '$REMOTE_SHA')"
  echo "   raw: $REMOTE_LINE"
  FAIL=$((FAIL+1))
fi

echo ""
echo "→ 3. Public repo URL responds 200"
HTTP_CODE=$(curl -sIo /dev/null -w "%{http_code}" https://github.com/kritsotakis/metis-cortex)
echo "   HTTP $HTTP_CODE"
if [ "$HTTP_CODE" = "200" ]; then
  echo "   ✓ public repo accessible"
  PASS=$((PASS+1))
else
  echo "   ✗ unexpected ($HTTP_CODE — should be 200)"
  FAIL=$((FAIL+1))
fi

echo ""
echo "→ 4. (Bonus) Repo content sanity — list root via GitHub API"
ROOT_FILES=$(curl -s https://api.github.com/repos/kritsotakis/metis-cortex/contents | grep -oE '"name": *"[^"]*"' | head -8 | sed 's/"name": *"//; s/"$//')
if [ -n "$ROOT_FILES" ]; then
  echo "   Root files visible via API:"
  echo "$ROOT_FILES" | sed 's/^/     - /'
else
  echo "   (no file list returned — repo may be empty or rate-limited)"
fi

echo ""
echo "===================="
echo "Result: $PASS pass, $FAIL fail"
echo "===================="
if [ "$FAIL" -eq 0 ]; then
  echo "✓ All checks pass. Task 2 complete."
  exit 0
else
  echo "✗ Some checks failed. Surface to Cowork before declaring done."
  exit 1
fi
