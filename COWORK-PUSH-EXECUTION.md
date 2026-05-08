# Cowork brief — Execute the push

> **For:** Cowork
> **Authored by:** Claude Code, 2026-05-07
> **Goal:** Get commit `7343bef` (currently sitting in Peter's local repo) pushed to `origin/main` at `https://github.com/kritsotakis/metis-cortex.git`. Once that lands, you trigger Tasks 3–10 from `COWORK-PETER-DELEGATIONS.md`.

---

## State of play

- ✅ Commit landed locally: `7343bef feat: brand bundle v3, static export, full content suite`
- ✅ Remote `origin` set to `https://github.com/kritsotakis/metis-cortex.git`
- ✅ Cloudflare Phase 0 confirmed by Peter (password rotated, 2FA enabled)
- ✅ GitHub repo created (empty) at the URL above
- ✅ Peter has installed **GitHub Desktop** on his Mac (this is the path he picked)
- ❌ Push has NOT happened — repo at the URL is still empty

The push is the only thing standing between current state and "site live within 90 min."

---

## Why earlier paths failed

1. **Token paste in Terminal failed** — macOS Terminal + zsh + paste-into-password-prompt is genuinely flaky. Token didn't paste correctly twice; second attempt ended up at a shell prompt as "command not found." Old token is now compromised (visible in screenshot Peter sent), needs revocation.
2. **Token-to-Code paste path** — offered but Peter didn't take it (auth dance is annoying).
3. **GitHub Desktop** — Peter's chosen path. UI-driven, no token paste required, OAuth handles auth.

---

## What Cowork executes

You have **kapture** (browser automation + screen capture) — use it.

### Path A — drive the flow visually if kapture supports native macOS apps

If kapture can drive native macOS apps (not just Chrome):

1. Bring GitHub Desktop to foreground (or launch from /Applications/GitHub Desktop.app)
2. If sign-in screen showing → click **`Sign in to GitHub.com`** → kapture drives the resulting OAuth flow in Chrome (which it can definitely handle) → after browser redirects to "Open GitHub Desktop?", click **Open GitHub Desktop**
3. **File menu → Add Local Repository** → choose `~/Desktop/metis-cortex` → Add
4. The unpushed commit `7343bef` will be visible in the GitHub Desktop UI
5. Click **`Publish branch`** (or **`Push origin`** depending on UI state)
6. Wait for push to complete (~5 sec)

### Path B — drive the OAuth + verify, ask Peter to click Push

If kapture is browser-only (most likely case):

1. Drive Chrome to github.com via OAuth flow if needed for auth confirmation
2. Verify Peter is signed into GitHub in his Chrome session
3. **Tell Peter to click `Publish branch` / `Push origin` in GitHub Desktop** — give him a one-line instruction
4. Wait for him to confirm the click happened

### Path C — alternative if both A and B blocked

Peter does the click himself (GitHub Desktop is open on his Mac, the button is visible). You stand by for the verification step (post-push curl + repo state check).

---

## Verification — required before declaring Task 2 done

Run these checks in order. ALL must pass:

```bash
# 1. Local + remote refs match
cd ~/Desktop/metis-cortex
git log --oneline -1                              # should show 7343bef
git ls-remote origin main 2>/dev/null | head -1   # should show 7343bef as the SHA
```

```bash
# 2. Repo is publicly accessible (gives 200 not 404)
curl -sIo /dev/null -w "%{http_code}\n" https://github.com/kritsotakis/metis-cortex
# Expected: 200
```

```bash
# 3. Repo has the expected file structure (sanity check via API)
curl -s https://api.github.com/repos/kritsotakis/metis-cortex/contents | head -20
# Expected: JSON listing the root files (README.md, next.config.ts, src/, public/, etc.)
```

If any check fails, surface the specific output. Don't declare done until all three pass.

---

## After push lands — three immediate follow-ups

### 1. Update STATUS.md

Open Loops:
- Close "GitHub repo creation pending"
- Close "commit + push pending"

Done This Sprint — add:
- 2026-05-07 — Static export migration committed + pushed (`7343bef`) by Code (commit) + Peter (push via GitHub Desktop) + Cowork (verification)

Decision Log — append:
- 2026-05-07 — Push path resolved: token paste in Terminal failed twice (macOS keychain + zsh paste flakiness); switched to GitHub Desktop OAuth; clean push achieved

Mirror to `~/.claude/memory/metis-cortex-status.md` (Code will sync this — it's outside Cowork's filesystem scope).

### 2. Tell Peter the leaked token MUST be revoked

The token he generated as `metis-cortex push` is visible in a screenshot from earlier in the chat. Even though he didn't successfully push with it, it's a valid 30-day token. Confirm with Peter that he's revoked it at github.com/settings/tokens. If he hasn't, do not proceed to Task 3 — security hygiene first.

### 3. Proceed to Task 3 (Cloudflare Pages → Connect to Git)

Per `COWORK-PETER-DELEGATIONS.md`. The trigger phrase Peter posts — *"Push landed. Commit SHA: 7343bef on origin/main. Proceeding to Task 3 (Cloudflare Pages connect)."* — fires this. Don't wait for explicit instruction beyond that.

---

## What Cowork must NOT do

- **Do not** generate or accept any GitHub Personal Access Tokens. The OAuth flow Peter has chosen via GitHub Desktop is the correct path; tokens are out of scope now.
- **Do not** attempt to bypass the GitHub Desktop UI by writing files directly to GitHub via API — the commit is already made locally; only the push is needed.
- **Do not** modify the local commit or remote URL. Both are correct.
- **Do not** declare Task 2 done without all three verification checks passing. The framing rule applies — "I think it pushed" is not "it pushed."
- **Do not** proceed to Task 3 if the leaked token hasn't been revoked. Security first.

---

## Confirmation Cowork posts back

```
✅ Push landed. Commit 7343bef now on origin/main.
   Verified:
   - git log local: 7343bef
   - git ls-remote origin main: 7343bef
   - github.com/kritsotakis/metis-cortex: HTTP 200, files present
   - Leaked token revoked: confirmed by Peter
   STATUS.md updated, memory mirror flagged for Code.
   Proceeding to Task 3 (Cloudflare Pages → Connect to Git).
```
