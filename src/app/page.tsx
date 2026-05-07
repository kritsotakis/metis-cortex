import { Hero } from "@/components/Hero";
import { CostOfMissedCalls } from "@/components/CostOfMissedCalls";
import { WhatsIncluded } from "@/components/WhatsIncluded";
import { DSKCaseStudy } from "@/components/DSKCaseStudy";
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
      <DSKCaseStudy />
      <HowItWorks />
      <Guarantee />
      <FAQ />
      <ClosingCTA />
      <Footer />
    </main>
  );
}
