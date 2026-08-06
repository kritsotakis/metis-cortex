# Metis Cortex — External Review Brief (for Manus · Gemini · ChatGPT)

**From:** Peter Kritsotakis
**Date:** 2026-05-29
**Ask:** Be a skeptical reviewer. Poke holes. I'd rather hear the problem now than after I've spent weeks. Review (1) the live site, (2) the positioning/strategy, (3) the go-to-market + validation plan. Tell me what's weak, what's missing, and what you'd change.

**Live site to review:** https://metiscortex.au

---

## What Metis Cortex is (current direction)
An AI "second chair" for **Australian legal practice, specialising in family law.** A solicitor records the client conference; Metis Cortex transcribes it (speaker-labelled), detects the legal issues, searches Australian case law live (AustLII), and drafts the **file note, case brief and client proposal** before the solicitor leaves the room — **the solicitor reviews and signs off on everything.** Roadmap adds the compliance artefacts a real conference produces (costs disclosure, conflict check, client ID, engagement letter).

It was built end-to-end (React + tRPC + Express + MySQL, AI pipeline) and migrated onto our own stack. A static marketing site is live; the full interactive product is built but not yet publicly deployed.

## Key strategic decisions already made (challenge any of them)
1. **Beachhead = NSW family-law sole/micro practitioners.** Chosen for founder-credibility fit: Peter has lived family-law experience (his own divorce/custody + a DPO matter). The unfair advantage is being a credible insider, not domain-novel tech.
2. **Integrate, don't replace.** LEAP and Smokeball dominate AU legal practice-management (trust accounting, billing, FCFCOA forms, 3-yr contracts). Verified on their own product pages: **neither records/transcribes a live in-person client conference or drafts a file note from the spoken meeting** — their AI reasons over content already typed into the matter. So Metis sits *upstream* — capture the conference, push a clean file note + drafts *into* their LEAP/Smokeball matter. We are not trying to replace the practice-management system.
3. **The wedge value props:** (a) live consult capture + family-law-tuned structuring; (b) first-conference one-pass drafting (incl. costs disclosure + advice letter); (c) compliance-grade consent + provenance.
4. **The crux risk = client-consent to record.** The consult-to-document seam is open partly *because* recording client conversations carries ethics/consent friction. This is both the moat (if nailed) and the #1 adoption blocker (if not). Reframe being tested: recording as *mutual protection* — a complete, consented record that protects the solicitor (defensible file note, ends "you never told me that" disputes) and the client. Validating this with solicitors is the make-or-break.
5. **Validate before building more.** We're running ~10 Mom-Test conversations (warm first, then cold to 14 Law Society NSW Accredited Specialists) before building the compliance engine. The costs-disclosure document is gated on a **lawyer review** (LPUL s178: a non-compliant disclosure voids the costs agreement + blocks fee recovery — getting it wrong is worse than not having it).
6. **Current-law discipline:** the legal knowledge base + site were corrected to post-2024 parenting reforms (no ESPR presumption / equal-time; simplified s60CC) and post-June-2025 property reforms (codified 4-step, economic effect of family violence, disclosure duty s71B/s90RI).

## Competitive context
- **LEAP** (~A$339-389/user/mo, Matter AI), **Smokeball** (A$49-239/user/mo, Archie AI) — dominant, sticky, strong family-law *forms*, but no live-conference capture.
- AI legal-scribe / note tools exist but few are AU-family-law-specific + integrated-beside-PMS.
- Adjacent: psychology/clinical AI-scribe market is far more contested (Heidi, an AU unicorn) — we deliberately narrowed OFF that to legal/family-law.

## What I want you to pressure-test
1. **Positioning** — is "second chair for family-law conferences, feeds your LEAP/Smokeball matter" sharp and credible, or still too broad/soft? Does the live site land it?
2. **The seam thesis** — is "live consult capture → drafted file note/costs disclosure" a real, defensible wedge, or will LEAP/Smokeball simply add it? How durable is the moat?
3. **The recording/consent risk** — is this fatal? What would make AU family-law solicitors actually record client conferences (or refuse)? Are there privilege/ethics landmines we're underestimating?
4. **Costs-disclosure feature** — smart wedge or dangerous liability to automate? How would you de-risk it beyond "lawyer review"?
5. **Go-to-market** — is the warm-first → cold-Accredited-Specialists Mom-Test plan sound? Is founder-credibility enough to get the first 5 paying customers, or what's missing?
6. **What have we missed entirely** — a bigger risk, a better wedge, a faster path, or a reason to stop?

Please be specific and blunt. Rank your top 3 concerns. Tell me what you'd do differently.
