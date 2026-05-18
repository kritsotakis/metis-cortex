const hooks: { headline: string; body: string }[] = [
  {
    headline: "The 7pm call you'll miss tonight.",
    body: "AI Receptionist handles overflow + after-hours, qualifies the caller, books straight into your CRM, and texts the caller with confirmation. Zero rings to voicemail.",
  },
  {
    headline: "The A$4,200 invoice that's 60 days overdue.",
    body: "Workflow automation chases politely, persistently, in your voice. Email + SMS keyed to invoice age, payment link baked in. You only step in when the system can't.",
  },
  {
    headline: "The same FAQ you've answered nine times this week.",
    body: "AI-drafted client comms — a button in your inbox writes a reply in your house style. You read, edit if needed, send. You stay in control. The typing disappears.",
  },
];

export function WhatStopsBleeding() {
  return (
    <section className="bg-bone py-24 sm:py-32">
      <div className="mx-auto max-w-6xl px-6 sm:px-10">
        <p className="mb-4 text-xs uppercase tracking-[0.22em] text-bronze">
          What stops bleeding
        </p>
        <h2 className="font-display max-w-3xl text-4xl leading-tight tracking-tight text-ink sm:text-5xl">
          Three things service businesses leak every week. We build the systems
          that stop the leak.
        </h2>

        <ol className="mt-16 grid gap-px overflow-hidden rounded-lg bg-ink/10 sm:grid-cols-3">
          {hooks.map((hook) => (
            <li key={hook.headline} className="flex flex-col gap-5 bg-bone p-10">
              <p className="font-display text-2xl leading-snug text-ink">
                {hook.headline}
              </p>
              <p className="text-base leading-relaxed text-ink-soft">
                {hook.body}
              </p>
            </li>
          ))}
        </ol>

        <p className="mt-10 max-w-2xl text-sm leading-relaxed text-ink-muted">
          These aren&rsquo;t theory. They&rsquo;re what we&rsquo;re solving in
          our own businesses right now.
        </p>
      </div>
    </section>
  );
}
