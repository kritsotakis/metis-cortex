const services: {
  name: string;
  headline: string;
  body: string;
  price: string;
}[] = [
  {
    name: "AI Strategy & Audit",
    headline: "Where are you bleeding time?",
    body: "Two-week paid audit. We map your workflows, find 2–3 automation opportunities, and hand you a 90-day roadmap with ROI per opportunity.",
    price: "From A$2,000",
  },
  {
    name: "AI Receptionist (Zoe)",
    headline: "Answer every call. Even at 11pm.",
    body: "Voice agent that handles overflow + after-hours calls, books into your CRM, and texts the caller with confirmation.",
    price: "From A$5,000 setup + A$1,500/mo",
  },
  {
    name: "Workflow Automation",
    headline: "Stop copy-pasting between tools.",
    body: "n8n / Make builds connecting your Xero, Jobber, ServiceM8, Brevo, Slack.",
    price: "From A$3,000",
  },
  {
    name: "Marketing Automation",
    headline: "Wake up the list you already have.",
    body: "Brevo / Mailchimp flows: welcome, nurture, post-purchase, win-back.",
    price: "From A$3,000 + A$500/mo",
  },
  {
    name: "Website (Astro / Cloudflare)",
    headline: "Fast, cheap, SEO-ready.",
    body: "Static site on Cloudflare. The same architecture we run on our own businesses.",
    price: "From A$5,000 + A$200/mo",
  },
  {
    name: "Custom AI Build",
    headline: "When the off-the-shelf options have run out.",
    body: "Bespoke agents, RAG systems, document processors, internal copilots.",
    price: "From A$10,000",
  },
];

export function ServiceStrip() {
  return (
    <section id="services" className="bg-bone py-24 sm:py-32">
      <div className="mx-auto max-w-6xl px-6 sm:px-10">
        <p className="mb-4 text-xs uppercase tracking-[0.22em] text-bronze">
          What we build
        </p>
        <h2 className="font-display max-w-3xl text-4xl leading-tight tracking-tight text-ink sm:text-5xl">
          Six service lines. One offer per engagement.
        </h2>
        <p className="mt-6 max-w-2xl text-base leading-relaxed text-ink-muted">
          We earn the next one. No 18-month &ldquo;platform&rdquo; promises.
        </p>

        <ul className="mt-16 divide-y divide-ink/10 border-y border-ink/10">
          {services.map((s) => (
            <li
              key={s.name}
              className="grid gap-4 py-7 sm:grid-cols-[1fr_2fr_auto] sm:items-baseline sm:gap-10"
            >
              <p className="font-display text-2xl leading-snug text-ink">
                {s.name}
              </p>
              <div>
                <p className="text-lg text-ink">{s.headline}</p>
                <p className="mt-2 text-sm leading-relaxed text-ink-muted">
                  {s.body}
                </p>
              </div>
              <p className="text-sm uppercase tracking-[0.14em] text-ink-muted sm:text-right">
                {s.price}
              </p>
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}
