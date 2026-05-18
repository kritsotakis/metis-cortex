import { Footer } from "@/components/Footer";
import { contactEmail } from "@/lib/site";

export default function Home() {
  const email = contactEmail();

  return (
    <>
      <main className="flex min-h-screen flex-col items-center justify-center bg-ink px-6 py-20 text-bone sm:px-10">
        <div className="flex max-w-2xl flex-col items-center text-center">
          <img
            src="/brand/metiscortex-mark.png"
            alt="Metis Cortex"
            className="h-24 w-24 sm:h-32 sm:w-32"
          />

          <img
            src="/brand/metiscortex-wordmark-tight.svg"
            alt="Metis Cortex"
            className="mt-8 h-12 w-auto sm:h-16"
          />

          <p className="mt-14 font-display text-[clamp(2rem,5vw,3.5rem)] leading-[1.1] tracking-tight text-bone">
            Something&rsquo;s{" "}
            <span className="mc-italic-display text-bone/85">coming.</span>
          </p>

          <p className="mt-10 max-w-md text-base leading-relaxed text-bone/65 sm:text-lg">
            We&rsquo;re building quietly. If you&rsquo;d like to know when, drop
            us a line.
          </p>

          <a
            href={`mailto:${email}`}
            className="mt-10 text-base text-bone/85 underline-offset-4 hover:text-bone hover:underline"
          >
            {email}
          </a>
        </div>
      </main>
      <Footer />
    </>
  );
}
