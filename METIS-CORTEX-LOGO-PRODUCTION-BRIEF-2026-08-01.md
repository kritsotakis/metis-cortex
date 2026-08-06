# Metis Cortex — Logo & Brand Asset Production Brief

**Prepared:** 1 August 2026, for handoff to a design tool (ChatGPT/image generation) to produce final,
deployable brand assets. Everything below is checked against the real live site and codebase, not
assumed — use it as-is rather than re-deriving specs from scratch.

---

## 1. What Metis Cortex is

Australian family-law legal-technology product, positioned as a solicitor's **"second chair"** for
client conferences, with a client-facing document-organiser product live today. Premium, trustworthy,
calm, discreet, professionally credible — not a consumer startup, not a generic SaaS tool.

**Name meaning (the identity should connect to this):**
- **Metis** — wisdom, skill, strategic intelligence, foresight, good counsel, in ancient Greek thought
  and mythology. Metis was the mother of Athena.
- **Cortex** — reasoning, language, judgment, intelligent processing.
- Intended idea: **strategic wisdom powered by an intelligent mind.**

---

## 2. Decision: replace the current mark

The current mark (`current_favicon_cortex_mark.png` in the earlier review pack — an organic
brain/fingerprint-style swirl of thin navy lines with one gold thread) is being retired. It looks
elegant at large size but fails the only test that actually matters day to day: at the 16–32px sizes
it's actually used at (browser tab, nav bar), the fine parallel lines collapse into an unreadable grey
smudge. It also risks reading ambiguously as floral or anatomical rather than "intelligent reasoning."

**Selected direction: W2** — an abstract mark built from two facing crescent/wing shapes forming an
"M," with a solid gold circle at the point where they nearly meet (see the review pack's
`06_Abstract_wisdom_options_W1-W3_recovered.png`, third-from-right position, labelled W2). Chosen over
the other 8 concepts reviewed (Athena/helmet, owl, laurel-wreath-monogram, single-eye, full owl body,
labyrinth, and two earlier gold-thread M/pathway concepts) because it's the only concept that is
simultaneously: distinctive, legible at favicon size (thick solid shapes, real negative space — no fine
linework to blur out), on-brand (M initial + a single point of gold "wise counsel"), and carries zero
risk of the associations below.

**Backup direction, worth a real side-by-side before final lock-in: O1** — a bold owl-face mark (owl =
Athena's own bird, the most literal wisdom symbol available) from `05_Owl_options_O1-O3.png`, leftmost
position. Same small-size legibility strength as W2, more literal/tellable in marketing copy. Neither
W2 nor O1 has yet been mocked up with the actual wordmark — do that before finalizing either.

### Explicitly rejected — do not revisit these directions

- **Any gold line/thread running through or across the mark at an angle** (the two earlier "M/pathway"
  concepts, and to a lesser extent the supplemental M-monogram lockup) — already vetoed once for
  reading like a stock-chart line or finance-app icon. Peter has explicitly rejected trading-chart and
  finance-brand associations; treat this as a hard constraint, not a style preference.
- **Single stylised eye** (O2) — risks an "all-seeing / surveillance" association, a genuinely bad fit
  for a product handling family-violence-adjacent, high-sensitivity matters.
- **Laurel wreath + circular monogram** (A3) — the single most saturated cliché in law-firm/professional-
  services branding; reads as generic "firm crest," not as this brand specifically.
- **Spartan/Corinthian helmet** (A1) — on-theme for Athena, but a war helmet risks a combative read
  rather than calm and trustworthy, and is heavily saturated in sports/esports branding specifically.
- **Full illustrated owl body** (O3) — competently drawn but the register is wrong; reads closer to a
  children's or conservation-org brand than a premium legal tool.
- Generic AI circuitry, crypto styling, medical-looking brain imagery, gavels, scales, religious or
  institutional-seal imagery, anything political.

---

## 3. Existing brand system to preserve

**Palette (exact hex, already live across the site — keep unless there's a compelling reason to
refine):**
- Deep navy `#0f1e3d` — primary
- Warm gold `#c9a84c` — accent
- Warm cream `#f5f0e8` — background

**Typography (already live, keep):**
- Playfair Display — headings and the "METIS" wordmark (serif, authoritative)
- Inter — body text

**Current wordmark lockup structure** (`client/src/components/Logo.tsx`), for reference — the new mark
should slot into the same two-tone lockup pattern, not force a redesign of the type treatment:
- Mark image, sized ~36×36px inline, to the left
- "METIS" stacked above "CORTEX": METIS in Playfair Display, `tracking-[0.12em]`, navy on light
  backgrounds / white on dark; CORTEX below it in a smaller size, `tracking-[0.32em]` (wide letter-
  spacing), gold `#c9a84c`, on both backgrounds

**Two-tone requirement (already how the current mark works, keep this pattern):** the mark needs a
navy/gold version for light (cream) backgrounds and a white/gold version for dark (navy) backgrounds —
both are used live throughout the app, not just the homepage.

---

## 4. Exact technical specs to hit (checked against the live codebase, not generic defaults)

- **Favicon:** currently a single 1005KB PNG at `/favicon.png` — oversized and not a real favicon set.
  Needs a proper multi-resolution set: 16×16, 32×32, 48×48, plus a 180×180 `apple-touch-icon` and a
  512×512 for PWA/Android home-screen use. Test the mark at all of these, not just 32px.
- **Open Graph / social share image:** `/og.png`, exactly **1200×630px**, referenced via `og:image`,
  `og:image:width`, `og:image:height`, and `twitter:image` in `client/index.html`. Needs the full
  wordmark lockup, not just the mark, since this is what renders when a link is shared to Slack, email,
  LinkedIn, iMessage, etc.
- **In-app mark usage:** currently imported as `mark.png` / `mark-on-dark.png` (transparent PNG,
  square-ish crop, used at roughly 36×36px in the nav) and `horizontal-light.png` / `horizontal-dark.png`
  / `stacked-light.png` / `stacked-dark.png` (full wordmark lockups, used across the solicitor-side
  dashboard pages). The new asset set needs to replace all of these 1:1 — same variant names, same
  transparent-background PNG format, same rough aspect ratios — so the swap is a drop-in file
  replacement, not a code change.
- **No social accounts are live yet** (no Twitter/X, LinkedIn, Instagram, or Facebook links currently
  on the site) — so there's no existing profile-picture crop to match, but produce the standard set
  below anyway since accounts are likely to launch alongside the new mark.

---

## 5. Deliverables to request

1. **Master vector artwork** — clean, optically balanced SVG of the final mark, redrawn properly (the
   AI-generated concept PNGs are references only, not production geometry — do not trace or
   auto-vectorize them directly).
2. **Outlined/stroke version** of the SVG, for single-colour or engraving-style use.
3. **Two-tone mark variants** — navy/gold (light backgrounds) and white/gold (dark backgrounds) — as
   transparent PNGs at minimum 512×512, plus the master SVG.
4. **Wordmark lockups** — horizontal (mark beside "METIS CORTEX") and stacked (mark above "METIS
   CORTEX"), each in both light and dark variants — matching the existing four-file naming pattern
   (`horizontal-light`, `horizontal-dark`, `stacked-light`, `stacked-dark`).
5. **Symbol-only variant** — mark with no wordmark, for contexts too small for text (app icon, favicon).
6. **Favicon set** — 16, 32, 48, 180 (apple-touch-icon), 512px, generated from the symbol-only variant
   and visually checked at each size, not just scaled down mechanically.
7. **Social preview / OG artwork** — 1200×630px, full wordmark lockup composed on-brand, ready to drop
   in at `/og.png`.
8. **Social profile-picture crops** — square 1:1 (works for X/Twitter, Facebook, Instagram) and circular-
   safe-area version (LinkedIn crops to a circle — keep the mark inside the safe circular area of the
   square canvas), symbol-only, at 512×512 minimum.
9. **Safe-space and minimum-size rules** — documented clear-space margin around the mark, and the
   smallest size at which it may be reproduced.
10. **Colour values** — confirm the three hex values above (or refined versions) as the final locked
    palette, plus any tint/shade variants needed for the wordmark-on-navy vs wordmark-on-cream cases.
11. **Accessibility check** — contrast ratios for gold-on-navy and navy-on-cream text usage, since the
    wordmark's "CORTEX" line is small and gold-on-light-background specifically.

---

## 6. Before anything ships

- Mock up the selected mark (W2, and ideally O1 as a real comparison) with the actual "METIS CORTEX"
  wordmark in both lockup orientations — this hasn't been done yet for either concept.
- Test the final symbol at 16, 24, 32, and 48px, in one colour, and reversed on navy — not just at
  the size it was generated at.
- Run a basic similarity/conflict screen before treating any direction as final (preliminary screening
  only, not legal trademark clearance).
- Once approved, replace the seven existing files in `client/src/assets/brand/` 1:1 and `/favicon.png`
  + `/og.png` in `client/public/` — no code changes needed if the new files use the same names and
  roughly the same aspect ratios as what they're replacing.
