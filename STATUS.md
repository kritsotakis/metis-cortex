# METIS CORTEX — STATUS

**Canonical state file.** Every Claude Code / Cowork / chat session reads this first, updates it last.
**Mirror:** `~/.claude/memory/metis-cortex-status.md`

---

**Last updated:** 2026-05-09 ~10:30 AEST · Claude Code (🟢 SITE LIVE — go-live prep landed: site config module pre-stages Calendly/email/LinkedIn/ASIC value swaps in one file; `/privacy` page closes the broken footer link with AU Privacy Act 1988 compliant draft; branded 404 page added. ASIC business name registration paid 2026-05-08, awaiting registration number in 1-2 business days.)

---

## State (3-line summary)

🟢 **SITE LIVE** at https://metiscortex.au (and https://metis-cortex.pages.dev) — Cloudflare Pages serving, SSL active, custom domain attached, all 6 critical assets HTTP 200, automatic deployments on push to main. Strategy: leveraged boutique (NOT competing with Sophiie/Chime) — AI ops layer for own portfolio (DSK + Eonia as case studies) + peers via warm intro. AI agent named **Zoe** (Greek for "life"). Phase 2 product spec for **Metis Cortex Outbound** (AI database activation) locked in `OUTBOUND-SPEC.md` after Belle Property Manly customer-discovery. Next: Calendly URL + LinkedIn page execution + DSK pilot Day 1 (sign up Retell+GHL+Twilio).

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
| Privacy policy review (or lawyer pass) | Peter | 2026-05-09 | Footer link now resolves; draft is AU Privacy Act 1988 compliant; Peter to read or hand to lawyer before considering it final |
| Analytics decision (Plausible vs GA4) | Peter | 2026-05-09 | Recommend Plausible (~€9/mo, no cookie banner). GA4 free but adds consent friction. Awaiting Peter's pick. |
| Copy reconciliation — "5 bookings" vs "5 appointments" | Peter | 2026-05-08 | Pending decision — affects Hero, Guarantee, Calendly confirmation email, onboarding sequence, sales prep |
| New Manus logo set integration | claude.ai/design + Code | 2026-05-08 | Design Claude refining; on landing, Code diffs token drift (#0e1e2e vs #0e1f3e) and swaps `public/brand/` assets in one batch |
| Hero hierarchy port (refund-guarantee anchor + italic Cormorant mix) | Code | 2026-05-08 | Held — batch with logo swap so one visible deploy. Design Claude shipped pattern in `ui_kits/marketing-site/index.html`; port to `src/components/Hero.tsx` when logos land. |

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
| Static export migration shipped — `output: 'export'`, `images.unoptimized: true`, `trailingSlash: true`, static `/public/robots.txt` + `/public/sitemap.xml`, OG `/og.png` 1200×630. Cloudflare Pages auto-deploy verified. | 2026-05-08 | Code |
| Custom domain attach — `metiscortex.au` + `www.metiscortex.au` live with SSL; GoDaddy parking A records cleaned; six-check post-attach smoke suite passing | 2026-05-08 | Peter (clicks) + Cowork (verify) |
| ASIC business name registration paid — awaiting registration number 1–2 business days | 2026-05-08 | Peter |
| Site config module `src/lib/site.ts` — single source of truth for Calendly URL, contact email, LinkedIn (personal + company), ABN/ACN, ASIC reg, pricing constants. CTAButton, Footer, layout.tsx schema all refactored to read from it. When Calendly URL / hello@ email / LinkedIn company URL / ASIC reg number lands, one-file edit propagates to Footer + CTAButton + JSON-LD + 404 + /privacy. | 2026-05-09 | Code |
| `/privacy` page — AU Privacy Act 1988 compliant draft policy at `src/app/privacy/page.tsx` (11 sections: collection, purposes, sharing, overseas, retention, security, cookies, rights, complaints, changes, contact). Closes the broken Footer link. **Needs Peter's read or lawyer pass before considering final.** | 2026-05-09 | Code |
| Branded 404 page at `src/app/not-found.tsx` — matches Hero ink+bronze treatment, links to home + contact email | 2026-05-09 | Code |

---

## Open Loops

| Item | Pending what | Date opened |
|------|--------------|-------------|
| Hosting target — Cloudflare Pages (per current plan) vs Vercel (per imported A records) | Resolves mechanically when Cloudflare Pages attaches custom domain — Pages auto-replaces Vercel A records. Per Phase 2.2 of the Cloudflare migration brief. Loop closes the moment Phase 1+2 land. | 2026-05-06 |
| DSK pilot Day 28 data | Real numbers needed for first LinkedIn case study post | Pending DSK pilot start |
| Eonia pilot start date | Confirm Eonia CMS (Cliniko/Pabau/Halaxy) for webhook spec; confirm therapist hire start date | 2026-05-06 |
| Peter sends Eonia CMS one-liner | Peter | Pending |
| Lawyer email to all 3 firms (Eonia therapist hire term sheet review, ~A$300–600 budget) | Peter | Pending |
| DSK photo curation for case study | Cowork blocked on filesystem access | Pending |

---

## Trigger Phrases (reactive)

| Trigger | Fires |
|---------|-------|
| `Phase 0 done — Cloudflare password rotated, 2FA on, GitHub repo at [URL]` | Cowork executes Cloudflare Migration Phase 1 (build artifact + push) |
| `DSK pilot Day 28 data: [numbers]` | Cowork populates LinkedIn first-post template with real figures (template held in Tasks 10–13 brief) |
| `Eonia CMS confirmed: [Cliniko/Pabau/Halaxy]` | Code generates Retell prompt + GHL workflow JSON + CMS webhook + 6 test call scripts for Eonia pilot Day 1 |
| `Calendly URL: <paste>` | Code flips `BOOKING.calendlyUrl` in `src/lib/site.ts` — propagates to every CTA button instantly |
| `Email forward live: hello@metiscortex.au` | Code flips `CONTACT.brandEmail` in `src/lib/site.ts` — Footer + JSON-LD + /privacy + 404 all update |
| `LinkedIn company page: <URL>` | Code flips `SOCIAL.linkedinCompany` in `src/lib/site.ts` — Footer link relabels and JSON-LD `sameAs` populates |
| `ASIC reg number: <number>` | Code flips `LEGAL.asicRegistrationNumber` in `src/lib/site.ts` — Footer fine print updates from "registration pending" to full reg line |
| `Analytics: Plausible` or `Analytics: GA4` | Code installs the chosen tracker (Plausible adds one script; GA4 adds tracker + cookie consent banner) |
| `Privacy policy approved` (or paste lawyer-edited copy) | Code locks the policy as final or replaces draft with lawyer copy |
| `Copy: 5 bookings` or `Copy: 5 appointments` | Code threads chosen wording across Hero, Guarantee, Calendly confirmation, onboarding emails, sales prep |

---

## Next Live Trigger

**Awaiting Peter's outputs from the four parallel tracks** ([COWORK-PARALLEL-TRACKS.md](COWORK-PARALLEL-TRACKS.md)): Calendly URL, hello@ email forward, LinkedIn company page, ASIC reg number. Each fires a one-line edit to `src/lib/site.ts` via the trigger phrases above. **Plus three decisions from Peter:** privacy policy review/approval, analytics pick (Plausible vs GA4), copy reconciliation ("5 bookings" vs "5 appointments"). All other work is held on logo/Hero batch (waiting on design Claude) or DSK pilot Day 28 data.

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
| 2026-05-08 | Claude Code | Static `/public/robots.txt` + `/public/sitemap.xml` replaced dynamic `app/robots.ts` + `app/sitemap.ts` (Next 16 `output: 'export'` rejects dynamic route handlers without `force-static`). Cloudflare Pages CI build then succeeded; site live. |
| 2026-05-08 | Peter + Cowork | Custom domain attached for `metiscortex.au` + `www`; GoDaddy parking A records removed; six post-attach smoke tests passing; SSL active (verify return code 0); cf-ray confirms Sydney edge POP. Auth-wall pattern formally adopted: Peter drives clicks in Cloudflare/GoDaddy/LinkedIn/Calendly, Cowork drives verification + STATUS. |
| 2026-05-09 | Claude Code | Site config refactor: `src/lib/site.ts` introduced as single source for Calendly, contact email, LinkedIn, ABN/ACN, ASIC reg, pricing. CTAButton, Footer, layout.tsx (incl. JSON-LD) read from it. Pre-stages every pending value swap as a one-line edit. Reasoning: each pending value (Calendly URL, hello@ email, LinkedIn company URL, ASIC reg number) was previously hardcoded across 3+ files; consolidation prevents drift and shrinks landing-day deploys. |
| 2026-05-09 | Claude Code | `/privacy` page added — AU Privacy Act 1988 compliant draft (11 sections, OAIC complaint pathway). Closes broken Footer link. Status: draft pending Peter's read or lawyer pass before treated as final. |
| 2026-05-09 | Claude Code | Branded 404 (`src/app/not-found.tsx`) added — matches Hero ink+bronze treatment. Replaces default Next.js 404. |
| 2026-05-09 | Claude Code + claude.ai/design | Hero hierarchy update + new Manus logo set held for batch deploy. Design Claude shipped #5 (refund-guarantee anchor) + #4 (italic Cormorant mix) in `ui_kits/marketing-site/index.html`; Code holds the port to `src/components/Hero.tsx` until logo files land so one visible deploy lands both changes plus any token drift fixes. Bronze (#b07843) and ink (#0e1e2e) brand tokens held — no preference-creep changes. |

---

## Reference docs (detail lives here)

| Surface | Where |
|---------|-------|
| Project root | `~/Desktop/metis-cortex/` |
| Cowork briefs (numbered series) | `COWORK-*.md` files (Cloudflare, Infrastructure, Status Sync, Tasks 10-13, Tasks 14-15) |
| Existing handoff conventions | `AGENTS.md` + `CLAUDE.md` (project-local) |
| Brand bundle | `brand/` subfolder |
| Eonia pilot pack | `eonia-pilot-pack.md` |
| Eonia therapist term sheet | `eonia-therapist-engagement-termsheet.md` |
| LinkedIn outreach plan | `LINKEDIN-FIRST-100-OUTREACH.md` |
| Cold email v1 prospects | `COLD-EMAIL-V1-PROSPECTS.md` |
| DSK pricing grid (Retell agent input) | `DSK-PRICING-GRID.md` |
| Calendly confirmation email | `CALENDLY-CONFIRMATION-EMAIL.md` |
