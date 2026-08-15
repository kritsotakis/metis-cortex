# Metis Cortex × LEAP — Integration Scoping Brief (2026-08-10)

Prepared after John's demo validated "LEAP connect" demand. Every claim sourced;
gated/unverifiable items marked. Full sources at bottom of each section in the
research transcript; headline facts:

## The shape of it
- LEAP has a real developer program: register free at console.leap.build →
  "Pre-approvals" vetting → build against a LOGIN-GATED API reference →
  Security & Compliance Review → App Review → Marketplace listing.
  Fees, review timeline and API schema are all partner-gated (UNVERIFIED).
- Marketplace precedent that matters: **Settify** (family-law intake — the
  closest analogue to Metis) has a full integration that creates pre-populated
  LEAP matters... and LEAP then bundled it into their own subscription. LEAP
  builds or absorbs family-law tooling (Balance Sheet+, "AI Paralegal").
  A native integration validates Metis AND exposes it.
- Even established dictation vendors (Philips SpeechLive) have NOT shipped a
  native LEAP app — they service LEAP firms via email/IT-configured workflows.

## The plan
**Phase 0 — this week, $0, no permission needed: "Email-to-LEAP".**
A per-session "Send to LEAP" button that emails the file note / brief / costs
PDF to a firm-nominated address, subject `[<LEAP matter no>] Metis file note —
<client> — <date>`. Staff files it with LEAP's own Outlook "Save to Matter"
add-in in one click. Honestly marketable as "works with LEAP" — it is exactly
how existing vendors service LEAP firms.

**Phase 1 — parallel, free: register at console.leap.build.** The only way to
see the real API surface, fees and review criteria. v1 native target: push a
document + time entry into an EXISTING matter (Settify in reverse). Do NOT
scope matter creation, billing sync or trust accounting.

**Phase 2 — only after a 2nd/3rd firm asks:** Marketplace Connector App.

## For the office-manager meeting
"Metis works with LEAP today — after every conference the file note and costs
disclosure arrive as a PDF email addressed with your LEAP matter number, and
whoever does your filing saves it with the normal Save-to-Matter button. One
click, nothing new to learn, no IT project. We're also on LEAP's developer
program; the next version files it automatically, and you'd be the design
partner shaping it. Your data stays in Australia — we host in Sydney, LEAP's
cloud is AWS Sydney."

## Risks
(a) LEAP's terms/fees/timeline are gated — Pre-approvals may say no or slow.
(b) LEAP absorbs successful family-law partners — plan for it.
(c) Never say "native LEAP integration" in sales material until credentials
    are actually granted. "Works with LEAP" (email workflow) is the honest
    claim today.
