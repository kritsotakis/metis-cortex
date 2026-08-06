# Metis Cortex — Client Acquisition: Content Plan + Outreach List

**Date:** 2026-07-31
**Source:** Real search-intent and referral-channel research (WebSearch, sourced) — see
chat log 2026-07-31 for the full synthesis. This doc is the actionable output: a first
batch of blog titles and a named list of NSW orgs to actually contact.

---

## Part 1 — First batch of blog posts

Each title is pulled from a real query pattern found in research, mapped to a matter
type that **already has a live checklist template** — so every post can end with a
direct "start your [X] checklist" CTA, not a generic sign-up link. Ordered roughly by
how directly each maps to something Metis already does well.

### Parenting
1. **"What documents do you actually need for a parenting matter in Australia?"**
   Query: *what documents do I need for parenting orders*. Direct lift from the live
   `PARENTING` template — this post basically writes itself from existing content.
2. **"Do you need a Section 60I certificate before applying for parenting orders?"**
   Query: *s60I certificate family court*. High-value — this is "the strictest gate on
   a parenting filing" per the template's own notes, and most people don't know it
   exists until a registry rejects their filing.
3. **"Can you represent yourself in a parenting matter?"**
   Query: *self-represented litigant family court*. Speaks directly to the addressable
   population (20–30% of matters involve a self-rep party).

### Property settlement
4. **"The 4-step process for property settlement in Australia, explained"**
   Query: *how does property settlement work*. Grounds the post in the real s79
   framework (already cited in `legalKnowledge.ts`), not generic advice.
5. **"How is superannuation split in an Australian divorce?"**
   Query: *how is super split in a divorce*. One of the most common long-tail
   questions found in research.
6. **"Property settlement checklist: what to gather before you see a solicitor"**
   Direct lift from the new `PROPERTY_SETTLEMENT` template — leads with the
   separation-date-vs-today valuation point, since that's the specific gap Peter hit
   himself and a genuinely non-obvious requirement.

### Divorce / separation
7. **"How to apply for a divorce in Australia: the 12-month separation rule"**
   Query: *12 months separation divorce Australia*.
8. **"Separated but still living together? What the court needs to know"**
   Query: *separated under one roof*. Niche, underserved query — most divorce content
   skips this, and it maps to a real, specific requirement (a statutory declaration)
   in the new `DIVORCE_SEPARATION` template.
9. **"Divorce checklist Australia: what you need before you apply"**

### Child support
10. **"How is child support calculated in Australia?"**
    Query: *how is child support calculated*. High search volume, direct match to
    `CHILD_SUPPORT_ASSESSMENT`'s care-percentage-and-income framing.
11. **"What is a Departure Prohibition Order, and how do you respond to one?"**
    Query: *departure prohibition order child support*. Narrow but high-intent — very
    little good content exists here, and it's a direct match to `CHILD_SUPPORT_STAY`.

### Family violence
12. **"Only police can apply for an AVO to protect a child — here's what that means"**
    This is the single most differentiated post in the batch — it's the specific,
    non-obvious nuance found while researching the `FAMILY_VIOLENCE` template this
    session, and it's not well-covered anywhere else that came up in research.
13. **"How to apply for an AVO in NSW: what to gather before you start"**
    Query: *how to apply for an AVO NSW*.

### General
14. **"What to bring to your first family lawyer appointment"**
    Direct lift from `INITIAL_CONSULT` — the lowest-effort, most matter-agnostic post,
    good as an evergreen anchor page other posts can link to.

**Why this batch specifically:** every title maps to informational/preparatory search
intent (the underserved bucket — law firms chase transactional intent like "divorce
lawyer near me" instead), and every post can be written largely from content that
already exists in `server/matterTemplates.ts` and `server/legalKnowledge.ts` rather
than needing fresh research.

---

## Part 2 — Referral outreach list (NSW)

Self-represented litigants already show up at these organisations. None of them
currently have a document-organising tool to hand out — that's the actual opening,
not competing for search traffic against law firms.

| Organisation | Why | Contact |
|---|---|---|
| **Community Legal Centres NSW** (peak body) | One relationship here could open doors to some of the 32 funded CLCs in NSW at once — worth approaching first. | clcnsw.org.au |
| **Women's Legal Service NSW** | Specialist family law + DV service for women across NSW — directly serves a large share of Metis's stated audience. | wlsnsw.org.au |
| **Redfern Legal Centre** | Established, well-known generalist CLC with a family law practice. | (02) 9698 7277 · info@rlc.org.au |
| **Marrickville Legal Centre** | Runs a Family Violence Prevention Legal Service. | (02) 9559 2899 |
| **Wirringa Baiya Aboriginal Women's Legal Centre** | Family law, DV, parenting — specifically for Aboriginal and Torres Strait Islander women in NSW. | 1800 686 587 |
| **Hunter Community Legal Centre** | Runs the duty solicitor service at the Newcastle Family Court registry — literally in the room with self-rep litigants. | hunterclc.org.au |
| **Legal Aid NSW — Family Advocacy Support Service (FASS)** | Government referral pathway specifically for family law + DV matters. | via legalaid.nsw.gov.au |
| **Relationships Australia NSW** | Runs FDR/mediation services — clients here are actively gathering documents, same incentive alignment as any FDR practitioner. | relationshipsnsw.org.au |

**Suggested opening message (adapt per org):**

> Hi [name], I've built a free tool called Metis that helps people gather the right
> documents for their family law matter — parenting, property, divorce, child support
> or family violence — before they see a solicitor or attend mediation. It's not legal
> advice, just an organiser: a document checklist tailored to their matter type, with
> plain-English explanations of why each item matters. Since your clients are often
> self-representing or preparing for a first appointment, I thought it might be useful
> to have on hand. Happy to walk you through it — [link].

**Not pursued this pass, flagged for later:** individual private FDR/mediation
practitioners (the Attorney-General's Family Dispute Resolution Register lists
accredited practitioners publicly — a real channel, just needs its own scoped outreach
list rather than bundling here) and Amica/National Legal Aid (worth a direct approach
about a reciprocal listing, but that's a different kind of conversation — a
partnership pitch, not a referral ask — and deserves its own message).

---

## Explicitly deferred from this research

- **Reddit (r/AusLegal) and NSW-specific Facebook separation/parenting groups** —
  plausible channels, genuinely unverified. Reddit was blocked from browser access
  this session; this needs a manual look, not another research pass.
- **Paid Google Ads** — actively avoid for now. $8–100+ CPC in the most expensive ad
  vertical in Australia; revisit only once there's a paying funnel and real LTV data.
