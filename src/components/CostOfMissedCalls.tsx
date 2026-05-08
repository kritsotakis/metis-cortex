const stats = [
  {
    figure: "30–40%",
    label: "of inbound calls",
    body: "Service businesses miss this many calls every week — usually outside hours, during jobs, or while on the other line.",
  },
  {
    figure: "A$380",
    label: "average lost booking",
    body: "Every missed call is roughly this much in lost booking value for a typical service business.",
  },
  {
    figure: "87%",
    label: "go to a competitor",
    body: "Of leads who don't reach you within 60 seconds, this share book somebody else instead.",
  },
];

export function CostOfMissedCalls() {
  return (
    <section className="bg-bone-soft py-24 sm:py-32">
      <div className="mx-auto max-w-6xl px-6 sm:px-10">
        <p className="mb-4 text-xs uppercase tracking-[0.22em] text-bronze">
          The cost of missed calls
        </p>
        <h2 className="font-display max-w-3xl text-4xl leading-tight tracking-tight text-ink sm:text-5xl">
          Every call you miss is a booking your competitor takes.
        </h2>

        <div className="mt-16 grid gap-px overflow-hidden rounded-lg bg-ink/10 sm:grid-cols-3">
          {stats.map((s) => (
            <div key={s.label} className="bg-bone-soft p-8 sm:p-10">
              <p className="font-display text-6xl text-ink">{s.figure}</p>
              <p className="mt-2 text-sm uppercase tracking-[0.16em] text-ink-muted">
                {s.label}
              </p>
              <p className="mt-6 text-base leading-relaxed text-ink-soft">
                {s.body}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
