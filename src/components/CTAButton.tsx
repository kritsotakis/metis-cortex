import Link from "next/link";
import { bookingHref } from "@/lib/site";

type Surface = "ink" | "bone";

const styles: Record<Surface, string> = {
  // Default — for use on dark (ink) sections. Cream pill with ink text,
  // bronze chevron only. Per design system: bronze appears on the arrow
  // glyph, never as the fill.
  ink:
    "bg-bone text-ink hover:bg-bone-soft focus-visible:ring-bone-soft shadow-[0_1px_0_rgba(0,0,0,0.08)] focus-visible:ring-offset-ink",
  // For use on light (bone) sections. Ink pill with cream text.
  bone:
    "bg-ink text-bone hover:bg-ink-soft focus-visible:ring-ink-soft shadow-[0_1px_0_rgba(15,32,63,0.08)] focus-visible:ring-offset-bone",
};

export function CTAButton({
  children,
  surface = "ink",
  href,
}: {
  children: React.ReactNode;
  surface?: Surface;
  href?: string;
}) {
  const target = href ?? bookingHref();
  const isExternal = target.startsWith("http") || target.startsWith("mailto:");
  const className = `inline-flex items-center justify-center gap-2 rounded-full px-7 py-4 text-base font-medium tracking-tight transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 ${styles[surface]}`;

  const content = (
    <>
      {children}
      <span aria-hidden="true" className="text-bronze font-semibold">
        ›
      </span>
    </>
  );

  if (isExternal) {
    return (
      <a
        href={target}
        className={className}
        target={target.startsWith("http") ? "_blank" : undefined}
        rel={target.startsWith("http") ? "noopener noreferrer" : undefined}
      >
        {content}
      </a>
    );
  }
  return (
    <Link href={target} className={className}>
      {content}
    </Link>
  );
}
