// @ts-check
import { defineConfig, passthroughImageService } from 'astro/config';
import expressiveCode from 'astro-expressive-code';
import { pluginOutputBlocks } from './src/lib/ec-output.mjs';

// GitHub project page: https://mouseml.github.io/blog
// `base` must lead every internal link/asset path.
export default defineConfig({
  site: 'https://mouseml.github.io',
  base: '/blog',
  // Pre-rendered PNGs (ex-Manim) ship as-is; no sharp under Bun.
  image: { service: passthroughImageService() },
  integrations: [
    // Code blocks: titles, line highlighting, copy button. Dark-only, brutalist —
    // square corners, hairline borders, no shadow, mono UI. Refined in the design phase.
    expressiveCode({
      plugins: [pluginOutputBlocks()],
      themes: ['github-dark'],
      styleOverrides: {
        borderRadius: '0',
        borderColor: 'rgba(255,255,255,0.18)',
        codeBackground: '#060606',
        codeFontFamily: "'JetBrains Mono', ui-monospace, monospace",
        uiFontFamily: "'JetBrains Mono', ui-monospace, monospace",
        frames: {
          frameBoxShadowCssValue: 'none',
          editorBackground: '#060606',
          editorActiveTabBackground: 'transparent',
          editorTabBarBackground: 'rgba(255,255,255,0.03)',
          terminalBackground: '#060606',
          terminalTitlebarBackground: 'rgba(255,255,255,0.03)',
        },
      },
    }),
  ],
});
