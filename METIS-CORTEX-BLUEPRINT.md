# METIS CORTEX — BLUEPRINT, VISION & ROADMAP

**Version 1.0 — 2026-07-30**

This is Metis Cortex's own blueprint — written by Claude Code from the actual
codebase and `STATUS.md`, not generated speculatively. It replaces the
5-volume ChatGPT "Master Product Blueprint" Peter had drafted separately,
which specced an enterprise rewrite (.NET/C#, PostgreSQL, Azure, microservices)
disconnected from what's actually built and running.

**Status tags used throughout, so this document can't drift into overclaiming:**
- 🟢 **LIVE** — shipped, deployed, real users can use it today
- 🟡 **BUILT, NOT OPEN** — code exists and works, gated behind a real blocker
- 🔵 **PLANNED** — scoped, not started
- ⚪ **VISION** — the direction, not yet scoped as engineering work

---

## 1. Positioning

**Australia's AI-assisted legal matter platform — an organiser, not a lawyer.**

An intelligent workspace connecting clients and solicitors from the start of
a matter to its resolution. Metis does not compete with practice-management
software or replace a solicitor's judgement — it removes the administrative
and organisational burden around a matter so both sides spend less time on
paperwork and more time on the actual legal work.

**What Metis is:**
- A document-organisation and preparation tool for individuals
- A meeting-capture and drafting aid for solicitors
- A shared workspace that keeps both sides in sync on one matter

**What Metis is explicitly not** (this line is load-bearing — it's why a
solicitor like Simon can look at it without feeling threatened):
- Not a law firm, not a source of legal advice
- Not a replacement for a solicitor
- Not a generic document-management tool
- Not a case-law citation engine (it never cites case law, by design)

This positioning is already live on the site
([Home.tsx:101](app/client/src/pages/Home.tsx:101),
[Home.tsx:308](app/client/src/pages/Home.tsx:308)) — this document just makes
it explicit as a standing principle, not something to re-litigate per feature.

---

## 2. Core philosophy

1. **Reduce administrative pain**, on both sides of a matter.
2. **Organise evidence and documents** — the single biggest recurring pain
   point identified across every round of user/solicitor conversation so far.
3. **Improve client↔solicitor communication** — fewer status-chasing calls,
   clearer visibility into what's outstanding.
4. **Integrate with what firms already use** rather than asking them to
   replace it. LEAP first (see §5).
5. **Honesty over confidence.** Metis would rather say "I don't know" or
   "unreadable" than guess. This isn't a slogan — it's enforced in code
   (§7) and has already shaped real product decisions (the checklist
   marks a filename match as a *suggestion the user confirms*, never a
   detection Metis claims credit for).

---

## 3. Product: three platforms

### Platform 1 — Client Portal 🟢 LIVE

For individuals going through a family law matter, without a solicitor yet
or in parallel with one.

- Matter-type triage (free-text description → suggested matter type, e.g.
  parenting, property settlement, divorce)
- Per-matter-type document checklist with retrieval instructions (what to
  gather, why it matters, where to get it)
- Document upload with filename-based suggestion matching (never an
  auto-confirmed detection — the user always confirms)
- Rails-gated chat scoped to the user's own matter and documents
- Exportable **Matter Pack** — a single inventory-only summary to bring to
  a solicitor's first appointment

**Goal:** walk into the solicitor's office organised, not with a shoebox.

**Not yet built:** intake questionnaires beyond the triage step, a distinct
"matter summary" view separate from the checklist, OCR/PDF text extraction
(blocks chronology, asset schedules, annexure numbering — see §6).

### Platform 2 — Solicitor Workspace 🟡 BUILT, NOT OPEN

For solicitors running client consultations.

- Meeting capture with AI-assisted note generation — 🟡 blocked: no
  transcription backend has a configured API key (Deepgram account not yet
  created; this is Peter's action item, not an engineering gap)
- Case brief / file note generation, force-capturing the two
  negligence-critical fields from *Sewell v Zelden* [2010] NSWSC 1180
  (risks warned of, client's response) — 🟢 built and tested
- Legislation/case-law surfacing via live AustLII search + a pre-loaded AU
  family-law knowledge base — 🟢 built and tested
- Task/action-item tracking per client — 🟢 built
- Compliance artefacts: conflict check, client ID/verification record,
  costs disclosure (LPUL s174/s178), costs agreement (s180) — 🟢 built,
  all generated content carries a **DRAFT — not lawyer-reviewed** banner
- LEAP sync — 🔵 planned, see §5

**Why it's not open:** four gates, none of them engineering work —
lawyer review of the generated templates, professional indemnity cover, an
AU data-residency decision, and a ToS/privacy pass. The product is closer
to done than these gates suggest; they're business/compliance work, not
code.

### Platform 3 — Shared Matter Portal ⚪ VISION (not built)

A live task list, document-request thread, messaging, appointments, and a
shared progress dashboard that both the client and their solicitor see —
one matter, one shared source of truth.

**Important gap to be upfront about:** Platform 1 (the new client-first
matters model — `matters`, `matterDocuments`, `matterChecklistItems`) and
Platform 2's client-facing side (the older `portalDocuments`,
`portalMessages`, `actionItems`, `caseMilestones` tables, token-based
`ClientPortal.tsx`) are **two separate systems today, built at different
times, not bridged.** A client using Platform 1 and a solicitor using
Platform 2 on the same real-world matter currently have no shared record.
Building Platform 3 for real means either merging these two data models or
building an explicit bridge between them — that's a real architecture
decision, not just new UI, and belongs in its own scoped plan before any
code gets written.

---

## 4. Roadmap — practice-area expansion

**Phase 1 — Family law 🟢 LIVE.** Deliberately the beachhead: highest
document-gathering burden, highest emotional stakes, existing willingness to
pay, and the only area with a built-out knowledge base (post-May-2024 s60CC
parenting rules, the 4-step property framework, disclosure duties under
s71B/s90RI).

The order below is a recommendation, reasoned from what actually transfers
from the family-law build — not the raw court-filing-volume order an LLM
will default to (criminal/traffic tops volume, but volume alone doesn't
mean Metis's core value — document organisation — has anywhere to land):

**Phase 2 — Wills & estates 🔵 planned-next.** Same shape of pain as family
law: heavy document gathering (asset registers, beneficiary details, prior
wills), low real-time conflict, long preparation windows. Closest fit to
what's already built.

**Phase 3 — Employment law 🔵 planned.** Also document/timeline-heavy
(contracts, correspondence, incident timelines) and shares family law's
emotional-stakes profile.

**Phase 4 — Civil disputes (general) 🔵 planned.** Broader and more
heterogeneous — will likely need to be scoped as several sub-templates
rather than one, closer to how family law itself splits into
parenting/property/divorce.

**Phase 5 — Criminal & traffic 🔵 planned, deliberately later.** Highest
raw court volume, but the lowest fit to Metis's core mechanic — most matters
are single-hearing with little to gather, and the UPL/rails risk profile is
materially different (urgency, different regulatory exposure) from
everything built so far. Worth doing once the platform and its rails
philosophy are proven, not first.

**Phase 6+ — Commercial, conveyancing, and others ⚪ vision.** Evaluate
against the same lens each time: does this matter type share the
"organise evidence, prepare documents" pain, or does it need a genuinely
different product?

---

## 5. Integration strategy

**LEAP first.** Rationale: avoid duplicate data entry for firms already
running LEAP as their practice-management system — Metis should feed a
firm's existing system, not compete with it.

**Current state:** 🟡 developer registration with LEAP's Marketplace program
is complete (submitted 2026-07-29, confirmation received). **No sync code
has been built yet** — this is a real gap between "registered as a
developer" and "integration exists." Next step, once prioritised: build
against LEAP's documented REST API for a working demo push (matter →
document → note).

Smokeball — 🔵 planned, gated behind their partner-application process
(not self-serve like LEAP), not yet submitted.

---

## 6. Architecture (what's actually running)

No rewrite. The current stack is right-sized for where the product actually
is — a modular monolith serving a small, real user base, not a platform
provisioned for "thousands of firms and millions of matters" that doesn't
exist yet.

- **Frontend:** React 19, TypeScript, Tailwind 4, tRPC 11 client
- **Backend:** Express 4, tRPC 11 (typed, no separate REST layer to
  maintain), Node.js
- **Database:** MySQL via Drizzle ORM
- **Storage:** Cloudflare R2 (`storagePut()`), never bytes in the DB
- **Auth:** magic-link (`server/magicAuth.ts`), sign-in gated by
  `ALLOWED_EMAILS` during early access
- **Email:** Resend
- **AI:** Anthropic Claude via `invokeLLM()` — provider-swappable at the
  call site already, no separate "AI Gateway" service needed at this scale
- **Hosting:** Fly.io, Sydney region (`syd`) — real AU data locality today,
  without needing an Enterprise-tier cloud data-residency product
- **CI:** GitHub Actions — typecheck + tests + build on every push

**What's genuinely missing, in priority order once there's demand for it:**
PDF text extraction/OCR (blocks chronology, asset schedules — see §3),
a bridge between the two matter/portal data models (§3), rate-limit/WAF
hardening tied to onboarding the first real paying client (already
decided — see `STATUS.md` 2026-07-27 security pass).

**Deliberately not doing, and why:** a rewrite to .NET/PostgreSQL/Azure —
the current stack works, is deployed, is tested, and a rewrite would trade
a working product for infrastructure nobody's using yet. Microservices,
an "Internal Developer Platform," a dedicated "AI Gateway" service, RBAC
across six roles — all real patterns, all premature for a modular monolith
with a handful of early-access users. Revisit if and when a specific,
felt scaling pain shows up, not on a five-year speculative timeline.

---

## 7. AI governance — already built, not aspirational

Generic AI-governance language ("transparency," "human oversight," "human
review before official record") is easy to write and hard to enforce. Metis
enforces its version in code, and it's already been tested against
adversarial cases:

- **Never claims detection it can't back.** A checklist filename match is a
  *suggestion the user confirms* — the pack says "confirmed by you," never
  "detected by Metis." Pinned by a test that was verified non-vacuous by
  injecting the regression.
- **Unreadable documents are reported as unreadable**, never silently
  treated as empty (`extractionStatus`).
- **No case-law citations, ever** — not even correct ones. Enforced via
  regex gate (`enforceRails()`, `server/routers/metis.ts`).
- **Generated legal wording carries a DRAFT banner.** The four LPUL s174
  client-rights statements are left as an explicit
  `[LAWYER TO CONFIRM EXACT WORDING]` placeholder rather than invented text
  — deliberately incomplete instead of plausibly wrong.
- **Domain-locked per matter.** The system prompt is generated from the
  matter's own title/description, not a shared prompt across matters.
- **Rate-limited and audited at the procedure layer**
  (`rateLimitedPublicProcedure`, `agreementGatedProcedure`).

This is the section of the original ChatGPT blueprint that was closest to
right in spirit — Metis just already has it built, tested, and verified
against real adversarial inputs, rather than as a future governance
framework to design.

---

## 8. Goals — near-term, not vanity metrics

Enterprise SaaS metrics (MRR, ARR, CAC, LTV, DAU/WAU) are premature for a
product with zero paying customers. The goals that actually matter right
now:

1. **Get real usage from real people on the client side** — Jacinta is
   using it; more early-access users are the actual validation signal, not
   a dashboard metric.
2. **Get a working solicitor to actually use Platform 2** — Simon has
   access and reacted well to the positioning; his read as a practising
   solicitor is worth more than any synthetic user-persona review.
3. **Clear the four Platform 2 gates** — lawyer review of generated
   templates, PI insurance, AU data-residency decision, ToS/privacy pass.
   None of these are code; all of them block real client data.
4. **One real LEAP integration demo** — proves the "avoid duplicate data
   entry" promise isn't just a roadmap line.
5. **A validated Phase 2 practice area** (wills & estates, most likely) —
   only after Phase 1 has real signal, not on a fixed calendar.

---

## 9. What this document deliberately doesn't do

It doesn't promise a timeline, a headcount plan, or a funding strategy —
none of that is real yet, and writing it down doesn't make it more real. It
doesn't claim Platform 3 exists. It doesn't claim LEAP sync exists. Every
🔵/⚪ item here is a direction, not a commitment — revisit this doc when the
product's actual state changes enough to make it stale, the same discipline
`STATUS.md` already follows.
