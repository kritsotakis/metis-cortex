# METIS CORTEX — STATUS

**Canonical state file.** Every Claude Code / Cowork / chat session reads this first, updates it last.
**Mirror:** `~/.claude/memory/metis-cortex-status.md`

---

**Last updated:** 2026-05-07 ~12:55 AEST · Claude Code (Path A static-export migration in flight — code changes applied locally, build verification in progress, push gated on Phase 0 + GitHub repo URL)

---

## State (3-line summary)

Metis Cortex (Speed-to-Lead AI receptionist agency) is pre-launch. Brand bundle v3 integrated, code production-ready, Cloudflare zone added (DNS imported with Vercel A records — see Decision Log re: hosting target). Strategy: leveraged boutique (NOT competing with Sophiie/Chime) — AI ops layer for own portfolio (DSK + Eonia as case studies) + peers via warm intro. AI agent named **Zoe** (Greek for "life"). Cowork executing Cloudflare migration + Apollo prospect enrichment. Eonia Frontline pilot pack drafted as case study #2.

---

## In Flight

| Item | Owner | Started | Blocking |
|------|-------|---------|----------|
| 🔴 SECURITY: Cloudflare password rotation (pasted plaintext in chat 2026-05-06) + 2FA confirmation | Peter | 2026-05-06 | Phase 1 of Cloudflare migration gated on this |
| GitHub repo creation: `kritsotakis/metis-cortex` (private) | Peter | Pending | Cowork Phase 1+ gated |
| Cowork: Cloudflare migration Phase 1+2+3 (~80 min) | Cowork | Awaiting Phase 0 (Peter) | Live site cutover |
| Calendly demo URL setup | Peter | Pending (15 min) | First booking infrastructure |
| GoDaddy email forward | Peter | Pending (10 min) | Inbound contact path |
| LinkedIn company page launch | Peter | Pending (30 min, assets ready) | First-100 outreach plan unblocks |
| Apollo enrichment of 26 → 50 prospects | Peter | Pending (15 min) | DO NOT send until DSK pilot data lands |
| **Static export migration Phase 1 — local code changes** | Code | 2026-05-07 ~12:55 | Applied: `output: 'export'` + `images.unoptimized` + `trailingSlash` in next.config.ts; `openGraph.images` + `twitter.images` referencing `/og.png` in layout.tsx; deleted `src/app/opengraph-image.tsx` + `twitter-image.tsx`. **Build verification in flight** — Turbopack appears to hang on static export, retrying with `--no-turbopack` (webpack). Push gated on Peter's GitHub repo URL. |

---

## Done Recently

| Item | Date | By |
|------|------|-----|
| Brand bundle v3: dark + light SVG lockups (real-text vector), transparent mark PNG, 3-page brand guide PDF, social kit for 7 platforms, favicon ladder (9 sizes) | 2026-05-04 to 2026-05-06 | Cowork + Code |
| Site code: 9 components, Cormorant + Inter typography, brand mark inline (Hero navy bg + Footer transparent), brand spec applied (.au canonical, ink #0e1e2e, bronze #b07843, cream #f5f1ea) | 2026-05-04 | Code |
| AI agent renamed Mia → Zoe ("life" in Greek) | 2026-05-04 | Peter |
| `.ai` domain skipped, `.au` canonical confirmed | 2026-05-04 | Peter |
| Cowork Tasks 7–9 synced into repo (memory diffs applied, LinkedIn first-100 outreach plan, 26-row Sydney prospect list with Apollo handoff) | 2026-05-06 | Cowork + Code |
| Cloudflare zone added for metiscortex.au (DNS imported — Vercel A records present, will be replaced when Pages custom domain attaches) | 2026-05-06 | Peter |
| Task 10 — Calendly confirmation email + no-show follow-up | 2026-05-06 | Cowork + Code sync (CALENDLY-CONFIRMATION-EMAIL.md at project root) |
| Task 11 — Onboarding email sequence (4 emails: Day 1 / Day 3 / Day 7 / Day 14) | 2026-05-06 | Cowork + Code sync (ONBOARDING-EMAIL-SEQUENCE.md at project root) |
| Task 12 — LinkedIn first-post template + 3 hook variants + comment + DM scripts | 2026-05-06 | Cowork + Code sync (LINKEDIN-FIRST-POST-DRAFT.md at project root) |
| Task 13 — DSK pricing grid + Retell-ready YAML/JSON | 2026-05-06 | Cowork + Code sync (DSK-PRICING-GRID.md at project root) |
| Task 14 — Sales prep package (10-min demo flow + 10 objections + 5 pricing rebuttals) | 2026-05-07 | Cowork + Code sync (SALES-PREP-PACKAGE.md at project root) |
| Task 15 — Pilot data capture kit (11-screenshot checklist + Day 28 metrics report email) | 2026-05-07 | Cowork + Code sync (PILOT-CAPTURE-KIT.md at project root) |
| STATUS protocol formally adopted by Metis Cortex Cowork session — confirmation receipt posted with load-bearing details quoted back | 2026-05-07 | Cowork |

---

## Open Loops

| Item | Pending what | Date opened |
|------|--------------|-------------|
| Hosting target — Cloudflare Pages (per current plan) vs Vercel (per imported A records) | Resolves mechanically when Cloudflare Pages attaches custom domain — Pages auto-replaces Vercel A records. Per Phase 2.2 of the Cloudflare migration brief. Loop closes the moment Phase 1+2 land. | 2026-05-06 |
| DSK pilot Day 28 data | Real numbers needed for first LinkedIn case study post | Pending DSK pilot start |
| Eonia Frontline pilot start date | Confirm Eonia CMS (Cliniko/Pabau/Halaxy) for webhook spec; confirm therapist hire start date | 2026-05-06 |
| Peter sends Eonia CMS one-liner | Peter | Pending |
| Lawyer email to all 3 firms (Eonia therapist hire term sheet review, ~A$300–600 budget) | Peter | Pending |
| DSK photo curation for case study | Cowork blocked on filesystem access | Pending |

---

## Trigger Phrases (reactive)

| Trigger | Fires |
|---------|-------|
| `Phase 0 done — Cloudflare password rotated, 2FA on, GitHub repo at [URL]` | Cowork executes Cloudflare Migration Phase 1 (build artifact + push) |
| `DSK pilot Day 28 data: [numbers]` | Cowork populates LinkedIn first-post template with real figures (template held in Tasks 10–13 brief) |
| `Eonia CMS confirmed: [Cliniko/Pabau/Halaxy]` | Code generates Retell prompt + GHL workflow JSON + CMS webhook + 6 test call scripts for Eonia Frontline pilot Day 1 |

---

## Next Live Trigger

**Awaiting Peter's Phase 0 (Cloudflare password rotation + 2FA + GitHub repo creation).** Once Phase 0 confirmed, Cowork executes Phase 1+2+3 of Cloudflare migration (~80 min total). Site goes live on Cloudflare Pages immediately after.

---

## Decision Log (append-only)

| Date | Session | Decision |
|------|---------|----------|
| 2026-05-04 | Peter | Strategy: leveraged boutique, AI ops layer for own portfolio (DSK + Eonia as case studies) + peers via warm intro. NOT competing with Sophiie/Chime. |
| 2026-05-04 | Peter | AI agent name: Zoe (Greek for "life"). Replaces Mia. |
| 2026-05-04 | Peter | Domain: `.au` canonical (`.ai` skipped) |
| 2026-05-04 | Code | Brand spec applied: ink #0e1e2e, bronze #b07843, cream #f5f1ea, Cormorant + Inter typography |
| 2026-05-06 | Peter | Cloudflare account = peter@kritsotakis.com.au; metiscortex.au added as zone |
| 2026-05-06 | Peter | Cloudflare password compromised (pasted plaintext in chat) — rotation required |
| 2026-05-07 | Claude Code | STATUS file adopted |
| 2026-05-07 | Metis Cortex Cowork | STATUS protocol formally adopted (read STATUS_PROTOCOL_FOR_COWORK.md + STATUS.md, confirmation receipt posted with load-bearing details quoted back). Operational reality flag: until Cowork has filesystem write access to `~/Desktop/metis-cortex/`, session-end STATUS updates are delivered as STATUS-diff docs in outputs folder for Code to apply. |
| 2026-05-07 | Metis Cortex Cowork | State correction: Tasks 10–15 are delivered (Cowork side) — STATUS In-Flight ledger updated to reflect that Cowork's work is done; only Code sync from outputs folder into `~/Desktop/metis-cortex/` is pending |
| 2026-05-07 | Metis Cortex Cowork | Hosting target Open Loop note expanded — drift resolves mechanically via Pages custom domain attach (Phase 2.2 of Cloudflare migration brief) |
| 2026-05-07 | Claude Code (Path A) | Static export migration applied locally — `output: 'export'`, `images.unoptimized: true`, `trailingSlash: true` added to next.config.ts. layout.tsx metadata wired to `/og.png` (1200×630). Dynamic OG endpoints (`opengraph-image.tsx`, `twitter-image.tsx`) deleted. **Build hangs on Turbopack** — retrying with `--no-turbopack` flag to use webpack (legacy build path). Will commit + stage push when build succeeds. Awaiting Peter's GitHub repo URL to push. |

---

## Reference docs (detail lives here)

| Surface | Where |
|---------|-------|
| Project root | `~/Desktop/metis-cortex/` |
| Cowork briefs (numbered series) | `COWORK-*.md` files (Cloudflare, Infrastructure, Status Sync, Tasks 10-13, Tasks 14-15) |
| Existing handoff conventions | `AGENTS.md` + `CLAUDE.md` (project-local) |
| Brand bundle | `brand/` subfolder |
| Eonia Frontline pilot pack | `eonia-frontline-pilot-pack.md` |
| Eonia therapist term sheet | `eonia-therapist-engagement-termsheet.md` |
| LinkedIn outreach plan | `LINKEDIN-FIRST-100-OUTREACH.md` |
| Cold email v1 prospects | `COLD-EMAIL-V1-PROSPECTS.md` |
| DSK pricing grid (Retell agent input) | `DSK-PRICING-GRID.md` |
| Calendly confirmation email | `CALENDLY-CONFIRMATION-EMAIL.md` |
