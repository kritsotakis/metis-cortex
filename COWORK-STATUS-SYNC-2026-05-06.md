# Cowork status sync — 2026-05-06 13:05

> **For:** Cowork
> **Summary:** Brand bundle complete. Some tasks in your previous briefs need updating. Three small new tasks added.

---

## What's changed since the previous two briefs were sent

You have two briefs from earlier today:
- `COWORK-CLOUDFLARE-MIGRATION.md` — gated on Peter's Phase 0
- `COWORK-INFRASTRUCTURE-SETUP.md` — partially executed (Tasks 3, 4, 5, 6 doc deliverables done in your output dir, then synced into repo by Code; Tasks 1, 2 still gated on Peter's auth)

Since then, **Manus delivered v1 + v2 + v3 of the brand bundle**, and Code has integrated everything. **The brand identity is now production-ready.** This changes a couple of things in the previous briefs.

---

## ⚠️ Update to Task 3 (LinkedIn company page) in `COWORK-INFRASTRUCTURE-SETUP.md`

The LinkedIn copy doc previously said *"use placeholder logo, render from app/icon.svg via npx svgexport"*. **That's now obsolete.**

**Replace those instructions with these:**

When Peter is ready to execute the LinkedIn page setup, he should use **`public/brand/social/linkedin-company-logo.png`** as the logo (Manus-rendered, 300×300, brand-aligned) instead of the placeholder svgexport approach.

**Cover banner:** previously said "hold until Manus delivers". Manus has delivered. Use **`public/brand/social/linkedin-company-cover.png`** (1128×191).

Update the existing `LINKEDIN-COMPANY-PAGE-COPY.md` in the repo root to reflect this — strike the placeholder render command, point to the two ready files.

---

## Brand bundle inventory (current state of repo)

Everything is at `~/Desktop/metis-cortex/public/brand/` and `public/icons/`:

```
public/
├── og.png                                          ← static OG image (Manus, used by Cloudflare migration)
├── icons/
│   ├── favicon-{16,16-simplified,32,48,64,128,256,512,1024}.png
├── brand/
│   ├── metiscortex-brand-guide.pdf                 ← 3-page brand guide (palette, type, lockup rules)
│   ├── metiscortex-wordmark.svg                    ← real-text SVG, navy bg
│   ├── metiscortex-wordmark-on-light.svg           ← real-text SVG, transparent bg, navy text
│   ├── metiscortex-horizontal-lockup.svg           ← hybrid SVG, dark variant
│   ├── metiscortex-horizontal-lockup-on-light.svg  ← hybrid SVG, light variant
│   ├── metiscortex-stacked-lockup.svg              ← hybrid SVG, dark variant
│   ├── metiscortex-stacked-lockup-on-light.svg     ← hybrid SVG, light variant
│   ├── metiscortex-mark.svg                        ← raster-wrapped, legacy (unused in code)
│   ├── metiscortex-mark-on-dark.svg                ← raster-wrapped, legacy
│   ├── metiscortex-mark-on-light.svg               ← raster-wrapped, legacy
│   ├── metiscortex-mark-transparent.png            ← clean transparent PNG, 1024x1024
│   ├── logo-mark-128.png                           ← navy-bg PNG, 128x128 (used by Hero)
│   ├── logo-mark-transparent-128.png               ← transparent PNG, 128x128 (used by Footer)
│   └── social/
│       ├── linkedin-personal-cover.png             ← 1584x396
│       ├── linkedin-company-cover.png              ← 1128x191
│       ├── linkedin-company-logo.png               ← 300x300
│       ├── twitter-header.png                      ← 1500x500
│       ├── twitter-avatar.png                      ← 400x400
│       ├── youtube-banner.png                      ← 2560x1440
│       └── youtube-avatar.png                      ← 800x800

src/app/
├── icon.svg                                        ← hand-coded "M+dot" — primary favicon
├── icon-16.svg                                     ← simplified for icon-generator script
└── apple-icon.png                                  ← Manus 256x256, auto-discovered
```

## Hero/Footer integration done by Code

- `Hero.tsx` — 40×40 mark using `/brand/logo-mark-128.png` (navy bg, blends into Hero's navy)
- `Footer.tsx` — 40×40 mark using `/brand/logo-mark-transparent-128.png` (transparent, sits cleanly on bone bg)

You don't need to touch these. They're working as intended.

---

## Three new small tasks for Cowork

### Task 7 — Update memory files with v3 brand state

**Why:** `~/.claude/memory/active-projects.md` Metis Cortex row was last updated when the brand was at "site built, awaiting hosting." It needs to reflect the current state.

**Steps:**

1. Read `~/.claude/memory/active-projects.md`. Find the Metis Cortex row.
2. Update the **Status** cell to add: *"Brand bundle v3 integrated — full set of dark + light SVG lockups, transparent mark, brand guide PDF, social kit (7 platforms), favicon ladder. Hero + Footer use brand mark inline."*
3. Update the **Next Step** cell — add the LinkedIn page setup item now that real logo + cover are available.
4. Append a new dated entry to `~/.claude/memory/recent-activity.md` covering today's brand work — three Manus iterations (v1 raster, v2 vector text, v3 light variants + brand guide), what was integrated, file structure.
5. Update `~/.claude/projects/-Users-kritsotakis/memory/project_metis_cortex.md` — mark brand bundle as complete, document the file structure.

**Timebox:** 15 min.

### Task 8 — LinkedIn first-100 outreach list

**Why:** Once the LinkedIn company page is live, Peter has a 30-day window to invite 100 first-degree connections to follow it (LinkedIn cap: 250 invites/month per admin). Choosing well matters — the first 100 followers shape the page's reach algorithm.

**Steps:**

1. Cowork drafts criteria for who to invite from Peter's existing LinkedIn first-degree network:
   - Service business owners (cleaners, tradies, real estate, dental, allied health, aesthetic clinics) — primary ICP
   - Sydney-based small business operators — most likely to convert
   - Founders / operators (decision-makers) — not employees of big companies
   - Avoid: agencies and consultants (competitor adjacency, low ICP value), recruiters (spam invites in their feed dilute brand), random connections from years ago who may have moved on
2. Cowork writes a 6-line invite-blurb Peter can use as the LinkedIn invite custom note (LinkedIn allows ~300 chars on follow-page invites):
   ```
   I just launched Metis Cortex — done-for-you AI receptionists for Australian service businesses. Built and proven on my own cleaning business (DSK). If missed calls are a real number for your business or you know someone who'd find it useful, would mean a lot if you'd follow the page.
   ```
   (Tweak as needed. Don't make it sales-y. Founder-to-peer tone.)
3. Save to `~/Desktop/metis-cortex/LINKEDIN-FIRST-100-OUTREACH.md` with criteria + invite blurb + a checklist Peter can use to track who he's invited.

**Timebox:** 30 min.

### Task 9 — Cold-email V1 prospect list prep (research only, do NOT send)

**Why:** When the DSK pilot data lands (~2 weeks after Day 14 of the install), Peter needs a ready prospect list to send the first cold-email batch to. Building it now means zero delay between case study landing and outreach starting. Building it after means a week's lag.

**Scope:**

1. Cowork compiles a list of **50 Sydney service businesses** matching Metis Cortex ICP:
   - 10 property cleaning companies (other than DSK obviously)
   - 10 trades (plumbers, electricians, builders, painters)
   - 10 real estate agencies (small / boutique, not Belle/Ray White corporate)
   - 10 aesthetic / beauty clinics (other than Eonia)
   - 10 allied health / dental / physio practices
2. For each: business name, owner/manager name, public email, public phone, website, suburb, **why they're likely a good fit** (1 sentence). Sources: Google Maps, public directories, LinkedIn (don't pull from LinkedIn DMs / private data).
3. Save to `~/Desktop/metis-cortex/COLD-EMAIL-V1-PROSPECTS.md` with rows clearly tagged by vertical.
4. **DO NOT send any emails.** This is research only. Peter sends manually after pilot data lands.

**Filtering rules:**

- ✅ Solo or small team (1–10 employees) — owner-operator decision-maker
- ✅ Phone number prominently on website (means phone-driven leads)
- ✅ Last website update visible within 12 months (active business)
- ❌ Big franchises (corporate, won't have buying authority at owner level)
- ❌ Anyone in Peter's existing personal network — those are warm intros, not cold
- ❌ Anyone who explicitly says "no spam / no solicitation" on their contact page — respect it

**Timebox:** 90 min for the full 50.

---

## Sequencing

| Task | Order | Blocker |
|---|---|---|
| Phase 0 (Cloudflare gates) | First | Peter |
| LinkedIn company page execute (now with real assets) | Second | Peter (after Task 7 update) |
| Task 7 (memory update) | Anytime | None — Cowork can do now |
| Task 8 (outreach list) | After LinkedIn page live | None for prep |
| Task 9 (cold email prospects) | Anytime | None — Cowork can do now |
| Cloudflare migration Phase 1 | After Phase 0 | Peter's GitHub repo |

**You can run Tasks 7 and 9 right now without any auth or filesystem dependency** (Task 7 is in `~/.claude/memory/`, Task 9 is research). Task 8 you can prep but not execute until LinkedIn is live.

---

## What Cowork must NOT do (still in force from previous briefs)

- No code touches in `~/Desktop/metis-cortex/src/` — Code's lane
- No git pushes — coordinated via Cloudflare brief
- No actual sending of cold emails or LinkedIn invites — research and prep only
- No domain registrations without explicit approval
- No engaging lawyers or signing anything
- No deletion of legacy raster-wrapped mark SVGs from `public/brand/` — they're brand assets even if unused in code

---

## Confirmation Cowork posts back

```
✅ Task 7 — memory files updated, dated entry in recent-activity.md, project memory refreshed
✅ Task 8 — LinkedIn first-100 outreach list at LINKEDIN-FIRST-100-OUTREACH.md
✅ Task 9 — 50 prospects across 5 verticals at COLD-EMAIL-V1-PROSPECTS.md
```

Then ping Peter with the three file paths.
