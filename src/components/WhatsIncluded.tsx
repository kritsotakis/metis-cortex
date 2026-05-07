const items = [
  "AI voice + SMS picks up every call within 30 seconds, 24/7.",
  "Qualifies the caller, captures their job and address, books the appointment.",
  "Syncs to your existing calendar (Google, Outlook) and CRM (Jobber, ServiceM8, GHL).",
  "Done-for-you install in 14 days — no IT work on your side.",
  "Month-to-month after setup. Cancel anytime.",
];

export function WhatsIncluded() {
  return (
    <section className="bg-bone py-24 sm:py-32">
      <div className="mx-auto max-w-6xl px-6 sm:px-10">
        <div className="grid gap-16 lg:grid-cols-[1fr_1.4fr] lg:gap-24">
          <div>
            <p className="mb-4 text-xs uppercase tracking-[0.22em] text-gold">
              What you get
            </p>
            <h2 className="font-display text-4xl leading-tight tracking-tight text-ink sm:text-5xl">
              Frontline. Installed on your business in fourteen days.
            </h2>
            <p className="mt-6 text-base leading-relaxed text-ink-muted">
              Built on Retell AI for voice, GoHighLevel for CRM and workflow,
              and Twilio for numbers. We configure all of it. You answer five
              questions and approve the script.
            </p>
          </div>

          <ul className="divide-y divide-ink/10 border-y border-ink/10">
            {items.map((item, i) => (
              <li
                key={item}
                className="grid grid-cols-[auto_1fr] items-start gap-6 py-6"
              >
                <span className="font-display text-2xl text-gold">
                  {String(i + 1).padStart(2, "0")}
                </span>
                <p className="text-lg leading-relaxed text-ink">{item}</p>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}
