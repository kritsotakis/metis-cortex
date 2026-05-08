# Cowork brief — Task 4: Custom domain `metiscortex.au` + SSL

> **For:** Cowork
> **Authored by:** Claude Code, 2026-05-08
> **Goal:** Get `https://metiscortex.au` resolving to the Cloudflare Pages deployment with valid SSL. Custom domain attached, nameservers configured, SSL provisioned, all six post-attach smoke tests passing.

---

## State of play

- ✅ Site live at `metis-cortex.pages.dev` (HTTP 200, all 6 critical assets serving)
- ✅ Cloudflare Pages project `metis-cortex` exists in account `0642c8fc02f351034537860996d9c4c2`, automatic deployments enabled, latest deploy is commit `c6b8090`
- ✅ Cloudflare zones for `metiscortex.au` AND `exitcode.trade` already added to the account (visible in account dashboard)
- ⚠️ Both `metiscortex.au` and `exitcode.trade` zones show **red ⚠** in the Domains panel — likely because **GoDaddy nameservers haven't been swapped to Cloudflare's yet**. dsk.au shows green ✅ (already on Cloudflare nameservers).
- ❌ Custom domain `metiscortex.au` NOT yet attached to the Pages project
- ❌ SSL not provisioned for the canonical domain

---

## The auth wall (already documented in PAIR.md)

You confirmed earlier that **Chrome MCP / kapture is a separate session from Peter's logged-in Chrome**. Cloudflare's session-bound auth doesn't transfer. Same wall as Task 3.

Therefore: **Peter drives the clicks in Cloudflare and GoDaddy. You drive the verification + STATUS update.** Don't waste cycles trying to drive Cloudflare's UI from your sandbox.

---

## What Peter does (you brief him with these exact instructions)

Send Peter this guidance verbatim if he asks, or as a check-in if he doesn't:

### Step 1 — Add custom domain in Pages project (~2 min)

1. dash.cloudflare.com → Workers & Pages → click **`metis-cortex`** project
2. **`Custom domains`** tab (next to Deployments / Metrics / Settings)
3. Click **`Set up a custom domain`**
4. Enter: `metiscortex.au`
5. Click **Continue**
6. Cloudflare may show one of three things:
   - **(a) "Domain ready"** → click **Activate**, done, jump to Step 3
   - **(b) "Nameservers need to be Cloudflare's"** with 2 nameserver values shown → continue to Step 2
   - **(c) "Add a CNAME at your registrar"** with a CNAME value → continue to Step 2 alternative

### Step 2 — Nameserver swap at GoDaddy (only if Cloudflare asks, ~5 min + propagation)

If Cloudflare showed option (b) above:

1. Copy the 2 Cloudflare nameservers shown (likely `emerie.ns.cloudflare.com` + `jimmy.ns.cloudflare.com` based on prior account work, but use whatever Cloudflare displays)
2. Open new tab → **GoDaddy** → My Products → **`metiscortex.au`** → **DNS** → **Nameservers** → **Change** → **"I'll use my own nameservers"**
3. Paste the 2 Cloudflare nameservers, save
4. Wait 5–60 min for propagation. Cloudflare emails you when active.

If Cloudflare showed option (c) — CNAME at registrar — alternative path:

1. Copy the CNAME target (something like `metis-cortex.pages.dev`)
2. GoDaddy DNS → Add a CNAME record at root or `www` pointing at the Cloudflare value
3. Save, wait for propagation

### Step 3 — Wait for SSL provisioning (~1–10 min)

Cloudflare auto-provisions Universal SSL for the new custom domain. Watch the Custom domains tab — status flips from `Pending` → `Active` when SSL is ready.

### Step 4 — Verify Peter's done

Tell Peter: *"Reply with `metiscortex.au live` when the Custom domains tab shows green Active for that domain."*

---

## What Cowork does after Peter says it's live

### Run the post-attach smoke suite

Six checks, each in its own bash call. Don't skip any.

```bash
# 1. Custom domain serves over HTTPS
curl -sIo /dev/null -w "metiscortex.au → HTTP %{http_code}\n" https://metiscortex.au
# Expected: 200
```

```bash
# 2. Same content as the .pages.dev preview URL (sanity check that custom domain points at our project)
diff <(curl -sL https://metis-cortex.pages.dev | head -50) <(curl -sL https://metiscortex.au | head -50)
# Expected: empty diff (same first 50 lines of HTML)
```

```bash
# 3. SSL chain valid — issuer + verify status
echo | openssl s_client -servername metiscortex.au -connect metiscortex.au:443 2>/dev/null | grep -E 'subject|issuer|verify return'
# Expected: subject = CN=metiscortex.au; issuer is a recognised CA (Google Trust Services / Lets Encrypt / Cloudflare); verify return code: 0 (ok)
```

```bash
# 4. og.png NOW resolves on canonical domain (the OG meta in layout.tsx points here, was 404 before custom domain attached)
curl -sIo /dev/null -w "og.png on .au: %{http_code}\n" https://metiscortex.au/og.png
# Expected: 200
```

```bash
# 5. HTTP redirects to HTTPS
curl -sIo /dev/null -w "http→https: %{http_code}\n" -L http://metiscortex.au
# Expected: 200 (after redirect chain), or use -I to see the 301/308 directly
```

```bash
# 6. Edge POP serving (confirms it's actually Cloudflare and not a misconfigured proxy)
curl -sI https://metiscortex.au | grep -iE 'server|cf-ray'
# Expected: server: cloudflare; cf-ray: <hash>-SYD (Sydney edge for AU traffic)
```

If all six pass, declare Task 4 done. If any fail, surface the specific failure to Peter (don't improvise).

### Update STATUS.md

Append to **Done This Sprint**:

> 2026-05-08 — Custom domain `metiscortex.au` attached to Pages project, SSL provisioned, all 6 smoke tests passing. Site live at canonical domain. Peter (clicks in Cloudflare/GoDaddy) + Cowork (verification + STATUS).

Close in **Open Loops**:
- "Custom domain attach pending"
- "SSL provisioning pending"
- "GoDaddy nameserver swap" (if it happened in Step 2)

Append to **Decision Log**:

> 2026-05-08 — Cowork (kapture browser) cannot drive Cloudflare/GoDaddy session-bound UIs (auth wall confirmed Task 3 and re-confirmed Task 4). Permanent operational pattern: Peter drives clicks in those tools; Cowork drives verification + state.

Mirror to `~/.claude/memory/metis-cortex-status.md` (Code will sync — outside Cowork's filesystem scope).

### Tell Peter what's next

Once verification passes, tell Peter:

> ✅ metiscortex.au live with valid SSL.
> Six smoke tests passing.
> STATUS.md updated.
>
> Next 3 tasks ready to run in parallel — pick whichever order suits:
> - Task 6 — Calendly demo URL (15 min, your browser)
> - Task 7 — GoDaddy hello@metiscortex.au email forward (10 min, your browser)
> - Task 8 — LinkedIn company page (30 min, your browser, assets in public/brand/social/ ready)
>
> Plus the parallel async work:
> - Task 10 — Send lawyer email to all 3 firms (5 min, draft in THERAPIST-LAWYER-SHORTLIST.md)
> - Send Eonia CMS WhatsApp (30 sec, message in EONIA-CMS-MESSAGE.md)
>
> When Calendly URL lands, paste it back to Code — Code updates CTAButton.tsx in same commit batch as the Footer email update.

---

## What Cowork must NOT do

- **Do not** retry Cloudflare or GoDaddy clicks via kapture. The auth wall is confirmed permanent.
- **Do not** try to access GoDaddy via API without explicit token from Peter (we don't have one configured).
- **Do not** declare Task 4 done without all six smoke tests passing.
- **Do not** proceed to Task 5 (a separate explicit nameserver swap brief) — it's effectively merged into Task 4 Step 2 above. If Cloudflare didn't require a nameserver swap in Step 1, Task 5 is a no-op.
- **Do not** modify the `next.config.ts`, `layout.tsx`, or `og.png` files. They're correct as-is. The OG image meta points at `metiscortex.au/og.png` deliberately.
- **Do not** commit or push to GitHub. The deployment is automatic via Pages Git integration.

---

## Confirmation Cowork posts back

After all six smoke tests pass:

```
✅ Task 4 done. metiscortex.au live with SSL.
   Verified:
   - https://metiscortex.au → 200
   - HTML matches .pages.dev preview (no diff)
   - SSL chain valid, verify return code 0, issuer = [name]
   - og.png on canonical domain → 200
   - http → https redirect working
   - Edge POP: cf-ray <hash>-SYD (Sydney)
   STATUS.md updated, memory mirror flagged for Code.
   Standing by for Tasks 6/7/8/10 triggers from Peter.
```

If any check fails:

```
⚠️ Task 4 partial. metiscortex.au attached but [specific failure].
   Surfacing to Peter:
   - [the failing check + actual result]
   - [recommended fix]
   STATUS.md NOT yet updated.
```

---

## Reference

- `STATUS.md` — canonical state
- `COWORK-PETER-DELEGATIONS.md` — full Tasks 1–10 delegation
- `COWORK-PUSH-EXECUTION.md` — Task 2 execution log (which set the precedent that Peter drives session-bound UIs)
- `PAIR.md` — running session log
