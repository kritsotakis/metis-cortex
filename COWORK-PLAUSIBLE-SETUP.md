# Cowork brief — Plausible analytics setup for metiscortex.au

> **For:** Cowork
> **Authored by:** Claude Code, 2026-05-09
> **Goal:** Get Plausible Analytics live on https://metiscortex.au — privacy-respecting, no cookie banner needed, AU-friendly. Site account created, Cowork verifies the dashboard is provisioned, then Code wires the tracker script in `src/app/layout.tsx` and ships.

---

## State of play

- ✅ Site live at https://metiscortex.au + https://www.metiscortex.au, auto-deploy on push to main
- ✅ Site config refactor landed today — single source of truth at `src/lib/site.ts`
- ❌ Zero analytics currently. We don't know if anyone's hitting the site, where they bounce, or whether the CTA button gets clicked.

---

## Why Plausible (not GA4)

Locked decision (Peter, 2026-05-09):

- **No cookie banner needed.** Plausible doesn't use cookies, so we skip the consent friction that kills first-impression conversion.
- **AU-friendly + GDPR-friendly.** No personal data collected. Aligns with our `/privacy` policy commitments.
- **Cheap.** ~€9/mo for the Growth plan (covers 10k pageviews — way more than we'll have for months).
- **Lightweight.** ~1 KB script vs GA4's ~50 KB. Matters because Cowork already flagged Cormorant + Inter as a font-loading concern.
- **Honest dashboard.** No vanity metrics, no sampling, no event modelling. Just pageviews + sources + paths.

---

## The auth wall (same pattern as Calendly / GoDaddy / LinkedIn / Cloudflare)

Plausible requires email signup → email verification → dashboard creation. **Session-bound auth that kapture cannot drive.** Peter clicks. You verify.

---

## What Peter does (brief him with this verbatim)

> **Goal:** A live Plausible dashboard for `metiscortex.au` so Code can drop in the tracker script.
>
> **Steps:**
> 1. plausible.io → **Start your free trial** (or **Log in** if you already have an account)
> 2. Sign up with **peter@kritsotakis.com.au** — Plausible emails a verification link, click it
> 3. **Add a site:**
>    - Domain: `metiscortex.au` (no www, no protocol — just the bare domain)
>    - Timezone: `Australia/Sydney`
>    - Reporting timezone setting: AEST/AEDT
> 4. After save, Plausible shows a snippet like:
>    ```html
>    <script defer data-domain="metiscortex.au" src="https://plausible.io/js/script.js"></script>
>    ```
>    **You don't paste this anywhere — Code will add it via the repo. Just confirm the dashboard exists.**
> 5. **Plan:** start on the free trial; after 30 days move to **Growth** (€9/mo, 10k pageviews, way over what we'll do for months). No need to enter card today.
> 6. **Optional but recommended:** in dashboard settings → **Visibility** → set to `Anyone with the link` so Cowork (and future you, on phone, anywhere) can view stats without logging in. Keep the URL private — share only with the team.
> 7. Reply with: `Plausible site ready` (and the dashboard URL if you made it public, e.g. `plausible.io/metiscortex.au`)

---

## What Cowork does after Peter posts `Plausible site ready`

### Verify the dashboard is reachable

If Peter shared a public dashboard URL:

```bash
curl -sIo /dev/null -w "Plausible dashboard: HTTP %{http_code}\n" https://plausible.io/metiscortex.au
# Expected: 200
```

If Peter kept it private (default), skip the curl — just trust his confirmation. Don't try to log in via kapture.

### Flag Code via PAIR.md

```
### YYYY-MM-DD HH:MM — cowork → code
**Did:** Plausible site provisioned for metiscortex.au. Dashboard live at <URL or 'private'>.
**Need from you:** Add Plausible tracker to src/app/layout.tsx (one-line script tag). Verify pageviews appear in the dashboard within 5 min of next deploy.
**Status:** ⏸️ waiting-on-pair
```

### After Code lands the script (you'll see a commit on main)

Once Code reports the script is deployed:

1. **Trigger a pageview** — open https://metiscortex.au in any browser (don't use private/incognito — Plausible respects DNT). Refresh once.
2. **Wait ~30 seconds** — Plausible pipeline is near-realtime but not instant.
3. **Confirm to Peter:** *"Plausible live — first pageview registered at HH:MM. Dashboard at <URL>."*

### Update STATUS.md

Append to **Done Recently**:

> 2026-05-09 — Plausible Analytics live for metiscortex.au — privacy-respecting, no cookie banner. Peter (signup) + Cowork (verify) + Code (script wire-up).

Close in **Open Loops**: "Analytics decision (Plausible vs GA4)"

Mirror to `~/.claude/memory/metis-cortex-status.md` (Code will sync if filesystem write is out of scope).

---

## What Cowork must NOT do

- **Do not** drive Plausible signup via kapture — Peter signs in.
- **Do not** paste the Plausible script into any file — Code owns repo edits.
- **Do not** enable extensions / event tracking / file download tracking yet — base pageview tracking only for v1. We add events when we have something to measure (CTA click, /privacy view).
- **Do not** declare Plausible "live" until you've confirmed at least one pageview lands in the dashboard after deploy.

---

## Trigger phrase summary

| Trigger | Fires |
|---------|-------|
| `Plausible site ready` | Code adds `<script defer data-domain="metiscortex.au" src="https://plausible.io/js/script.js"></script>` to `<head>` in `src/app/layout.tsx`. Commits + pushes. Cloudflare auto-deploys. |
| `First pageview confirmed` | Cowork closes the loop, updates STATUS, mirrors to memory. |

---

## Reference

- [STATUS.md](STATUS.md) — canonical state
- [COWORK-PARALLEL-TRACKS.md](COWORK-PARALLEL-TRACKS.md) — Calendly + email + LinkedIn + ASIC parallel queue
- [src/app/layout.tsx](src/app/layout.tsx) — where Code adds the script tag
- Plausible docs: https://plausible.io/docs
