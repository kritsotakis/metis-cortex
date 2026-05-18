const faqs = [
  {
    q: "Why should I trust you — you're not a household name?",
    a: "Fair. I'm not. I'm an operator who's run things for 30 years and decided to build AI for service businesses because nobody was building it the way I'd want it sold to me. Six years of enterprise IT (MCSE, Cisco, Citrix) before the restaurant. 21 years running Limani Seafood in Narrabeen. Currently building four service businesses of my own. Every system I sell, I install on one of my four first. That's the entire pitch. If 'someone who's been in your seat building real systems for 30 years' isn't enough — there are agencies with bigger logos. They charge more and use the same tools.",
  },
  {
    q: "How do you actually price this?",
    a: "AI Audit from A$2,000 (the front door — a 2-week paid engagement that produces a 90-day roadmap with ROI per opportunity). Builds priced individually depending on scope — AI Receptionist starts at A$5,000 setup + A$1,500/mo, Workflow Automation at A$3,000 setup + A$500/mo retainer, full Custom AI at A$10,000+. We earn the right to the next offer. No bundling, no 18-month minimums, no 'platform fees'.",
  },
  {
    q: "Will Zoe (the AI receptionist) sound robotic to my customers?",
    a: "No. Modern voice AI is indistinguishable from a human in normal conversation. Zoe introduces herself as an AI assistant for your business — no deception — and the voice is Australian, neutral, calm. We'll send a 30-second sample on request so you can hear it before booking. Every call is recorded and transcribed; we tune weekly for the first 30 days post-install.",
  },
  {
    q: "What if it doesn't work?",
    a: "The AI Audit has a mini-guarantee — if at the walkthrough call you don't see at least one opportunity worth A$10,000/year to your business, we refund the difference between what you paid and A$500 (to cover our work). Build engagements: month-to-month after install, no lock-in, full data export if you exit. We're not playing the 'lock you into a 24-month contract and hope you forget to cancel' game. If something we install doesn't earn its keep, you walk.",
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
