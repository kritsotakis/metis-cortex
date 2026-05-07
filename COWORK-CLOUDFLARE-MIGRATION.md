# Cowork brief — Migrate Metis Cortex hosting to Cloudflare Pages

> **Owner:** Peter Kritsotakis
> **Assigned:** Cowork
> **Repo:** `~/Desktop/metis-cortex`
> **Status when written:** Next.js 16.2.4 site fully built locally, no remote yet. Brand/domain edits already applied to `.au` canonical, ink `#0e1e2e`, bronze `#b07843`. Uncommitted modifications present (see `git status`).
> **Authored by:** Claude Code, 2026-05-06

---

## Goal in one sentence

Move the Metis Cortex marketing site from "built but unhosted" to "live at `https://metiscortex.au` on Cloudflare Pages, auto-deploying on every push to GitHub `main`".

## Why Cloudflare Pages + static export (not Workers + adapter)

The site is a single static page with no server-side features (no auth, no API routes, no ISR, no dynamic data). For this shape:

- **Pages + static export** = Git integration, automatic builds, zero secrets in chat, $0/month, deploys in ~90 seconds. ✅
- **Workers + `@opennextjs/cloudflare` adapter** = needs an API token in chat OR GitHub Actions secret, more moving parts, only worth the complexity if Phase 2 adds server actions/ISR/API routes.

We're picking Pages now. If Phase 2 needs Workers features, the migration to OpenNext is a one-evening job — revert `output: 'export'`, install `@opennextjs/cloudflare`, change Pages config to point at the Worker. Not a one-way door.

The only feature we lose with static export is the **dynamic edge OG image**. Solution: pre-generate it once as a static PNG and commit it.

---

## ⚠️ Phase 0 — Peter actions (security, do FIRST, before any code)

**Cowork: do not start Phase 1 until Peter confirms 0.1 and 0.2 are complete.**

### 0.1 — Rotate Cloudflare password (URGENT)

The current password was pasted in plaintext to a Claude Code chat on 2026-05-06 and is now in transcripts and auto-memory. Treat as compromised.

1. Log into Cloudflare → top-right avatar → **My Profile**
2. **Authentication** tab → **Change Password**
3. Generate a new password using a password manager (1Password, Bitwarden, Apple Passwords). Minimum 20 chars, fully random. **Do NOT use any pattern related to "Solutions" or family names.**
4. Save in password manager. **Never paste this anywhere except the Cloudflare login form.**

### 0.2 — Enable 2FA on Cloudflare

1. Same Authentication tab → **Two-Factor Authentication** → **Enable**
2. Use an authenticator app (Google Authenticator, Authy, 1Password's built-in). **Not SMS** — SMS is vulnerable to SIM-swap.
3. Save the recovery codes in your password manager.

### 0.3 — Create a private GitHub repo (Peter or Cowork)

If Peter has the `gh` CLI authenticated and is comfortable, Cowork can run this:

```bash
cd ~/Desktop/metis-cortex
gh auth status   # verify authenticated
gh repo create kritsotakis/metis-cortex --private --source . --remote origin
```

If `gh` is not authenticated, Peter does this in browser:
1. github.com → **New repository** → Owner: `kritsotakis` (or his GitHub username) → Name: `metis-cortex` → **Private** → no README/license/gitignore (the local repo already has them)
2. Copy the repo's HTTPS URL (e.g. `https://github.com/kritsotakis/metis-cortex.git`)
3. Tell Cowork the URL — Cowork will run `git remote add origin <URL>` and push.

**Do NOT push yet.** We push at the end of Phase 1, after the static-export changes are committed.

### Gate before Phase 1

Cowork must have written confirmation in the chat from Peter that:
- [ ] Cloudflare password rotated
- [ ] Cloudflare 2FA enabled with authenticator app
- [ ] GitHub repo created (URL captured)

---

## Phase 1 — Cowork actions (code changes for static export)

**Timebox: 30 minutes. If exceeded, stop and surface what's blocking.**

### 1.1 — Convert Next config to static export

Edit `next.config.ts`:

```ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "export",
  images: {
    unoptimized: true, // required for static export — no Image Optimization at build
  },
  // Trailing slash is required for Cloudflare Pages to serve /path/ correctly
  trailingSlash: true,
};

export default nextConfig;
```

**Why each option:**
- `output: "export"` — produces static HTML/CSS/JS in `out/` directory at build time
- `images: { unoptimized: true }` — Next's built-in Image Optimization is server-side; static export can't use it. The site barely uses `next/image` (check Hero/cards), but this option is required.
- `trailingSlash: true` — Cloudflare Pages serves `metiscortex.au/about` as `metiscortex.au/about/index.html` only when trailing slash is on, otherwise you get 404s on subpaths.

### 1.2 — Replace dynamic OG with static PNG

Static export can't run `next/og` at request time, but we can generate the same image once at build time and commit it.

**Step A: Create a one-shot generator script.**

Create `scripts/generate-og.mjs`:

```js
import { ImageResponse } from "@vercel/og";
import { writeFileSync, mkdirSync } from "node:fs";
import { resolve } from "node:path";

const out = await new ImageResponse(
  (
    {
      type: "div",
      props: {
        style: {
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          padding: 80,
          background: "radial-gradient(circle at 80% 20%, #1a3454 0%, #0e1e2e 60%)",
          color: "#f5f1ea",
          fontFamily: "Georgia, serif",
        },
        children: [
          {
            type: "div",
            props: {
              style: { display: "flex", alignItems: "center", fontSize: 28, letterSpacing: 1, textTransform: "uppercase" },
              children: [
                { type: "span", props: { style: { color: "#b07843", marginRight: 12 }, children: "·" } },
                { type: "span", props: { children: "Metis Cortex" } },
              ],
            },
          },
          {
            type: "div",
            props: {
              style: { display: "flex", flexDirection: "column" },
              children: [
                { type: "div", props: { style: { display: "flex", fontSize: 140, lineHeight: 1, letterSpacing: -2, fontWeight: 600 }, children: "Stop missing" } },
                { type: "div", props: { style: { display: "flex", fontSize: 140, lineHeight: 1, letterSpacing: -2, fontWeight: 600, fontStyle: "italic", color: "#cc9359", marginTop: 8 }, children: "calls." } },
                { type: "div", props: { style: { display: "flex", fontSize: 32, color: "rgba(245, 241, 234, 0.78)", fontFamily: "system-ui, sans-serif", maxWidth: 920, marginTop: 40 }, children: "AI receptionist installed in 14 days. A$1,500 setup. Refund guarantee." } },
              ],
            },
          },
        ],
      },
    }
  ),
  { width: 1200, height: 630 },
);

const buf = Buffer.from(await out.arrayBuffer());
mkdirSync(resolve("public"), { recursive: true });
writeFileSync(resolve("public/og.png"), buf);
console.log("✓ Generated public/og.png (" + buf.length + " bytes)");
```

**Step B: Add `@vercel/og` as a devDependency** (one-shot generator only, not shipped in production):

```bash
cd ~/Desktop/metis-cortex
npm install --save-dev @vercel/og
```

**Step C: Add an npm script for the generator** in `package.json`:

```json
"scripts": {
  "dev": "next dev",
  "build": "next build",
  "start": "next start",
  "lint": "eslint",
  "og": "node scripts/generate-og.mjs"
}
```

**Step D: Run the generator once to produce the file.**

```bash
npm run og
```

Verify `public/og.png` exists, ~50–150KB, and looks correct (open it in Preview).

**Step E: Delete the dynamic OG components.**

```bash
rm src/app/opengraph-image.tsx src/app/twitter-image.tsx
```

**Step F: Update `src/app/layout.tsx` metadata to reference the static PNG.**

In the `metadata.openGraph` block, add:

```ts
openGraph: {
  type: "website",
  url: SITE_URL,
  siteName: "Metis Cortex",
  title: TITLE,
  description: DESCRIPTION,
  locale: "en_AU",
  images: [
    {
      url: "/og.png",
      width: 1200,
      height: 630,
      alt: "Metis Cortex — Stop missing calls.",
    },
  ],
},
twitter: {
  card: "summary_large_image",
  title: TITLE,
  description: DESCRIPTION,
  images: ["/og.png"],
},
```

### 1.3 — Verify build

```bash
cd ~/Desktop/metis-cortex
npm run build
```

**Expected output:** Build completes without errors. `out/` directory contains:
- `out/index.html` (the homepage)
- `out/og.png` (1200×630, copied from public/)
- `out/sitemap.xml`
- `out/robots.txt`
- `out/_next/...` (CSS/JS chunks, fonts)

**If build fails:**
- Read the full error
- Most likely cause: a component uses something incompatible with static export (e.g. `cookies()`, `headers()`, dynamic route params). Fix the source, don't disable static export.
- If you can't resolve in 10 minutes, stop and surface to Peter.

### 1.4 — Smoke-test the static output locally

```bash
npx serve out -p 3000
```

Open `http://localhost:3000` in browser. Confirm:
- Homepage renders (Hero, all 9 sections, Footer)
- No console errors in DevTools
- OG image accessible at `http://localhost:3000/og.png`
- View-source contains `<meta property="og:image" content="https://metiscortex.au/og.png">`

### 1.5 — Commit and push

```bash
cd ~/Desktop/metis-cortex
git add -A
git status   # review what's being committed — make sure no .env, no secrets
git commit -m "$(cat <<'EOF'
chore: migrate to Cloudflare Pages static export

- Add output: export to next.config.ts
- Replace dynamic next/og endpoint with static public/og.png
- Add scripts/generate-og.mjs for future regeneration
- Apply brand spec (.au canonical, ink #0e1e2e, bronze #b07843)

Co-Authored-By: Cowork <noreply@cowork>
EOF
)"
git remote -v   # confirm origin points at the GitHub repo Peter created in Phase 0.3
git push -u origin main
```

If the branch is named `master` not `main`, push to `master` and we'll rename later.

### Phase 1 deliverables

Cowork tells Peter when these are all true:
- [ ] `next.config.ts` set to static export
- [ ] `public/og.png` generated and committed
- [ ] Old `opengraph-image.tsx` + `twitter-image.tsx` deleted
- [ ] `npm run build` exits 0
- [ ] `out/` smoke-tested locally
- [ ] Push to GitHub successful — paste the GitHub repo URL back to Peter
- [ ] Total time spent

---

## Phase 2 — Peter actions (Cloudflare Pages connection, browser only)

**Cowork cannot do this — requires Peter's auth.**

### 2.1 — Create Pages project

1. Cloudflare dashboard → **Workers & Pages** (left sidebar) → **Create application** → **Pages** tab → **Connect to Git**
2. Authorize Cloudflare to access GitHub (if not already) → select `kritsotakis/metis-cortex`
3. **Set up builds and deployments:**
   - **Project name:** `metis-cortex`
   - **Production branch:** `main` (or `master` if Phase 1 used master)
   - **Framework preset:** select **Next.js (Static HTML Export)** — IMPORTANT, not the regular "Next.js" preset
   - **Build command:** `npm run build`
   - **Build output directory:** `out`
   - **Root directory:** `/`
   - **Environment variables:** none needed for v1
4. **Save and Deploy.**
5. Wait ~90 seconds for the first build. You'll get a `.pages.dev` preview URL. Open it and confirm the site renders. Keep this URL — you'll use it to verify before flipping the domain.

### 2.2 — Add the custom domain

1. In the Pages project → **Custom domains** tab → **Set up a custom domain**
2. Enter `metiscortex.au` → Cloudflare will check DNS and tell you what's needed.

**There are two ways Cloudflare can manage this domain — pick based on where DNS is now:**

#### Option A — Move DNS to Cloudflare (recommended; faster, free DDoS, free SSL, easier future changes)

1. In Cloudflare dashboard → **Add a Site** → enter `metiscortex.au` → choose **Free plan**
2. Cloudflare scans existing DNS records — review and accept
3. Cloudflare gives you 2 nameservers (e.g. `aaron.ns.cloudflare.com` and `tegan.ns.cloudflare.com`)
4. In **GoDaddy** (where the domain is registered):
   - Login → My Products → `metiscortex.au` → **DNS** → **Nameservers** → **Change** → **I'll use my own nameservers**
   - Paste the 2 Cloudflare nameservers, save
5. Wait 5–60 minutes for nameservers to propagate (Cloudflare emails when active)
6. Back in Pages → Custom domains → Cloudflare auto-detects, provisions SSL in ~10 min, marks domain Active
7. Open `https://metiscortex.au` — should load over HTTPS

#### Option B — Keep DNS at GoDaddy, just point records at Cloudflare Pages

1. Cloudflare Pages will tell you to add a **CNAME** record:
   - Name: `@` (or root) — pointing to `metis-cortex.pages.dev`
   - Plus a CNAME for `www` → `metis-cortex.pages.dev`
2. Some registrars don't allow CNAME at root — GoDaddy supports it as an "ANAME" or "CNAME flattening" setting. If GoDaddy doesn't allow, use **Option A**.
3. Save records, wait 5–30 min for propagation
4. Pages will auto-provision SSL

**Recommendation: use Option A.** Cleaner long-term, plays well with Cloudflare's other features (Workers, R2, Email, etc.) you may want later.

### 2.3 — Set up domain redirects (defensive registrations)

If Peter owns `metiscortex.com.au` and `metiscortex.com`, set them to 301 → `metiscortex.au` so SEO doesn't fragment:

1. In each domain's Cloudflare zone (you'd need to add them too via "Add a Site"):
2. **Rules → Redirect Rules → Create rule**:
   - When: hostname equals `metiscortex.com.au` (or `metiscortex.com`)
   - Then: Static redirect, Type: **301 Permanent**, URL: `https://metiscortex.au${URI_PATH}`

If `.com` and `.com.au` aren't owned yet — skip for now. Defensive registration is fine but not required for v1.

### Phase 2 deliverables

Peter confirms when:
- [ ] Cloudflare Pages project created and first deploy is green
- [ ] `metiscortex.au` resolves over HTTPS to the new site
- [ ] Pages preview URL also resolves (sanity check)
- [ ] DNS migration confirmed (nameservers updated, propagation done)

---

## Phase 3 — Cowork verification

**Timebox: 15 minutes.**

Once Peter confirms Phase 2 is live, Cowork runs:

```bash
# Production URL responds
curl -I https://metiscortex.au/ | head -10
# Should see: HTTP/2 200, server: cloudflare, content-type: text/html

# OG image is accessible
curl -I https://metiscortex.au/og.png | head -5
# Should see: HTTP/2 200, content-type: image/png

# Sitemap and robots
curl -s https://metiscortex.au/sitemap.xml | head -20
curl -s https://metiscortex.au/robots.txt

# OG meta tags present in HTML
curl -s https://metiscortex.au/ | grep -E 'og:image|og:title|twitter:card'
# Should show og:image pointing to https://metiscortex.au/og.png

# JSON-LD LocalBusiness schema present
curl -s https://metiscortex.au/ | grep -A1 'application/ld+json'

# Cloudflare-specific headers (sanity check)
curl -I https://metiscortex.au/ | grep -i 'cf-ray\|cf-cache'
```

Run a quick Lighthouse from the command line if available:

```bash
npx lighthouse https://metiscortex.au/ --only-categories=performance,accessibility,best-practices,seo --quiet --chrome-flags='--headless' --output=json --output-path=./lighthouse-report.json
```

**Pass criteria:**
- All four Lighthouse categories ≥ 90 (target was 95+; ≥90 is acceptable for v1)
- LCP < 2s
- No console errors
- All meta tags present

If any fail, surface to Peter with the specific finding. Don't try to fix Lighthouse in this session — that's a separate task.

### Phase 3 deliverables

Cowork posts back:
- [ ] All curl checks pass
- [ ] Lighthouse scores (4 numbers)
- [ ] Any failed checks (specific URLs / error messages)
- [ ] Total time spent

---

## What Cowork must NOT do

- **Do not** ask Peter for the Cloudflare password again. The auth flow is GitHub integration, not password.
- **Do not** install `@cloudflare/next-on-pages` or `@opennextjs/cloudflare`. We're not using Workers.
- **Do not** edit any component files (Hero, Footer, etc.) — only the files explicitly listed in Phase 1.
- **Do not** delete `node_modules` and reinstall unless build fails specifically because of a dependency mismatch.
- **Do not** rewrite the README. The README will be updated in a separate task once Phase 1 lands.
- **Do not** push to a remote that isn't `kritsotakis/metis-cortex` (or whatever Peter named in 0.3).
- **Do not** commit `public/og.png` if it's >500KB without compression — run it through `pngquant` or similar first.
- **Do not** mark the migration "Final" until Phase 3 verification passes. "Done" ≠ "Final" until checks are green.

## Out of scope (do not touch this round)

- Logo integration — pending logo export from Manus/Gemini, will be a separate task
- Analytics (Plausible/Cloudflare Web Analytics) — separate task once deploy is live
- Phase 2 features (about page, audit page, vertical landing pages) — explicitly deferred per onboarding doc
- README updates — separate task
- Adding `.com` and `.com.au` defensive domains — only if Peter confirms he owns them

## Total timebox

| Phase | Owner | Timebox |
|---|---|---|
| 0 — Security + GitHub repo | Peter | 15 min |
| 1 — Code changes | Cowork | 30 min |
| 2 — Cloudflare connect | Peter | 20 min |
| 3 — Verification | Cowork | 15 min |
| **Total** | | **~80 min** |

If the total exceeds 2 hours, stop and surface why.

## Rollback plan

If anything breaks in production:

1. **Pages deploy is bad:** in Cloudflare Pages → Deployments → find the last green deploy → **Rollback to this deploy**. Takes ~30 sec.
2. **Custom domain misconfigured:** in Pages → Custom domains → remove `metiscortex.au` → Cloudflare reverts; site stays on `metis-cortex.pages.dev` until you re-add.
3. **Code regression:** in the GitHub repo → revert the offending commit → push → Pages auto-rebuilds.

Site can't be "broken beyond recovery" because the source of truth is the Git repo. Worst case: revert the static-export commit, and we re-plan.

---

## Confirmation Cowork sends back to Peter when done

Paste this filled in:

```
✅ Phase 0 — Peter confirmed password rotated, 2FA on, GitHub repo at <URL>
✅ Phase 1 — Static export commit pushed: <commit SHA>, build OK in <N>s, og.png <size>KB
✅ Phase 2 — Peter confirmed Pages live, custom domain resolving over HTTPS
✅ Phase 3 — Lighthouse Perf/A11y/BP/SEO: <P>/<A>/<BP>/<SEO>, all curl checks pass
Production URL: https://metiscortex.au
Pages preview URL: https://metis-cortex.pages.dev
Total time: <total>
```

Then update `~/.claude/memory/active-projects.md` with a new row:

```
| **Metis Cortex live** | Metis Cortex | LIVE on Cloudflare Pages from GitHub kritsotakis/metis-cortex. Static export, og.png static, .au canonical. | Logo integration (pending Manus/Gemini export), analytics setup, README update | 2026-05-06 |
```

And append to `~/.claude/memory/recent-activity.md`:

```
## 2026-05-06 (Wed) — Metis Cortex hosting migrated to Cloudflare Pages

**Context:** Site was built locally on May 4, no remote, no host. Migration to Cloudflare Pages from GitHub via static export. Brand/domain edits already applied (.au canonical, ink #0e1e2e, bronze #b07843).

**Built:** Static export config, static og.png, GitHub repo kritsotakis/metis-cortex, Pages project with auto-deploy on main, custom domain metiscortex.au with HTTPS.

**Logged to:** active-projects.md row "Metis Cortex live"
```
