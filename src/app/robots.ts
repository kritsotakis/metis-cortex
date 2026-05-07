import type { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [{ userAgent: "*", allow: "/" }],
    sitemap: "https://metiscortex.au/sitemap.xml",
    host: "https://metiscortex.au",
  };
}
