const faqs = [
  {
    q: "Will it sound robotic?",
    a: "No. Modern voice AI is indistinguishable from a human in normal conversation — we'll send you a 30-second demo clip on request so you can hear it before the call.",
  },
  {
    q: "What if it messes up a lead?",
    a: "Every call falls back to a human if the AI can't handle it, every call is recorded, and we do a weekly review with you for the first month to tune the script.",
  },
  {
    q: "What does it integrate with?",
    a: "Jobber, ServiceM8, GoHighLevel, and Google Calendar out of the box. Most other CRMs via Zapier. If you have something exotic, we'll tell you straight on the scoping call.",
  },
  {
    q: "Am I locked into a contract?",
    a: "No. Month-to-month after the 14-day install. Cancel any time, no exit fee.",
  },
  {
    q: "What if my phone system isn't standard?",
    a: "We bring our own number and forward your existing one to it. That works with any phone setup — VoIP, mobile, landline, or a switchboard.",
  },
  {
    q: "Why is this so cheap?",
    a: "Because we built it on our own cleaning business (DSK) before we sold it externally. You're getting the version we already trust enough to use ourselves.",
  },
];

const faqJsonLd = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: faqs.map((f) => ({
    "@type": "Question",
    name: f.q,
    acceptedAnswer: { "@type": "Answer", text: f.a },
  })),
};

export function FAQ() {
  return (
    <section className="bg-bone py-24 sm:py-32">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqJsonLd) }}
      />
      <div className="mx-auto max-w-4xl px-6 sm:px-10">
        <p className="mb-4 text-xs uppercase tracking-[0.22em] text-gold">
          Questions we get
        </p>
        <h2 className="font-display text-4xl leading-tight tracking-tight text-ink sm:text-5xl">
          Straight answers.
        </h2>

        <div className="mt-12 divide-y divide-ink/10 border-y border-ink/10">
          {faqs.map((faq) => (
            <details
              key={faq.q}
              className="group py-6 [&_summary::-webkit-details-marker]:hidden"
            >
              <summary className="flex cursor-pointer items-start justify-between gap-6 text-lg font-medium text-ink list-none">
                <span>{faq.q}</span>
                <span
                  aria-hidden="true"
                  className="mt-1 inline-flex h-6 w-6 flex-none items-center justify-center text-gold transition-transform group-open:rotate-45"
                >
                  +
                </span>
              </summary>
              <p className="mt-4 max-w-3xl text-base leading-relaxed text-ink-muted">
                {faq.a}
              </p>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
}
