import type { Metadata } from "next";
import Link from "next/link";
import { CTAButton } from "@/components/CTAButton";
import { Footer } from "@/components/Footer";
import { SITE } from "@/lib/site";

export const metadata: Metadata = {
  title: `7-Question Operations Audit Checklist · ${SITE.name}`,
  description:
    "Seven questions a service-business owner can ask themselves to surface their biggest automation opportunity. The same checklist we run on our own four businesses.",
  alternates: { canonical: "/audit-checklist" },
  robots: { index: true, follow: true },
};

const questions: { n: string; q: string; why: string; signal: string }[] = [
  {
    n: "01",
    q: "How many calls did you miss last week — including after-hours, weekends, lunch rush, and ones you saw but didn't pick up?",
    why: "Service businesses lose A$200–A$600 per missed call on average (varying by job value). Most owners underestimate this by 3×. The number itself is rarely smaller than 8/week.",
    signal:
      "If your honest answer is 10+ calls/week, an AI receptionist pays for itself inside 30 days. If under 5, look at the other six questions first — phones aren't your leak.",
  },
  {
    n: "02",
    q: "What's your oldest unpaid invoice as of today — and what's the dollar value of everything over 60 days?",
    why: "Accounts receivable over 60 days correlates with operational chaos more than with bad customers. The fix is rarely 'chase harder' — it's 'chase systematically, with payment links baked in, before the relationship gets awkward'.",
    signal:
      "If you can't answer this in 30 seconds, you don't have an AR system, you have a vague feeling. If your 60+ day AR is more than 10% of monthly revenue, automated invoice chasing recovers that in 90 days.",
  },
  {
    n: "03",
    q: "What's the same email you've written more than five times in the past month?",
    why: "Repeat emails are the operator's tax — every one costs 3–8 minutes of focused attention you'll never get back. Most owners don't realise how many they write until they list them.",
    signal:
      "If you can name three of them off the top of your head, an AI-drafted client comms tool gives you back 5+ hours/week. The button writes a draft in your voice; you read, edit if needed, send.",
  },
  {
    n: "04",
    q: "What data gets manually copied between two SaaS tools every week — and who does the copying?",
    why: "Manual data shuffle between tools is the #1 source of operational drag in growing service businesses. The owner often doesn't see it because a staff member absorbs it silently.",
    signal:
      "If the answer involves you OR a senior staff member spending 2+ hours/week on this, workflow automation pays for itself inside two months. n8n / Make can connect almost anything.",
  },
  {
    n: "05",
    q: "How many hours per week do you (the owner) personally spend on admin tasks below your A$/hr equivalent value?",
    why: "Owner admin time is hidden cost. If you bill out at A$200/hr but spend 10 hours/week typing invoice details into Xero, that's A$2,000/week of value evaporating because the systems aren't doing the work.",
    signal:
      "If the answer is more than 5 hours/week, you're not running a business — you're working in your business as a clerk. That's where the audit roadmap kicks in.",
  },
  {
    n: "06",
    q: "If a customer texts you at 9pm with a job request, when does it actually get logged into your CRM or job-management system?",
    why: "After-hours capture is where most service businesses bleed quietly. The job either gets remembered in your head (and forgotten), captured on a sticky note (and lost), or entered tomorrow morning (after the customer has already called your competitor).",
    signal:
      "If the honest answer is 'tomorrow morning, sometimes' — you need an AI receptionist OR a workflow that auto-routes inbound texts to your CRM. Both are off-the-shelf at this point.",
  },
  {
    n: "07",
    q: "What's the one recurring document or report that takes more than a week to chase data for — every quarter or every year?",
    why: "BAS, EOFY tax docs, year-end accounting handover, annual compliance, quarterly board reports. Every operator has at least one. The chase is the worst part; the actual production rarely is.",
    signal:
      "If the chase consistently eats more than a week per cycle, an automated document-collection workflow (with reminders, secure upload links, AI-parsed inbox triage) cuts that to 1–2 days. Real, today.",
  },
];

export default function AuditChecklistPage() {
  return (
    <main className="bg-bone-soft min-h-screen">
      <section className="bg-ink text-bone py-20 sm:py-28">
        <div className="mx-auto max-w-4xl px-6 sm:px-10">
          <p className="mb-6 text-xs uppercase tracking-[0.22em] text-bone/55">
            <Link href="/" className="hover:text-bone">← Metis Cortex</Link>
          </p>
          <h1 className="font-display text-[clamp(2.25rem,5vw,4.5rem)] leading-[1.05] tracking-tight text-bone">
            The 7-question operations audit.
            <br />
            <span className="mc-italic-display text-bone/80">
              The same one we run on our own businesses.
            </span>
          </h1>
          <p className="mt-8 max-w-2xl text-lg leading-relaxed text-bone/80">
            Sit with these seven questions for ten minutes. Answer them
            honestly — not aspirationally. The pattern that emerges from your
            answers tells you which automation will pay for itself first.
          </p>
          <p className="mt-6 max-w-2xl text-base leading-relaxed text-bone/65">
            This isn&rsquo;t a sales funnel disguised as a quiz. There&rsquo;s
            no email gate. You read it, you keep it. If two or more of your
            answers worry you, book the operator call at the bottom and
            we&rsquo;ll talk about which one to fix first.
          </p>
        </div>
      </section>

      <section className="py-24 sm:py-32">
        <div className="mx-auto max-w-4xl px-6 sm:px-10">
          <ol className="space-y-16">
            {questions.map((item) => (
              <li
                key={item.n}
                className="grid gap-6 sm:grid-cols-[auto_1fr] sm:gap-10"
              >
                <span className="font-display text-5xl text-bronze/70 leading-none">
                  {item.n}
                </span>
                <div>
                  <p className="font-display text-2xl leading-snug text-ink sm:text-3xl">
                    {item.q}
                  </p>
                  <p className="mt-5 text-base leading-relaxed text-ink-soft">
                    <span className="font-semibold text-ink">
                      Why this one:
                    </span>{" "}
                    {item.why}
                  </p>
                  <p className="mt-3 text-base leading-relaxed text-ink-soft">
                    <span className="font-semibold text-ink">
                      What the signal means:
                    </span>{" "}
                    {item.signal}
                  </p>
                </div>
              </li>
            ))}
          </ol>

          <div className="mt-24 rounded-lg border border-ink/10 bg-bone p-10">
            <p className="text-xs uppercase tracking-[0.22em] text-bronze">
              The pattern
            </p>
            <h2 className="mt-3 font-display text-3xl leading-tight text-ink sm:text-4xl">
              If two or more answers worried you — let&rsquo;s talk.
            </h2>
            <p className="mt-6 text-base leading-relaxed text-ink-soft">
              The 15-minute operator call is free. No SDR — you&rsquo;ll
              actually talk to me. I&rsquo;ll tell you straight whether AI
              fixes your top-two answers, whether the fix is something else
              (hiring, process, software you already own), or whether we
              shouldn&rsquo;t work together. About 1 in 3 calls ends with
              &ldquo;you don&rsquo;t need us, you need X&rdquo; — and we say
              that, because the alternative is wasting both our afternoons.
            </p>
            <div className="mt-8">
              <CTAButton surface="bone">Book a 15-min operator call</CTAButton>
            </div>
          </div>

          <p className="mt-12 text-center text-sm text-ink-muted">
            <Link href="/" className="hover:text-bronze">
              ← Back to Metis Cortex
            </Link>
          </p>
        </div>
      </section>

      <Footer />
    </main>
  );
}
