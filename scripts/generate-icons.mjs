#!/usr/bin/env node
/**
 * Generate the favicon ladder + Apple touch icon + PWA icons from src/app/icon.svg.
 * Output sizes match the Exit Code Manus deliverable pattern: 16/32/48/64/128/256/512/1024.
 *
 * Usage:
 *   npm install --save-dev sharp
 *   node scripts/generate-icons.mjs
 *
 * Outputs:
 *   public/icons/favicon-16.png       — small browser tabs (uses simplified SVG if present)
 *   public/icons/favicon-32.png       — standard favicon
 *   public/icons/favicon-48.png
 *   public/icons/favicon-64.png
 *   public/icons/favicon-128.png
 *   public/icons/favicon-256.png
 *   public/icons/favicon-512.png      — PWA icon
 *   public/icons/favicon-1024.png     — high-DPI source
 *   public/apple-icon.png             — 180x180 for iOS bookmarks (Next App Router auto-discovers)
 *
 * After Manus delivers a new mark SVG, drop it at src/app/icon.svg and rerun this script.
 * Optional: drop a smaller/cleaner variant at src/app/icon-16.svg and the 16px output will
 * use that instead of downscaling the main icon.
 */

import { readFileSync, mkdirSync, existsSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import sharp from "sharp";

const __dirname = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(__dirname, "..");

const mainSvgPath = resolve(repoRoot, "src/app/icon.svg");
const smallSvgPath = resolve(repoRoot, "src/app/icon-16.svg");
const outDir = resolve(repoRoot, "public/icons");
const appleOutPath = resolve(repoRoot, "public/apple-icon.png");

if (!existsSync(mainSvgPath)) {
  console.error(`✗ Missing source SVG at ${mainSvgPath}`);
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });

const mainSvg = readFileSync(mainSvgPath);
const smallSvg = existsSync(smallSvgPath) ? readFileSync(smallSvgPath) : null;

const ladder = [16, 32, 48, 64, 128, 256, 512, 1024];

console.log("Generating favicon ladder…");
for (const size of ladder) {
  const source = size === 16 && smallSvg ? smallSvg : mainSvg;
  const variant = size === 16 && smallSvg ? " (using simplified icon-16.svg)" : "";
  const outPath = resolve(outDir, `favicon-${size}.png`);
  await sharp(source, { density: Math.max(72, size * 4) })
    .resize(size, size, { fit: "contain", background: { r: 0, g: 0, b: 0, alpha: 0 } })
    .png({ compressionLevel: 9 })
    .toFile(outPath);
  console.log(`  ✓ ${size}×${size}${variant}`);
}

console.log("Generating Apple touch icon (180×180)…");
await sharp(mainSvg, { density: 720 })
  .resize(180, 180, { fit: "contain", background: { r: 0, g: 0, b: 0, alpha: 0 } })
  .png({ compressionLevel: 9 })
  .toFile(appleOutPath);
console.log(`  ✓ ${appleOutPath}`);

console.log("\nDone. Files written to public/icons/ and public/apple-icon.png.");
console.log("Next: in src/app/layout.tsx metadata block, reference these via:");
console.log('  icons: { icon: "/icons/favicon-32.png", apple: "/apple-icon.png" }');
console.log("Or rely on Next App Router auto-discovery if you keep app/icon.svg + app/apple-icon.png.");
