// @ts-check
import { defineConfig, passthroughImageService } from 'astro/config';

// GitHub project page: https://mouseml.github.io/blog
// `base` must lead every internal link/asset path.
export default defineConfig({
  site: 'https://mouseml.github.io',
  base: '/blog',
  // Pre-rendered PNGs (ex-Manim) ship as-is; no sharp under Bun.
  image: { service: passthroughImageService() },
});
