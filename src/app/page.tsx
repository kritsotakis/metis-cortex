import { Hero } from "@/components/Hero";
import { CostOfMissedCalls } from "@/components/CostOfMissedCalls";
import { WhatsIncluded } from "@/components/WhatsIncluded";
// DSKCaseStudy held until DSK pilot Day 28 metrics land — placeholder em-dashes
// kill credibility. Hero already says "Built and proven on DSK" above the fold.
// Re-enable once DSKCaseStudy.tsx renders real numbers.
// import { DSKCaseStudy } from "@/components/DSKCaseStudy";
import { HowItWorks } from "@/components/HowItWorks";
import { Guarantee } from "@/components/Guarantee";
import { FAQ } from "@/components/FAQ";
import { ClosingCTA } from "@/components/ClosingCTA";
import { Footer } from "@/components/Footer";

export default function Home() {
  return (
    <main>
      <Hero />
      <CostOfMissedCalls />
      <WhatsIncluded />
      {/* <DSKCaseStudy /> — held for real DSK Day 28 numbers */}
      <HowItWorks />
      <Guarantee />
      <FAQ />
      <ClosingCTA />
      <Footer />
    </main>
  );
}
