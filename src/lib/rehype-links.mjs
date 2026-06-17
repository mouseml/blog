import { visit } from 'unist-util-visit';

/**
 * Restore link behaviour the source posts expressed via Material attr-lists
 * (`{:target="_blank"}`, `{:download=...}`), which the porter strips:
 *   - external links (http/https) open in a new tab, safely;
 *   - links into /static/ (the downloadable .pt/.csv/.py assets) get `download`.
 */
export function rehypeLinks() {
  return (tree) => {
    visit(tree, 'element', (node) => {
      if (node.tagName !== 'a') return;
      const href = node.properties?.href;
      if (typeof href !== 'string') return;
      if (/^https?:\/\//.test(href)) {
        node.properties.target = '_blank';
        node.properties.rel = 'noopener noreferrer';
      } else if (href.includes('/static/')) {
        node.properties.download = true;
      }
    });
  };
}
