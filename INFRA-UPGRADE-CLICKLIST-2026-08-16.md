# Infrastructure upgrades — what's built, what needs your hands (2026-08-16)

Everything code-side is deployed (v152). Four things need your account or card. Each is a few minutes; do them in this order.

## Built and live
- **Second backup target** — DB dumps write to Cloudflare R2 *and* Amazon S3 Sydney once `BACKUP_S3_*` secrets exist. Encrypted before upload either way.
- **Weekly restore rehearsal** — Mondays after the dump: fetch newest (S3 preferred), decrypt, gunzip, parse, reconcile every table's row count against live; logged. `pnpm restore:check` on demand.
- **Bedrock adapter** — when `BEDROCK_*` secrets exist, Claude inference runs in `ap-southeast-2` (Sydney) instead of the global Anthropic API. Same behaviour, same rails.
- **Opus for solicitor drafting** — `DRAFTING_MODEL=claude-opus-5` set on prod (briefs, proposals, costs docs). Client chat/triage stay on the chat model.
- **Security & Trust page** at metiscortex.au/security, `/.well-known/security.txt`, footer entity line, "early software / small business" framing retired everywhere (agreement re-accept prompted).

## 1. Cloudflare — proxy on + Pro (~US$20/mo)
Today the site is **not** behind Cloudflare (DNS only; traffic hits Fly directly). 
1. dash.cloudflare.com → metiscortex.au → **DNS** → for the `A`/`CNAME` records of `metiscortex.au` and `www`, click the grey cloud → **orange (Proxied)**. Leave `_acme-challenge`/mail records DNS-only.
2. **SSL/TLS** → Overview → **Full (strict)**. (Fly serves a valid cert; anything less than Full-strict is a downgrade.)
3. **Plan** → upgrade to **Pro** → then **Security → WAF**: enable *Cloudflare Managed Ruleset* and *OWASP Core Ruleset*; **Security → Bots**: turn on Bot Fight Mode; **Security → WAF → Rate limiting rules**: add one rule — path contains `/api/trpc/auth` → 30 requests / 10 min / IP → block.
4. Tell me when it's on; I'll re-test the origin guard and WebSocket through the proxy (Cloudflare needs WebSockets enabled under **Network** — it's on by default).

## 2. AWS account (card) → S3 Sydney bucket + IAM user
1. aws.amazon.com → create account (use info@metiscortex.au; the trust as the entity). Enable MFA on the root user, then stop using root.
2. **S3** → Create bucket → name `metis-cortex-backups`, region **ap-southeast-2 (Sydney)**, Block all public access ON, default encryption SSE-S3, **Object Lock enabled** (governance mode, 35 days) so a compromised key can't delete backups.
3. **IAM** → Users → Create `metis-backup-writer` → attach an inline policy allowing only `s3:PutObject, s3:GetObject, s3:ListBucket` on that bucket → create **access key** (Application running outside AWS).
4. Then run (paste the two values yourself):
```bash
flyctl secrets set BACKUP_S3_BUCKET=metis-cortex-backups BACKUP_S3_REGION=ap-southeast-2 BACKUP_S3_ACCESS_KEY_ID=… BACKUP_S3_SECRET_ACCESS_KEY=… -a metis-cortex
```
Next boot's dump will land in both buckets and the Monday rehearsal will prefer S3.

## 3. Bedrock (same AWS account) → Sydney inference
1. Console → **Amazon Bedrock** → region **ap-southeast-2** → **Model access** → request access to **Anthropic Claude** models (Opus + Sonnet). Approval is usually minutes to hours.
2. Note the two **model IDs** shown for the Sydney region (they look like `apac.anthropic.claude-…`). One for drafting (Opus), one for chat (Sonnet).
3. IAM → user `metis-bedrock` → inline policy allowing `bedrock:InvokeModel` on those model ARNs → access key.
4. Run:
```bash
flyctl secrets set BEDROCK_REGION=ap-southeast-2 BEDROCK_ACCESS_KEY_ID=… BEDROCK_SECRET_ACCESS_KEY=… BEDROCK_DRAFTING_MODEL_ID=… BEDROCK_CHAT_MODEL_ID=… -a metis-cortex
```
From that boot, all Claude calls run in Sydney; I'll then change the Privacy/Security pages from "global routing" to "processed in Sydney".

## 4. Two secrets + two sign-offs (yours only)
```bash
flyctl secrets set BACKUP_ENCRYPTION_KEY="$(openssl rand -base64 48)" -a metis-cortex
```
— save that value in the password manager next to FIELD_ENCRYPTION_KEY. Then: request Anthropic zero-data-retention + DPA (console → Privacy/Legal, or sales), and Deepgram DPA (dashboard → Legal). Enrol TOTP on your solicitor account so I can make it mandatory.

## Cost picture
Cloudflare Pro ~US$20/mo · S3 Sydney: cents/month at our size · Bedrock: per-token, same order as the direct API · Opus drafting: ~5× Sonnet per document, at our volume tens of dollars/month.
