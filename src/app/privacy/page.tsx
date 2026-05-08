import type { Metadata } from "next";
import Link from "next/link";
import { CONTACT, LEGAL, SITE, contactEmail } from "@/lib/site";

const EFFECTIVE_DATE = "9 May 2026 (revised after Manus privacy review)";

export const metadata: Metadata = {
  title: `Privacy policy — ${SITE.name}`,
  description: `How ${SITE.name} collects, uses, stores, and discloses personal information under the Australian Privacy Act 1988.`,
  alternates: { canonical: "/privacy" },
  robots: { index: true, follow: true },
};

export default function PrivacyPage() {
  const email = contactEmail();
  return (
    <main className="bg-bone text-ink">
      <header className="mx-auto max-w-3xl px-6 pt-12 sm:px-10">
        <Link
          href="/"
          aria-label={SITE.name}
          className="inline-flex items-center gap-3 transition-opacity hover:opacity-80"
        >
          <img
            src="/brand/metiscortex-horizontal-lockup-transparent.png"
            alt={SITE.name}
            className="h-9 w-auto"
          />
        </Link>
      </header>

      <article className="mx-auto max-w-3xl px-6 py-16 sm:px-10 sm:py-20">
        <p className="mb-4 inline-flex items-center gap-3 text-xs uppercase tracking-[0.22em] text-bronze">
          <span className="h-px w-8 bg-bronze" />
          Privacy policy
        </p>
        <h1 className="font-display text-[clamp(2.5rem,6vw,4rem)] font-semibold leading-[1.05] tracking-tight">
          How we handle your information.
        </h1>
        <p className="mt-4 text-sm text-ink-muted">
          Effective {EFFECTIVE_DATE}.
        </p>

        <div className="prose-content mt-12 space-y-8 text-base leading-relaxed text-ink/85">
          <section>
            <p>
              {SITE.name} is a registered business name of the {LEGAL.trustName}{" "}
              (ABN {LEGAL.abn}), trustee {LEGAL.trusteeName} (ACN{" "}
              {LEGAL.trusteeAcn}). This policy explains how we handle personal
              information under the{" "}
              <em>Privacy Act 1988</em> (Cth) and the Australian Privacy
              Principles (APPs).
            </p>
            <p className="mt-4">
              We collect as little personal information as we can to do our
              work, and we don&rsquo;t sell it. If you don&rsquo;t want us to
              hold information about you, don&rsquo;t send it to us — though
              that limits what we can do for you.
            </p>
          </section>

          <section>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              1. What we collect
            </h2>
            <p className="mt-3">
              Depending on how you interact with us, we may collect:
            </p>
            <ul className="mt-3 list-disc space-y-2 pl-6">
              <li>
                <strong>Booking enquiries:</strong> name, business name, email,
                phone number, and the answers you give to demo qualifying
                questions when you book a call via our scheduling tool
                (Calendly).
              </li>
              <li>
                <strong>Email correspondence:</strong> any information you
                include when you email us at {email}.
              </li>
              <li>
                <strong>Server and security logs:</strong> our hosting and
                security provider (Cloudflare) keeps standard request logs —
                IP address, user agent, requested URL, timestamp — used to
                serve the site and protect it from abuse.
              </li>
              <li>
                <strong>Pilot and customer data:</strong> if you become a
                pilot or paying customer, we will hold the information needed
                to deliver the service — lead notes, billing details, and
                integration credentials you choose to share.
              </li>
              <li>
                <strong>Call recordings and transcripts:</strong> when a
                caller interacts with our AI voice agent (Zoe), we record the
                audio and generate a text transcript. We use these recordings
                to provide the service, qualify leads, and improve system
                accuracy. We do not use your voice data to train third-party
                foundational AI models. Callers are informed that the call is
                recorded at the start of every call. You may request deletion
                of your call recordings by contacting us.
              </li>
            </ul>
          </section>

          <section>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              2. Why we collect it
            </h2>
            <ul className="mt-3 list-disc space-y-2 pl-6">
              <li>To respond to your enquiry and run a demo call.</li>
              <li>
                To deliver the Metis Cortex service to pilot and paying
                customers.
              </li>
              <li>To send you scheduling confirmations and follow-ups.</li>
              <li>
                To meet legal, accounting, and tax obligations under
                Australian law.
              </li>
              <li>
                To protect the site and our customers&rsquo; data from misuse,
                fraud, and abuse.
              </li>
            </ul>
            <p className="mt-4">
              We rely on the lawful bases of consent (you give us your
              information knowing why), contract (delivering the service you
              signed up for), and legitimate interest (running and securing
              the business).
            </p>
          </section>

          <section>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              3. Who we share it with
            </h2>
            <p className="mt-3">
              We use a small number of trusted service providers to operate.
              Each holds only the data they need:
            </p>
            <ul className="mt-3 list-disc space-y-2 pl-6">
              <li>
                <strong>Calendly</strong> — appointment scheduling. Stores the
                booking details you submit. Calendly is based in the United
                States.
              </li>
              <li>
                <strong>Cloudflare</strong> — site hosting, DNS, and security.
                Sees standard request data. Cloudflare operates globally with
                Australian edge locations.
              </li>
              <li>
                <strong>Google Workspace</strong> — email, documents, and
                calendar. Used for our internal correspondence and any
                customer files you send us. Google Workspace data is held in
                the United States.
              </li>
              <li>
                <strong>Pilot and customer infrastructure</strong> — Retell AI
                (call agent), GoHighLevel (CRM and workflows), Twilio
                (telephony) and similar tools used to deliver the Metis Cortex
                service. We will tell you specifically which tools handle
                your data when you onboard as a pilot or customer.
              </li>
              <li>
                <strong>Professional advisers</strong> — our accountant,
                bookkeeper, and lawyer, where they need information to do
                their work. Each is bound by confidentiality.
              </li>
              <li>
                <strong>Authorities</strong> — where required by law (for
                example, the ATO, ASIC, or a valid court order).
              </li>
            </ul>
            <div className="mt-6 rounded-md border-l-2 border-bronze/60 bg-bone-soft px-5 py-4">
              <p className="font-medium text-ink">
                How we share your data — and how we don&rsquo;t.
              </p>
              <p className="mt-2">
                We are in the business of answering your phones, not selling
                your data.
              </p>
              <ul className="mt-3 list-disc space-y-1 pl-6">
                <li>
                  We <strong>do not</strong> sell your customer lists or lead
                  data to anyone.
                </li>
                <li>
                  We <strong>do not</strong> share your data with advertisers.
                </li>
                <li>
                  We <strong>do not</strong> allow our AI providers (like
                  Retell AI) to use your private conversations to train their
                  public models.
                </li>
              </ul>
              <p className="mt-3">
                We only share data with the specific software providers (like
                GoHighLevel and Twilio) needed to make your AI receptionist
                work.
              </p>
            </div>
          </section>

          <section>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              4. Overseas data storage
            </h2>
            <p className="mt-3">
              We use third-party service providers located outside of
              Australia, primarily in the <strong>United States</strong>{" "}
              (including Retell AI, GoHighLevel, Twilio, Calendly, and Google
              Workspace). By using our service, you consent to the transfer
              of your personal information to these overseas locations.
            </p>
            <p className="mt-4">
              In line with our obligations under{" "}
              <strong>Australian Privacy Principle 8.1</strong>, we take
              reasonable steps to ensure these providers handle your personal
              information in a manner consistent with the Australian Privacy
              Principles.
            </p>
          </section>

          <section>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              5. How long we keep it
            </h2>
            <p className="mt-3">
              We keep personal information only for as long as we have a
              reason to. Booking enquiries that don&rsquo;t become customers
              are deleted within 12 months unless you ask us to delete them
              sooner. Customer records, billing data, and tax records are
              kept for the period required by Australian law (typically up
              to seven years).
            </p>
          </section>

          <section>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              6. How we keep it safe
            </h2>
            <p className="mt-3">
              We take <strong>reasonable steps</strong> to protect your
              personal information from misuse, interference, and loss, in
              line with{" "}
              <strong>Australian Privacy Principle 11</strong>. This includes
              using encrypted connections (HTTPS/TLS) and requiring strong
              authentication for systems that access customer data.
            </p>
            <p className="mt-4">
              No system is perfect. If a data breach happens that is likely
              to cause serious harm, we will notify you and the Office of the
              Australian Information Commissioner (OAIC) as required by the
              Notifiable Data Breaches scheme.
            </p>
          </section>

          <section>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              7. Cookies and analytics
            </h2>
            <p className="mt-3">
              The site uses minimal cookies. Cloudflare may set a small
              number for security and bot-protection purposes. We do not run
              advertising or cross-site tracking cookies. If we add
              site-analytics in future, we&rsquo;ll prefer privacy-respecting
              tools that don&rsquo;t identify individual visitors and
              we&rsquo;ll update this policy.
            </p>
          </section>

          <section>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              8. Your rights
            </h2>
            <p className="mt-3">Under the Privacy Act and the APPs, you can:</p>
            <ul className="mt-3 list-disc space-y-2 pl-6">
              <li>Ask what personal information we hold about you;</li>
              <li>
                Ask us to correct it if it&rsquo;s wrong, out of date, or
                incomplete;
              </li>
              <li>
                Ask us to delete it — including call recordings and
                transcripts — subject to records we&rsquo;re required by law
                to keep;
              </li>
              <li>Withdraw consent for future communications at any time;</li>
              <li>Make a complaint about how we&rsquo;ve handled your data.</li>
            </ul>
            <p className="mt-4">
              Email{" "}
              <a className="underline hover:text-bronze" href={`mailto:${email}`}>
                {email}
              </a>{" "}
              and we&rsquo;ll respond within 30 days. We may need to verify
              your identity before acting on a request.
            </p>
          </section>

          <section>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              9. Complaints
            </h2>
            <p className="mt-3">
              If you&rsquo;re not happy with how we&rsquo;ve handled your
              information, please contact us first at{" "}
              <a className="underline hover:text-bronze" href={`mailto:${email}`}>
                {email}
              </a>
              . If the issue isn&rsquo;t resolved, you can complain to the
              Office of the Australian Information Commissioner at{" "}
              <a
                className="underline hover:text-bronze"
                href="https://www.oaic.gov.au/"
                target="_blank"
                rel="noopener noreferrer"
              >
                oaic.gov.au
              </a>
              .
            </p>
          </section>

          <section>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              10. Changes to this policy
            </h2>
            <p className="mt-3">
              We may update this policy as the business changes. The
              effective date at the top of the page tells you when it was
              last updated. Material changes will be flagged on the site and,
              for active customers, by email.
            </p>
          </section>

          <section>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              11. Contact
            </h2>
            <p className="mt-3">
              {SITE.name} (a registered business name of the {LEGAL.trustName},
              ABN {LEGAL.abn}).
              <br />
              Email:{" "}
              <a className="underline hover:text-bronze" href={`mailto:${email}`}>
                {email}
              </a>
              <br />
              Phone: {CONTACT.phoneDisplay}
              <br />
              Sydney, NSW, Australia.
            </p>
          </section>
        </div>

        <div className="mt-16">
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-sm uppercase tracking-[0.18em] text-ink-muted hover:text-ink"
          >
            <span aria-hidden="true">←</span> Back to home
          </Link>
        </div>
      </article>
    </main>
  );
}
