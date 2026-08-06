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
| **Backups** | Cloudflare R2 — separate infrastructure, separate failure domain |
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

**At rest — application layer.** The most sensitive columns are encrypted by
Metis itself with **AES-256-GCM** before they reach the database:

- conference transcripts (raw and processed)
- the full extracted text of every uploaded document
- matter chat history
- the client's own free-text account of their problem

Authenticated encryption, so tampered data fails loudly rather than silently
returning something altered — which matters when the content is a file note.

**Deliberately not encrypted:** client names, emails, phone numbers and matter
titles. They are sorted, searched and displayed in list views, and encrypting
them would break those features for a small gain over the free-text content
above. That is a product decision, recorded here so it is visible rather than
assumed.

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
| Full database — all 27 tables | Cloudflare R2, gzipped | Daily | 30 days |
| Volume snapshots | Fly.io | Automatic | 5 days |

An on-demand backup can be taken at any time before anything risky.

### Verified, not assumed
- **Volume restore, actually performed:** a snapshot was restored to a scratch
  volume, contents verified, and the test resources torn down. **Measured
  recovery time ≈ 30 seconds. Recovery point ≤ 24 hours.**
- **Database dump, actually retrieved:** a dump was downloaded from R2 and
  decompressed *outside* the application, confirming 27 tables and every matter
  and document record present and readable.
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
- **Every database query is scoped to the owning user in SQL**, not filtered
  after the fact. This is the failure class that has bitten the project before;
  it is now pinned by automated tests that fail the build if a new feature
  forgets it.
- **Solicitor features are role-gated** — verified exhaustively across all 41
  solicitor procedures.
- **Client portal links** expire in 30 days, can be revoked instantly by the
  solicitor, and are stored hashed.
- **Cross-site request forgery protection** and a **Content-Security-Policy**
  are enforced on every request.

---

## 5. Audit trail

Access to and export of client material is recorded: who, what, when, from
which address. Covered events include full matter-pack exports, portal link
creation and revocation, and sharing a proposal with a client.

Deliberately not a general request log — recording every list view would bury
the events that actually matter.

---

## 6. The professional-obligation question: what if Metis disappears?

A firm's file-retention obligations are its own, and "our vendor had it" is not
an answer. Three points:

1. **Export whenever you like.** Any matter exports as a single archive
   containing every document plus a summary. Nothing is held hostage.
2. **Intended practice-management integration.** A LEAP integration is in
   development — the finished file note and brief would land in your LEAP
   matter, which is already your system of record and already inside your own
   backup and retention regime. **It is not built yet** and nothing may be
   claimed as "integrates with LEAP" until it is.
3. **We do not push copies onto firm hardware,** and that is deliberate: a copy
   on an unmanaged laptop is one nobody can secure, audit, or delete on
   request.

---

## 7. Known gaps — stated plainly

A vendor who lists none of these is not being straight with you.

| Gap | Status |
|---|---|
| **No independent penetration test or third-party security audit** | Real. The code has been audited internally and the findings fixed; nobody external has tried to break it. |
| **No 24/7 automated intrusion monitoring** | One person checks manually. |
| **Single founder** | One person is the whole detection, response and continuity plan. A continuity arrangement is not yet documented. |
| **Overseas AI processing without a zero-retention agreement** | Matter content reaches Anthropic in the US under standard retention. Disclosed, not yet negotiated away. |
| **Subprocessor data-processing agreements not all confirmed executed** | In progress. |
| **Professional indemnity and cyber insurance not yet in force** | Blocks real client data on the solicitor side. |
| **Costs-disclosure wording not yet lawyer-reviewed** | The four s174 client-rights statements generate as a visible blank rather than invented text. Blocks real client use. |
| **No real client conference has ever been recorded through the product** | The pipeline is proven on pasted and synthetic transcripts only. |

---

## 8. ⚠️ Operator note — NOT for client distribution

**The encryption key is now a single point of failure for disaster recovery,
and it must be stored outside Fly.io.**

Fly secrets cannot be read back. If the Fly application is lost and the key
exists nowhere else, **the R2 database backups become permanently
undecryptable** — encryption would have made the disaster-recovery position
worse, not better.

Required sequence, and the key must never be handled anywhere it could be
logged or transcribed:

1. Generate and store it in a password manager first.
2. Then set it on Fly:
   ```
   flyctl secrets set FIELD_ENCRYPTION_KEY="<the value>" -a metis-cortex
   ```
3. Confirm the boot warning stops appearing in the logs.

Until it is set, the application logs a warning at every boot and the sensitive
columns are stored as plaintext — the state described in §2 is not yet in
force. Existing rows convert as they are rewritten; nothing needs migrating.

**Treat this key like the backups themselves. Losing it loses the data.**
