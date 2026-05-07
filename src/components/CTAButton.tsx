import Link from "next/link";

type Variant = "primary" | "ghost";

const CALENDLY_URL = "https://calendly.com/peter-kritsotakis/metis-cortex-demo";

const styles: Record<Variant, string> = {
  primary:
    "bg-gold text-ink hover:bg-gold-soft focus-visible:ring-gold-soft shadow-[0_1px_0_rgba(0,0,0,0.06)]",
  ghost:
    "bg-transparent text-bone border border-bone/40 hover:bg-bone/10 focus-visible:ring-bone/60",
};

export function CTAButton({
  children,
  variant = "primary",
  href = CALENDLY_URL,
}: {
  children: React.ReactNode;
  variant?: Variant;
  href?: string;
}) {
  const isExternal = href.startsWith("http");
  const className = `inline-flex items-center justify-center gap-2 rounded-full px-7 py-4 text-base font-semibold tracking-tight transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-ink ${styles[variant]}`;

  if (isExternal) {
    return (
      <a
        href={href}
        className={className}
        target="_blank"
        rel="noopener noreferrer"
      >
        {children}
        <span aria-hidden="true">→</span>
      </a>
    );
  }
  return (
    <Link href={href} className={className}>
      {children}
      <span aria-hidden="true">→</span>
    </Link>
  );
}
