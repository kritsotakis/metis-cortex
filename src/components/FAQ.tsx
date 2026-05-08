const faqs = [
  {
    q: "Will it sound robotic?",
    a: "No. Modern voice AI is indistinguishable from a human in normal conversation. Zoe introduces herself as an AI assistant for your business — no deception — but the voice is Australian, neutral, 30s. We'll send you a 30-second clip on request so you can hear it before the demo.",
  },
  {
    q: "What if Zoe messes up a booking or quote?",
    a: "Every call records, every transcription tags. Weekly review with you for the first 30 days to tune the script. If a customer ever complains about Zoe in the first month, we fix the underlying script + workflow within 24 hours or refund that month — written into the agreement.",
  },
  {
    q: "What does it integrate with?",
    a: "Out of the box: Jobber, ServiceM8, GoHighLevel, Cliniko, SevenRooms, NowBookIt, and Google Calendar. Most other CRMs via Zapier. If you have something exotic — legacy POS, custom-built — we'll tell you straight on the scoping call and quote a one-off integration if it's needed.",
  },
  {
    q: "Am I locked into a contract?",
    a: "No. Month-to-month after the 14-day install. Cancel anytime, full data export included. Founding-rate clients keep their A$800/mo rate for life regardless.",
  },
  {
    q: "What if my phone system isn't standard?",
    a: "We bring our own Twilio number and forward your existing one to it. That works with any phone setup — VoIP, mobile, landline, switchboard, or a hostess station with a multi-line handset.",
  },
  {
    q: "Why is the price so low?",
    a: "Founding-rate clients (first 5, one per vertical) get A$800/mo for life because we want their case-study data. Standard rate is A$1,200/mo, which is still under the cost of a part-time human receptionist (A$2,500–4,000/mo) and well below a custom AI agency build (A$5,000+ setup + A$3,000+/mo).",
  },
  {
    q: "But my hostess / receptionist / front desk never makes mistakes.",
    a: "We hear this most often from restaurants and clinics. Every operator we've installed has found at least 5 booking mistakes per month their team didn't know about — wrong night, wrong table size, missed dietary, wrong service code. We pull the data on Day 14 and show you. If you don't want it, refund.",
  },
  {
    q: "We already use SevenRooms / NowBookIt / Cliniko / Jobber. Why do I need this?",
    a: "Those handle web bookings — they don't pick up the phone. ~40% of bookings still come in by phone in service businesses. Zoe sits in front of your existing platform, handles the phone bookings, and writes them straight into your existing system. We integrate; we don't replace.",
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
      <div className="mx-auto max-w-4xl px-6 sm:px-10" id="faq">
        <p className="mb-4 text-xs uppercase tracking-[0.22em] text-bronze">
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
                  className="mt-1 inline-flex h-6 w-6 flex-none items-center justify-center text-ink/40 transition-transform group-open:rotate-45"
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
