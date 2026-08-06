# Metis Cortex — safety, security and redundancy

**As at 7 August 2026.** Written to be handed to a solicitor or a firm's IT
adviser. Everything below is either verified or explicitly marked as not yet
verified. Nothing here is aspirational.

If you are looking for the sentence that says "100% secure", it isn't here, and
you should distrust any legal-tech vendor who offers it.

---

## 1. Where your data physically is

| | |
|---|---|
| **Application and database** | Fly.io, **Sydney (`syd`)** |
| **Documents you upload** | Encrypted disk on that same Sydney machine |
| **Backups** | Cloudflare R2 — separate infrastructure and failure domain from the live machine. Both backups write to the same bucket under one set of credentials, so they are process-independent, not account-independent. **Bucket jurisdiction is to be confirmed and stated here.** |
| **AI drafting** | Anthropic (Claude) — **processed in the United States** |
| **Transcription** | Deepgram — only if audio is uploaded, and only after consent is confirmed |
| **Email** | Resend — US-stored |
| **Payments** | Stripe — receives your email and a matter reference only. No client names, no matter content |

The overseas AI processing is the honest caveat in an otherwise Australian
stack. It is disclosed in the privacy policy rather than buried.

---

## 2. Encryption — precisely what it does and doesn't do

**In transit.** TLS on every connection, HTTPS forced. The database connection
is encrypted, though its certificate chain is not verified — the managed
database presents a self-signed certificate, and it travels a private
WireGuard-encrypted network, so the realistic risk is passive observation
rather than interception.

**At rest — infrastructure.** Provider disk encryption on both the Sydney
volume and the backup storage.

**At rest — application layer.** The sensitive content is encrypted by Metis
itself with **AES-256-GCM** before it reaches the database:

- conference transcripts (raw and processed)
- the case brief / file note, including the risks-warned and client-response fields
- identified legal issues and the transcript excerpts supporting them
- case proposals
- the full extracted text of every uploaded document
- matter chat history and client-portal messages
- the client's own free-text account of their problem

Authenticated encryption, so tampered data fails loudly rather than silently
returning something altered — which matters when the content is a file note.

**Not encrypted, and this list is exhaustive:** client names, emails, phone
numbers, matter titles, research citations, action items and milestones,
conflict-check and client-ID notes, and the portal access log (including IP
addresses). Names and titles are sorted, searched and displayed in list views,
so encrypting them would break those features for a small gain over the content
above. That is a product decision, recorded here so it is visible rather than
assumed.

**Applies to data written from 7 August 2026 onward.** Records created before
that date remain in plain columns until they are next rewritten. Both forms are
readable by the application; the distinction only matters if a backup from
before that date were exposed.

**Authentication tokens are stored hashed**, never in readable form. A database
leak exposes useless digests, not working sign-in links.

### What this protects against
A leaked database dump, a stolen connection string, a support query, or
provider-side access to the disk.

### What it does not protect against
**Compromise of the running application.** Metis holds the key and must decrypt
to function, so anything executing as the application can read everything. This
is true of every system of this kind. It is not end-to-end encryption and is
never described as such.

---

## 3. Redundancy — the "something happens the morning of a hearing" scenario

Two independent daily backups to infrastructure separate from the live system:

| What | Where | Frequency | Retention |
|---|---|---|---|
| Every uploaded document | Cloudflare R2 | Daily, incremental | Indefinite |
| Full database — all 29 tables | Cloudflare R2, gzipped | Daily | 30 days |
| Volume snapshots | Fly.io | Automatic | 5 days |

An on-demand backup can be taken at any time before anything risky.

### Verified, not assumed
- **Volume restore, actually performed:** a snapshot was restored to a scratch
  volume, contents verified, and the test resources torn down. **Measured
  recovery time ≈ 30 seconds. Recovery point ≤ 24 hours.**
- **Database dump, actually retrieved:** a dump was downloaded from R2 and
  decompressed *outside* the application, confirming every table and every
  matter and document record present and readable.
- Spent authentication tokens are purged **before** each dump, so dead
  credentials never travel offsite.

### Not yet verified
A full restore *rehearsal* — replaying a dump into a live schema. The backup is
proven readable and complete; it has not been proven replayable. That
distinction is stated rather than glossed, and closing it is the next step.

---

## 4. Access control

- **No passwords.** Sign-in is by single-use emailed link, valid 15 minutes.
  There is no password to breach, reuse or phish.
- **The tenancy-critical queries filter by the owning user in SQL**, not after
  the fact. A small number of fetch-by-id helpers are explicitly labelled as
  unfiltered and are checked at each call site. This is the failure class that
  has bitten the project before, and the known paths are regression-tested — a
  test suite cannot, however, detect a *new* feature that forgets the check.
- **Solicitor features are role-gated** — verified exhaustively across all 41
  solicitor procedures.
- **Client portal links** expire in 30 days, can be revoked instantly by the
  solicitor, and are stored hashed.
- **State-changing API requests are origin-checked** (cross-site writes are
  rejected), and a **Content-Security-Policy** with `script-src 'self'` is
  served in production.

---

## 5. Audit trail

**Export and sharing** of client material is recorded: who, what and when.
The covered events are full matter-pack exports (which also record the IP
address and browser), portal link creation and revocation, sharing a proposal
with a client, and deleting a document.

Deliberately not a general request log — recording every list view would bury
the events that matter. To be precise about the current limit: **viewing a
matter or opening a transcript is not itself logged**, only export and sharing.

---

## 6. The professional-obligation question: what if Metis disappears?

A firm's file-retention obligations are its own, and "our vendor had it" is not
an answer. Three points:

1. **Export whenever you like.** Any matter exports as a single archive
   containing every document plus a summary. Nothing is held hostage.
2. **Intended practice-management integration.** Our LEAP developer
   registration is in progress; **nothing is built.** The intention is narrow:
   push the finished file note and brief into the right LEAP matter, which is
   already your system of record and already inside your own backup and
   retention regime. Until it exists, you would copy the file note across.
3. **We do not push copies onto firm hardware,** and that is deliberate: a copy
   on an unmanaged laptop is one nobody can secure, audit, or delete on
   request.

---

## 7. Known gaps — stated plainly

A vendor who lists none of these is not being straight with you.

| Gap | Status |
|---|---|
| **No independent penetration test or third-party security audit** | Real. The code was audited internally on 7 August 2026 and the high-severity findings fixed; a documented hardening backlog remains open. Nobody external has tried to break it. |
| **No 24/7 automated intrusion monitoring** | One person checks manually. |
| **Single founder** | One person is the whole detection, response and continuity plan. A continuity arrangement is not yet documented. |
| **Overseas AI processing without a zero-retention agreement** | Matter content reaches Anthropic in the US under standard retention. Disclosed, not yet negotiated away. |
| **Subprocessor data-processing agreements not all confirmed executed** | In progress. |
| **Professional indemnity and cyber insurance not yet in force** | Blocks real client data on the solicitor side. |
| **Costs-disclosure wording not yet lawyer-reviewed** | The four s174 client-rights statements generate as a visible blank rather than invented text. Blocks real client use. |
| **Terms of service and privacy policy have not had a lawyer's review** | One of the four standing pre-launch gates. |
| **Formal Australian data-residency review not done** | Hosting is in Sydney, but AI processing happens in the US. The formal review is the gate, not the hosting. |
| **No real client conference has ever been recorded through the product** | The pipeline is proven on pasted and synthetic transcripts only. |

---
