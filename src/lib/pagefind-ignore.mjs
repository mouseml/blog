import { visit } from 'unist-util-visit';

/**
 * Keep code blocks and math out of the Pagefind search index, so results match
 * only prose (inline `code` stays — it's part of the sentence). `data-pagefind-
 * ignore` tells Pagefind to skip an element's subtree.
 *
 * Two halves, because code and math are emitted by different pipelines:
 *   - math (KaTeX, via rehype-katex) is tagged in the markdown rehype pass;
 *   - code (Expressive Code) is tagged inside EC's own render hook — the
 *     pipeline that owns the code block's final markup — rather than guessing at
 *     rehype-plugin ordering around EC.
 */

// rehype: tag KaTeX output — display (`.katex-display`) and inline (`.katex`).
export function rehypePagefindIgnore() {
  return (tree) => {
    visit(tree, 'element', (node) => {
      const cls = node.properties?.className;
      const classes = Array.isArray(cls) ? cls : cls ? [cls] : [];
      if (classes.includes('katex') || classes.includes('katex-display')) {
        node.properties.dataPagefindIgnore = true;
      }
    });
  };
}

// Expressive Code: tag each rendered code block at its root (covers the code,
// its frame, and the title/filename header).
export function pluginPagefindIgnore() {
  return {
    name: 'pagefind-ignore',
    hooks: {
      postprocessRenderedBlock(context) {
        const root = context.renderData.blockAst;
        root.properties = root.properties || {};
        root.properties.dataPagefindIgnore = true;
      },
    },
  };
}
