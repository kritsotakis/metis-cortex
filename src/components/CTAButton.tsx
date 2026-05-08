import Link from "next/link";
import { bookingHref } from "@/lib/site";

type Variant = "primary" | "ghost";

const styles: Record<Variant, string> = {
  primary:
    "bg-gold text-ink hover:bg-gold-soft focus-visible:ring-gold-soft shadow-[0_1px_0_rgba(0,0,0,0.06)]",
  ghost:
    "bg-transparent text-bone border border-bone/40 hover:bg-bone/10 focus-visible:ring-bone/60",
};

export function CTAButton({
  children,
  variant = "primary",
  href,
}: {
  children: React.ReactNode;
  variant?: Variant;
  href?: string;
}) {
  const target = href ?? bookingHref();
  const isExternal = target.startsWith("http") || target.startsWith("mailto:");
  const className = `inline-flex items-center justify-center gap-2 rounded-full px-7 py-4 text-base font-semibold tracking-tight transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-ink ${styles[variant]}`;

  if (isExternal) {
    return (
      <a
        href={target}
        className={className}
        target={target.startsWith("http") ? "_blank" : undefined}
        rel={target.startsWith("http") ? "noopener noreferrer" : undefined}
      >
        {children}
        <span aria-hidden="true">→</span>
      </a>
    );
  }
  return (
    <Link href={target} className={className}>
      {children}
      <span aria-hidden="true">→</span>
    </Link>
  );
}
