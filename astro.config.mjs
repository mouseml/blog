// @ts-check
import { defineConfig, passthroughImageService } from 'astro/config';
import expressiveCode, { pluginFramesTexts } from 'astro-expressive-code';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { pluginOutputBlocks } from './src/lib/ec-output.mjs';
import { remarkHeadingIds } from './src/lib/remark-heading-ids.mjs';
import { rehypeFigures } from './src/lib/rehype-figures.mjs';
import { rehypeLinks } from './src/lib/rehype-links.mjs';

// Localize the code-block copy button (Expressive Code defaults to en-US).
pluginFramesTexts.overrideTexts('en', {
  copyButtonTooltip: 'Скопировать',
  copyButtonCopied: 'Скопировано',
});

// GitHub project page: https://mouseml.github.io/blog
// `base` must lead every internal link/asset path.
export default defineConfig({
  site: 'https://mouseml.github.io',
  base: '/blog',
  // Pre-rendered PNGs (ex-Manim) ship as-is; no sharp under Bun.
  image: { service: passthroughImageService() },
  // Math: $...$ / $$...$$ rendered to KaTeX at build time (no runtime MathJax).
  // KaTeX CSS is loaded by the layout; KaTeX inherits currentColor (white on black).
  markdown: {
    remarkPlugins: [remarkHeadingIds, remarkMath],
    rehypePlugins: [rehypeKatex, rehypeFigures, rehypeLinks],
  },
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
