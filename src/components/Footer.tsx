import { CONTACT, LEGAL, PRICING, SITE, SOCIAL, asicLine, contactEmail, priceFormatAud } from "@/lib/site";

export function Footer() {
  const email = contactEmail();
  const linkedinHref = SOCIAL.linkedinCompany ?? SOCIAL.linkedinPersonal;
  const linkedinLabel = SOCIAL.linkedinCompany ? "LinkedIn" : "LinkedIn (founder)";

  return (
    <footer className="bg-bone border-t border-ink/10 py-14">
      <div className="mx-auto grid max-w-6xl gap-10 px-6 sm:px-10 lg:grid-cols-[1.2fr_1fr_1fr]">
        <div>
          <div aria-label={SITE.name} className="flex items-center gap-3">
            <img
              src="/brand/logo-mark-transparent-128.png"
              alt=""
              width={40}
              height={40}
              className="h-10 w-10"
            />
            <p className="font-display text-2xl font-medium tracking-tight text-ink">
              Metis<span aria-hidden="true" className="mx-1 text-gold">·</span>Cortex
            </p>
          </div>
          <p className="mt-3 max-w-sm text-sm leading-relaxed text-ink-muted">
            {SITE.name} is a registered business name of the {LEGAL.trustName}.
            Sydney, Australia.
          </p>
          <p className="mt-2 text-xs text-ink-muted">
            ABN {LEGAL.abn} · Trustee: {LEGAL.trusteeName} (ACN {LEGAL.trusteeAcn}) · {asicLine()}.
          </p>
          <p className="mt-3 text-xs text-ink-muted">
            Founding rate {priceFormatAud(PRICING.foundingMonthlyAud)}/mo for first{" "}
            {PRICING.foundingClientCap} case-study clients; {priceFormatAud(PRICING.monthlyAud)}/mo
            standard thereafter.
          </p>
        </div>

        <div>
          <p className="text-xs uppercase tracking-[0.18em] text-ink-muted">
            Contact
          </p>
          <ul className="mt-3 space-y-2 text-sm text-ink">
            <li>
              <a href={`mailto:${email}`} className="hover:text-gold">
                {email}
              </a>
            </li>
            <li>
              <a
                href={`tel:${CONTACT.phoneE164}`}
                className="hover:text-gold"
              >
                {CONTACT.phoneDisplay}
              </a>
            </li>
            <li>
              <a
                href={linkedinHref}
                target="_blank"
                rel="noopener noreferrer"
                className="hover:text-gold"
              >
                {linkedinLabel}
              </a>
            </li>
          </ul>
        </div>

        <div>
          <p className="text-xs uppercase tracking-[0.18em] text-ink-muted">
            Legal
          </p>
          <ul className="mt-3 space-y-2 text-sm text-ink">
            <li>
              <a href="/privacy" className="hover:text-gold">
                Privacy policy
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div className="mx-auto mt-12 max-w-6xl px-6 sm:px-10">
        <div className="rule" />
        <p className="mt-6 text-xs text-ink-muted">
          © {new Date().getFullYear()} {LEGAL.trustName}. All rights reserved.
        </p>
      </div>
    </footer>
  );
}
