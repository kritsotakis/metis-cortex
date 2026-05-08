import Link from "next/link";
import { contactEmail } from "@/lib/site";

export default function NotFound() {
  const email = contactEmail();
  return (
    <main className="relative min-h-screen overflow-hidden bg-ink text-bone">
      <div className="relative mx-auto flex min-h-screen max-w-3xl flex-col justify-center px-6 py-20 sm:px-10">
        <p className="mb-6 inline-flex items-center gap-3 text-xs uppercase tracking-[0.22em] text-bronze">
          <span className="h-px w-8 bg-bronze" />
          404
        </p>
        <h1 className="font-display text-[clamp(3rem,7vw,5rem)] font-semibold leading-[0.95] tracking-tight text-bone">
          That page didn&rsquo;t pick up.
        </h1>
        <p className="mt-8 max-w-xl text-lg leading-relaxed text-bone/80">
          We couldn&rsquo;t find the page you were after. The rest of the site
          is still very much answering the phone.
        </p>
        <div className="mt-10 flex flex-wrap items-center gap-6">
          <Link
            href="/"
            className="inline-flex items-center justify-center gap-2 rounded-full bg-bone px-7 py-4 text-base font-medium tracking-tight text-ink transition-colors hover:bg-bone-soft focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-ink focus-visible:ring-bone-soft"
          >
            Back to home
            <span aria-hidden="true" className="text-bronze font-semibold">›</span>
          </Link>
          <a
            href={`mailto:${email}`}
            className="text-sm text-bone/70 underline-offset-4 hover:text-bone hover:underline"
          >
            Or email us: {email}
          </a>
        </div>
      </div>
    </main>
  );
}
