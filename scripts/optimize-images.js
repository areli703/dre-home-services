#!/usr/bin/env node
/**
 * Batch image optimiser for dre-home-services. v2 with tightened variants.
 * Run from repo root:  node scripts/optimize-images.js
 */
const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

const SRC_DIR = "images";
const OUT_DIR = "images/optimized";
const REPORTS_DIR = "reports";

const PRESETS = {
  "favicon":       { widths: [48, 180],            fit: "cover", quality: { avif: 60, webp: 75 } },
  "logo":          { widths: [180, 360],           fit: "inside", quality: { avif: 70, webp: 80 } },
  "logo-new":      { widths: [180, 360],           fit: "inside", quality: { avif: 70, webp: 80 } },
  "logo-dark":     { widths: [180, 360],           fit: "inside", quality: { avif: 70, webp: 80 } },
  "logo-alt":      { widths: [180, 360],           fit: "inside", quality: { avif: 70, webp: 80 } },
  "og-image":      { widths: [1200],               fit: "cover",  quality: { avif: 60, webp: 75 } },
  "deck-gazebo":   { widths: [640, 1280],          fit: "cover",  quality: { avif: 55, webp: 70 } }, // hero
};
// Everything else is a below-fold gallery photo → two variants only.
const DEFAULT = { widths: [480, 960], fit: "inside", quality: { avif: 55, webp: 72 } };

function fmtBytes(n) {
  if (n < 1024) return `${n} B`;
  if (n < 1024 * 1024) return `${(n / 1024).toFixed(1)} KB`;
  return `${(n / (1024 * 1024)).toFixed(2)} MB`;
}

async function processOne(file) {
  const srcPath = path.join(SRC_DIR, file);
  const ext = path.extname(file).toLowerCase();
  const base = path.basename(file, ext);
  if (![".png", ".jpg", ".jpeg"].includes(ext)) return null;
  const cfg = PRESETS[base] || DEFAULT;
  const srcBytes = fs.statSync(srcPath).size;
  const img = sharp(srcPath, { failOnError: false });
  const meta = await img.metadata();
  if (!meta.width) return null;
  const out = { base, srcBytes, srcWidth: meta.width, srcHeight: meta.height, files: [] };

  for (const width of cfg.widths) {
    const targetW = Math.min(width, meta.width);
    const scale = targetW / meta.width;
    const targetH = Math.round(meta.height * scale);
    for (const format of ["avif", "webp"]) {
      const name = `${base}-${targetW}w.${format}`;
      const dest = path.join(OUT_DIR, name);
      await img
        .clone()
        .resize({ width: targetW, height: targetH, fit: cfg.fit, withoutEnlargement: true, kernel: sharp.kernel.lanczos3 })
        [format]({ quality: cfg.quality[format], effort: format === "avif" ? 4 : 4 })
        .toFile(dest);
      out.files.push({ format, width: targetW, height: targetH, bytes: fs.statSync(dest).size, name });
    }
  }
  return out;
}

(async () => {
  fs.mkdirSync(OUT_DIR, { recursive: true });
  fs.mkdirSync(REPORTS_DIR, { recursive: true });

  // Clean out prior bloated variants
  for (const f of fs.readdirSync(OUT_DIR)) fs.unlinkSync(path.join(OUT_DIR, f));

  const files = fs.readdirSync(SRC_DIR).filter((f) =>
    [".png", ".jpg", ".jpeg"].includes(path.extname(f).toLowerCase())
  );

  console.log(`\nProcessing ${files.length} source images from ${SRC_DIR}/ -> ${OUT_DIR}/\n`);

  const results = [];
  for (const file of files) {
    process.stdout.write(`  ${file} ... `);
    try {
      const r = await processOne(file);
      if (!r) { console.log("skipped"); continue; }
      results.push(r);
      const totalOut = r.files.reduce((s, f) => s + f.bytes, 0);
      const saved = r.srcBytes - totalOut;
      const pct = ((saved / r.srcBytes) * 100).toFixed(1);
      console.log(`ok  ${fmtBytes(r.srcBytes)} → ${fmtBytes(totalOut)} (-${pct}%)  [${r.files.length} variants]`);
    } catch (e) {
      console.log(`FAIL ${e.message}`);
    }
  }

  // Total payload comparison: what a mobile user would ACTUALLY download
  // = 1 hero at 1280w AVIF + 6 below-fold photos at 480w AVIF, plus logo+favicon
  let heroPayload = 0, galleryPayload = 0;
  for (const r of results) {
    if (r.base === "deck-gazebo") {
      const heroAvif = r.files.find((f) => f.format === "avif" && f.width === 1280);
      heroPayload = heroAvif ? heroAvif.bytes : 0;
    }
  }
  const galleryBases = ["deck-stairs","deck-construction-2","deck-construction-3","deck-built-in-bench","deck-new-backyard","concrete-floor-sealing","concrete-epoxy-floor"];
  for (const r of results) {
    if (galleryBases.includes(r.base)) {
      const avif = r.files.find((f) => f.format === "avif" && f.width === 480);
      if (avif) galleryPayload += avif.bytes;
    }
  }

  console.log(`\n=== ESTIMATED MOBILE PAYLOAD (hero 1280w AVIF + 7 gallery 480w AVIF) ===`);
  console.log(`Hero   : ${fmtBytes(heroPayload)}`);
  console.log(`Gallery: ${fmtBytes(galleryPayload)}`);
  console.log(`Total  : ${fmtBytes(heroPayload + galleryPayload)} (was ~14MB original)`);
  console.log(`Savings: ${((1 - (heroPayload + galleryPayload) / (14 * 1024 * 1024)) * 100).toFixed(1)}%`);
})();
