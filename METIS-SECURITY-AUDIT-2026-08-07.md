# METIS CORTEX — SECURITY & DATA POSTURE AUDIT (2026-08-07)

> **STATUS: H1–H6, M1 and M9 FIXED AND DEPLOYED 2026-08-07.**
>
> **LATER THE SAME DAY — the encryption position below was superseded.** §2 and
> the "Deliberately NOT done" note say there is no application-layer encryption.
> That was true when written and is now false: AES-256-GCM field encryption was
> built, the key set, and encryption verified in production against a live
> backup. See `METIS-SAFETY-AND-REDUNDANCY-2026-08-07.md` §2 for the current,
> authoritative position and the exhaustive list of what is and is not covered.
> The original text is left intact below so the record shows what was actually
> found. See the
> "Remediation" section at the end for what was changed, what was verified in
> production, and what deliberately was not done. The findings below are kept
> as written so the record shows what was actually wrong.

Code-verified against `/Users/kritsotakis/dev/metis/app` @ `9f52309`. Every claim below
traces to a file:line. Where something could only be verified from a prior operational
check (flyctl output), that is stated rather than assumed.

## 1. Where the data actually lives

- **Database:** MySQL on **Fly.io, Sydney** (`fly.toml:7`, `primary_region = "syd"`).
  Pool at `server/db.ts:44`. ⚠️ **No TLS options are passed** — whether the app↔DB hop is
  encrypted depends entirely on whether `DATABASE_URL` carries `?ssl=`, which is not
  verifiable from the repo. `DEPLOY.md` still documents Railway and is stale/wrong.
- **Uploaded files:** **local Fly volume**, not R2. `fly.toml:17-18`
  (`STORAGE_DRIVER=local`, `LOCAL_STORAGE_DIR=/data/storage`), volume `metis_data`
  mounted at `/data` (`fly.toml:34-36`).
- **Backups:** `server/backupToR2.ts` mirrors the **file volume only** to R2, incrementally,
  daily via an in-process scheduler. **Silently optional** — if R2 creds are unset the app
  logs a warning and continues (`_core/index.ts:83-89`).
- **⚠️ There is no database backup code anywhere in the repo.** Only Fly's own volume
  snapshots (5-day retention), which `fly.toml:28-31` itself says are not a primary backup.

### Personal data held (from `drizzle/schema.ts`)
Client names, emails, phones, postal addresses; free-text legal issue descriptions;
**raw + processed consultation transcripts**; audio recordings on the volume; AI-detected
issues with verbatim transcript excerpts; case briefs, proposals, research; **portal tokens
and magic-link tokens in plaintext**; portal messages; matter titles/descriptions;
**full extracted text of every uploaded document**; client↔AI chat history; court-form
answers; conflict checks; client-ID verification records (type + notes only — the ID
document itself is deliberately not stored); costs figures; portal access log **including
IP addresses**.

## 2. Encryption — the honest answer

- **In transit (browser→app):** TLS terminated by Fly (`fly.toml:22 force_https = true`).
  Cloudflare is **DNS-only / grey-clouded**, so there is **no WAF or CDN** in front.
- **At rest:** provider disk encryption only — Fly volume shows `ENCRYPTED: true`;
  R2 applies its own default SSE. **Database at-rest encryption is unconfirmed.**
- **Application-layer encryption: NONE.** Zero fields encrypted. A grep for
  `encrypt|cipher|aes|SSE` across server, schema and client returns nothing relevant.
  `meetingSessions.encryptionKeyId` is a dead legacy column, never written.
  The schema says so itself at `schema.ts:64-68`: *"transcripts are NOT app-layer
  encrypted today … Do not describe session data as 'encrypted' in UI."*

**So: transcripts, client PII, document text, chat history and both token types sit in
readable plaintext columns.** That is defensible if disclosed precisely (it is) — but it
is the largest exposure before real client data.

## 3. Auth & sessions — mostly strong

- **Magic link:** 256-bit tokens (`db.ts:149`, `crypto.getRandomValues(32)`), 15-min expiry,
  single-use enforced. Non-enumerating (returns `sent:true` for unknown addresses) while
  still failing loudly if the mailer breaks. Sign-in **can never grant the solicitor role**
  (`magicAuth.ts:96-104`) — that only comes from `scripts/grantSolicitor.ts`. ✅
- **Session cookie:** `httpOnly` ✅, `Secure` in production ✅, **`SameSite=None`** in
  production (needed for the browser extension) — see H2.
- **JWT:** HS256 via `jose`, **algorithm pinned on verify** (`sdk.ts:213`) so alg-confusion
  is closed ✅. Boot guard refuses to start in production without a ≥32-char `JWT_SECRET`
  (`_core/index.ts:48`) ✅. **No revocation / no `jti`** — a stolen cookie stays valid 7 days.
- **DEV_AUTH: triple-guarded** — two env flags + non-production, a hard production boot
  failure that deliberately reads the *raw* env var so the guard can't defuse itself
  (`_core/index.ts:26-33`), plus `DEV_AUTH=false` baked into the Dockerfile. No gap found. ✅
- **Role gating: complete.** All **41** procedures in `consultation.ts` are
  `solicitorProcedure`, verified exhaustively. No leaks. ✅

## 4. Tenancy — one real hole

The `db.ts` helpers are split into clearly-labelled filter-in-SQL (safe) and
unfiltered-fetch-by-id (caller must check) families. Every `consultation.ts` procedure
taking a `sessionId`/`clientId` **does** perform an ownership check. The matter-pack ZIP
route uses `req.user.id`, never a client-supplied id. That part is sound.

**The exception is H1 below.**

## 5. Third parties — what each actually receives

| Service | Receives | Path |
|---|---|---|
| **Anthropic** | **Full consultation transcripts**, matter titles/descriptions, checklist state, **extracted document text**, chat history, user messages | `_core/llm.ts:344`; `consultation.ts:1146`; `metis.ts:571`. **No ZDR — ~30-day US retention** |
| **Deepgram** | **Raw consultation audio**, diarised | `_core/voiceTranscription.ts:105` |
| **Google Gemini** | LLM payloads + **raw audio base64** when routed there. ⚠️ **API key in the URL query string** (`voiceTranscription.ts:190`) | dormant path (no key set) |
| **Resend** | Recipient email, **magic-link URL containing the live token**, client first+last name, 300-char message preview | `email.ts:38-40, 82-85, 250-252`. US-stored |
| **Stripe** | User email + matter id only. No names, no matter content ✅ | `stripe.ts:33-39` |
| **AustLII** | ⚠️ **The first 200 characters of the raw transcript, as a public GET query string** | `consultation.ts:1282` → `austlii.ts:129` |
| **ElevenLabs** | **Nothing** — demo voiceover only, not in any user-data path ✅ | repo-root script |

## 6. Gaps, ranked

### HIGH — fix before real client data
- **H1 · Cross-tenant document-text read (real, exploitable).**
  `metis.uploadDocument` (`metis.ts:458, 466-495`) ownership-checks the *matter* but accepts
  an **unverified client-supplied `storageKey`**, then `storageReadBytes()` it and persists
  the extracted text into the caller's own matter — readable afterwards via chat/matter-pack.
  An authenticated user who learns another tenant's storage key can exfiltrate that
  document's full text. Keys carry ~32 bits of suffix entropy plus the filename, so it isn't
  trivially brute-forceable — but this is a **missing authorisation check**, not a control.
- **H2 · No CSRF protection, with `SameSite=None` cookies.** tRPC mutations are cookie-
  authenticated POSTs with no CSRF token and no Origin/Referer check (`cookies.ts:50`,
  `_core/index.ts:102`). Also affects the plain upload and matter-pack routes.
- **H3 · No Content-Security-Policy is served at all.** `helmet({contentSecurityPolicy: false})`
  defers CSP "to the Cloudflare layer" — but Cloudflare is DNS-only and that layer does not
  exist. An app that ingests attacker-supplied PDFs and renders LLM output has no XSS backstop.
- **H4 · No app-layer encryption, and auth tokens stored in plaintext.** Any DB read — leaked
  `DATABASE_URL`, support query, backup file — is total compromise **including the ability to
  mint live sessions** from unexpired magic-link tokens. Minimum fix: store SHA-256 of both
  token types and look up by hash.
- **H5 · Verbatim client speech sent to AustLII in a URL.** 200 chars of raw consultation
  text, GET, public internet, to a service **not in the subprocessor register**. Fix: send
  only detected legal-area keywords.
- **H6 · DB TLS unspecified; DB at-rest encryption unconfirmed.** Pass explicit
  `ssl: { rejectUnauthorized: true }` and get written confirmation from Fly.

### MEDIUM
M1 no DB backup in code · M2 R2 backup silently optional · M3 magic-link consume not atomic
(select-then-update race) · M4 the tight auth rate limiter guards the wrong route (the tRPC
`requestMagicLink` is only under the 500/15min general limiter) · M5 four portal procedures
unrate-limited · M6 rate limiting in-memory/per-instance · M7 rate limiting disabled outside
production · M8 file-type validation is declared-MIME only, and the extension API has **no
filter at all** · **M9 `auditLog` table exists and is never written — zero audit trail of who
read or exported which client's file** · M10 no session revocation · M11 Gemini key in URL ·
M12 portal tokens live 30 days with no rotation.

### LOW
L1 `appId` claim never validated · L2 `DEPLOY.md` stale/wrong platform · L3 Stripe webhook not
idempotent (no impact today) · L4 dead `encryptionKeyId` column · L5 global 50 MB JSON limit ·
L6 `enforceRails` is paraphrase-bypassable (it's a UPL control, not a security one — never
present it as injection defence) · L7 `ALLOWED_EMAILS` unset at launch, so the allowlist no
longer gates.

## 7. What's genuinely good (don't re-litigate)

Complete `solicitorProcedure` coverage (41/41, verified); triple-guarded DEV_AUTH with a
raw-env-var boot check; `JWT_SECRET` ≥32-char production guard; JWT algorithm pinning;
**Stripe webhook raw-body ordering correct** (the detail most implementations get wrong);
storage proxy authorises against the owning record and 404s rather than 403s to prevent key
probing, forcing `attachment` + `nosniff` + `no-store`; 256-bit tokens throughout;
path-traversal defence in depth; a well-reasoned phone-scan token design (15-min, audience-
scoped, write-only); the `READ_FILE` pseudo-tool loop is properly contained (user+matter
scoped, budget-capped) — a genuine prompt-injection containment win; **no secrets in the repo
or its git history**, with a `.gitignore` whose comment records the near-miss that produced it.

The codebase is unusually honest about its own gaps — several comments cite the dated incident
that produced the fix. That candour means the items above are **omissions, not
misrepresentations**.

## Pre-launch minimum before real client data
**H1, H2, H3, H4 (at least token hashing), H5, H6, plus M1 and M9.**


---

# REMEDIATION — 2026-08-07 (deployed and verified in production)

| Finding | Fix | Verified |
|---|---|---|
| **H1** cross-tenant document-text read | Storage keys are now namespaced per user (`documents/u<id>/…`); `metis.uploadDocument` rejects any key outside the caller's namespace | 5 regression tests in `server/security.test.ts`, incl. the near-miss cases (u1 vs u12 prefix, traversal) |
| **H2** no CSRF protection | `server/_core/originGuard.ts` — Origin/Referer allowlist on every state-changing `/api` request; Stripe webhook and token-authed phone upload exempted with reasons | Deployed; app functioning normally |
| **H3** no CSP served | Real Content-Security-Policy enabled in production via helmet (`script-src 'self'`, no `unsafe-inline` for scripts) | `curl -I` confirms the header is served |
| **H4** auth tokens stored plaintext | Magic-link and portal tokens stored as SHA-256 digests; raw value never persisted. Magic-link consume switched to a conditional UPDATE, closing the select-then-update race | Legacy plaintext rows purged (16 removed); dump re-verified |
| **H5** raw transcript sent to AustLII | Search now uses the detected legal area + our own issue-type vocabulary; no client words leave the system | Code change in `consultation.ts` |
| **H6** DB TLS unspecified | TLS now explicitly configured. **Production uses `no-verify`, not full verification** — see the incident note below | Verified live |
| **M1** no database backup | `server/backupDatabase.ts` + independent daily scheduler + `pnpm backup:db` | **Dump retrieved from R2 and content-verified**: 115 rows / 27 tables / 231KB, 4 matters and 89 document records intact |
| **M9** `auditLog` never written | `server/audit.ts`; wired to matter-pack export, portal token mint/revoke, proposal sharing | Fire-and-forget by design — cannot break the audited operation |

## Two incidents caused by this work, both caught and fixed

1. **I took the database offline for ~2 minutes.** Setting
   `rejectUnauthorized: true` broke the connection — the managed MySQL presents
   a self-signed certificate (`HANDSHAKE_SSL_ERROR`). Production now uses
   `no-verify`: still encrypted, chain not verified, which is honest about what
   it does and does not protect against. Set `DB_SSL=require` if the provider
   ever serves a publicly-chained certificate.
2. **The database dump was initially nested inside the file-sync's
   "already ran today" guard**, so on any day the file sync had already run,
   the database would never have been dumped at all. The two checks are now
   fully independent.

## Deliberately NOT done

- ~~**App-layer field encryption (part of H4).**~~ **SUPERSEDED the same day —
  this WAS subsequently built.** The reasoning below stood at the time; Peter
  asked whether to defer it to the first client, and the answer was that
  retrofitting onto a live firm's matters is a migration under pressure while
  doing it against near-empty tables is close to free. Transcripts, case briefs,
  legal issues, proposals, document text, chat and portal messages are now
  encrypted; client names, emails and matter titles deliberately are not.
- **A full restore rehearsal** into a scratch database. The dump has been
  retrieved and verified readable and complete; it has not been replayed.
- **M2–M8, M10–M12 and the LOW findings** — none are exploitable authorisation
  holes; they are hardening. Next pass.
