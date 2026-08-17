# AWS Support case — Anthropic models return AccessDenied despite an accepted agreement

**Raise at:** https://support.console.aws.amazon.com/support/home#/case/create
**Type:** Account and billing → Service: Bedrock → Category: Model access / General guidance
(Basic support can raise account-and-service cases at no cost.)
**Severity:** General guidance
**Subject:** `Bedrock: Anthropic Claude models return AccessDenied though agreement status is AVAILABLE (ap-southeast-4)`

---

## Case body — paste as is

Account: 593011452315
Region: ap-southeast-4 (Melbourne, enabled). Same result from ap-southeast-2.
Models: anthropic.claude-sonnet-5 and anthropic.claude-opus-5 (also anthropic.claude-opus-4-8).

Every InvokeModel call against an Anthropic model fails with:

    AccessDeniedException: anthropic.claude-sonnet-5 is not available for this account.
    You can explore other available models on Amazon Bedrock. For additional access
    options, contact AWS Sales.

This does not match the account state. `bedrock get-foundation-model-availability`
returns, for both models, in ap-southeast-4:

    agreementAvailability.status = AVAILABLE
    authorizationStatus          = AUTHORIZED
    entitlementAvailability      = AVAILABLE
    regionAvailability           = AVAILABLE

Steps already completed:
1. Submitted the Anthropic use-case details form in the Bedrock console (the
   account-level form; the per-model "Model access" page is retired).
2. Accepted the AWS Marketplace model agreements for Claude Sonnet 5 and
   Claude Opus 5 via `bedrock create-foundation-model-agreement`. Confirmation
   emails received from AWS Marketplace on 16 August 2026 (Seller: Anthropic,
   PBC; purchase amount 0.00 USD). Agreement status went PENDING → AVAILABLE
   within about a minute.
3. Waited ~16 hours and retried. Same AccessDeniedException.

Evidence that the problem is specific to Anthropic models rather than the
account, the region or our IAM policy — all from the same IAM user and region:

- `apac.amazon.nova-lite-v1:0` in ap-southeast-4: **succeeds**, returns a
  normal completion. So the credentials, the region and Bedrock runtime
  access are all working.
- `au.anthropic.claude-sonnet-5`, `au.anthropic.claude-opus-5` and
  `au.anthropic.claude-opus-4-8` in ap-southeast-4: **AccessDeniedException**
  ("not available for this account").
- The same Anthropic model ID invoked in ap-southeast-2 gives the identical
  AccessDeniedException, so it is not region-specific.
- `bedrock list-inference-profiles --region ap-southeast-4` lists the AU geo
  profiles for both models, with the expected foundation-model ARNs, so the
  IDs and ARNs are correct.

IAM: the calling user has an inline policy allowing bedrock:InvokeModel and
bedrock:InvokeModelWithResponseStream on the two AU inference-profile ARNs and
on the corresponding foundation-model ARNs in ap-southeast-2 and
ap-southeast-4. An IAM denial would return a different message ("not
authorized to perform"), and the same policy is what the successful Nova call
used.

Request: please enable Anthropic model access for this account, or tell us
what step remains. If there is an outstanding review on the use-case
submission, please advise its status and whether anything further is needed
from us.

Business context, in case it is relevant to the review: we are an Australian
legal-technology product (metiscortex.au) operated by Kritsotakis Investments
Pty Ltd ATF Kritsotakis Family Trust. We are already an Anthropic API customer
in production; the reason for moving to Bedrock is data residency — the AU geo
inference profiles keep inference within Australia, which our clients (law
firms) ask about. Our production traffic is currently served by the direct
Anthropic API, so this is not an outage for us, but it is blocking a
residency commitment we would like to be able to make.

---

## Notes for whoever files this

- **Nothing is broken in production.** Metis falls back to the direct Anthropic API automatically and logs each fallback (v160). Users are unaffected.
- Do not delete or re-create the model agreements — they are correct. Re-running the flow would only muddy the case.
- If Support asks for a request ID, re-run the failing call and copy it from the error; ask Code to run it and hand you the ID.
- If Support says the account needs to "contact AWS Sales", that is the boilerplate in the error text, not necessarily a real requirement — push back once with the evidence above before agreeing to a sales call.
