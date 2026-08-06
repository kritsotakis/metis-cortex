# Monday 10:30 — John. How to open.

One page. Read it in the car. Built around what John actually told you, not what
we assumed for the last six weeks.

---

## What you now know about him

1. **He never ignored you.** He wasn't sure the emails were real.
2. **He hates AI for legal work.** He volunteered that.
3. **You said "it always goes to a solicitor." He said "that's good."**

Point 3 is the entire meeting. You already found the message — don't leave it
behind and go back to pitching features.

---

## Open with the liability, not the software

Don't start with what Metis does. Start with the thing he lives with:

> "The reason I built it is the 'you never told me that' conversation. That's
> the one that ends up in a complaint, and it turns on whether the file note
> recorded the risk you warned about and what the client said back."

That's *Sewell v Zelden* territory and he'll know it immediately. You're opening
on his risk, not your product. Then:

> "So the software won't produce a file note at all unless both of those are in
> it. And if they weren't said in the conference, it writes that they weren't —
> it doesn't fill the gap."

**Stop there and let him react.** That single behaviour is the whole pitch.

---

## Lead with the three refusals

If the word "AI" comes up before these do, you've lost the frame. Say these
first, in this order:

1. **It won't write the statutory wording.** The four s174 client-rights
   statements generate as a visible blank — `[LAWYER TO CONFIRM EXACT WORDING]`
   — because a non-compliant disclosure voids the costs agreement and blocks fee
   recovery under s178. *"I'd rather hand you something obviously unfinished
   than something plausibly wrong."*
2. **Nothing reaches a client until a solicitor clicks approve.** The draft is
   invisible to the client until a human signs off. No auto-send, anywhere.
3. **It never sets a number.** The solicitor enters every fee and estimate. The
   software only computes which disclosure tier that triggers.

Plus, when it fits: two of the five compliance artefacts involve **no AI at
all** — the conflict check and the client ID record are just dated facts.

---

## When AI does come up — and it will

Don't get defensive, and don't oversell. The honest line:

> "It drafts. It doesn't decide, and it doesn't send. Every output lands in
> front of you marked as a draft, and the ones that carry real legal weight
> either won't generate without your input or leave the wording blank for you.
> If you think the drafting itself is the wrong idea for this, that's exactly
> what I want to hear from you today."

Inviting the objection is stronger than defending against it. He already told
you his prior — pretending you didn't hear it will read as a sales job.

Also true and worth saying unprompted, because he'll find it in the pack anyway:
**AI processing happens overseas (Anthropic), and that's disclosed.** Hosting is
Sydney.

---

## ⚠️ On showing the video

The capabilities video is **narrated by a synthetic voice, over a synthetic
client conference in two more synthetic voices.** For a man who just said he
hates AI for this work, that may undercut everything above.

**Recommendation: don't play it.** Use the silent cut and talk over it yourself,
or better, just drive the live product for two minutes. Keep the narrated
version for firms who haven't told you their priors.

If you do show something, show **the checklist** — it's the least AI-feeling
part of the product and the most obviously useful.

---

## If he asks "is it ready?"

Don't claim it's finished. The stronger answer:

> "It's built and it runs — you're watching production. It's not open to firms,
> because the costs-disclosure wording needs a solicitor's sign-off before it
> goes near a real client. That's the main reason I'm here."

Four things gate real client use and **none of them are code**:
1. Lawyer review of the generated wording ← this is him
2. Professional indemnity insurance — not in force
3. AU data residency — formal pass not done (Fly Sydney satisfies it in practice)
4. ToS / privacy lawyer pass

Also true if it comes up: **no real conference has ever been recorded through
it**, and the client side and solicitor side are still separate data models.

---

## The ask — don't leave without it

**A price and a timeframe to review the five artefacts.**

The pack is `METIS-LAWYER-REVIEW-PACK-2026-08-01.md` — five artefacts, each
showing the exact prompt used, each with a tick-box: approved / approved with
changes / not yet safe. It's built to produce decisions, not commentary.

Win condition: **a number and a date.** Not "send it through and I'll look."

If you get that, everything else on this page is upside.

---

## His firm runs LEAP — confirmed. Use it, carefully.

This is the strongest card in the meeting, and the easiest one to overplay.

**Why it matters to him:** the integration would push the finished file note and
brief straight into the right LEAP matter, so nobody in his office re-keys it.
That's a concrete benefit to *his* firm, not an abstract capability. Say it as a
question, not a claim:

> "Your file notes end up in LEAP anyway — how much of that is someone
> re-typing it?"

**Why it matters to you:** our LEAP developer registration has been stalled
since 29 July on their question about mutual clients. A LEAP-using design
partner answers it.

### The line you must not cross

LEAP asked about **mutual clients**. That means a firm actually *using Metis*.

- John agreeing to **review the wording for a fee** → he is a *supplier*. This
  does **not** make his firm a mutual client. Do not tell LEAP it does.
- John's firm agreeing to **pilot Metis**, even informally → that *is* a real
  answer to LEAP's question, and only with his express permission to be named.

LEAP can and will verify. Overstating this once would cost the integration and
the relationship. If Monday only produces a paid review, LEAP simply gets the
honest answer it was always getting — no names yet.

### The second ask, if the meeting goes well

> "There's one other thing. LEAP have my developer registration on hold until I
> can point to a firm that uses both. If you ever did trial this properly, would
> you be open to me naming the firm to them? Not today — only if you actually
> use it and you're happy to."

Ask it **after** the review ask, not instead of it. And take a no cleanly.

---

## Know the firm before you walk in (teardown, 2026-08-07)

Full report: `KONSTAN-LAWYERS-TEARDOWN-2026-08-07.md`. The load-bearing facts:

- **They have no working website.** konstanlawyers.com.au has been a parked
  domain since 2018; every directory points at the dead URL. Metis's client
  portal would be their first real digital client experience — that's the
  frame, not "another tool."
- **Their headline practice is CRIMINAL law** (+ conveyancing, PI,
  construction). **Family law is not on their public list.** So ask early:
  *"What's the actual split of your caseload?"* and *"Is family law your
  caseload, John, or the firm's?"* If family is thin for them, the roadmap
  conversation shifts: criminal-conference tool first (their #1 fit —
  conference → file note → brief-to-counsel IS criminal practice), and a
  conveyancing document-collection module on the client side.
- **Small Greek-bilingual shop in Marrickville** — two solicitors found (Simon
  Konstantinidis, principal; John). Zero IT overhead is mandatory, and
  Greek-language client prompts would be a genuine differentiator. You're
  Greek-Australian; use that.
- **Their Google reviews (3.9★, unclaimed, one nasty complaint unanswered)** —
  offering to help claim and tidy that profile is an hour of goodwill.
- **Verify LEAP version** — cloud or desktop changes what "integration" means.

## The other question to ask him

**"How should I have reached you?"** He already told you: call, don't email. Now
ask what a credible first approach from a stranger actually looks like to a
solicitor. That answer is worth the meeting on its own — it fixes every outreach
attempt after this one, and there are 25–30 of them queued.

---

## Don't say

- "AI-powered" anything
- "Saves you hours" — he hasn't agreed he has a problem yet
- "Integrates with LEAP" — **it does not.** Registration is in progress and
  nothing is built.
- Any claim that a real client has used it. None has.
