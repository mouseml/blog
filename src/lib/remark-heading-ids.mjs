import { visit } from 'unist-util-visit';

/**
 * Honor explicit heading ids: `## Заголовок {#anchor}`.
 *
 * Astro auto-slugs headings, but it transliterates Cyrillic into clumsy anchors
 * (понять-задачу) and treats `{#id}` as literal text. Our posts author short ASCII
 * ids for clean, shareable anchors (/posts/<slug>/#task), so we parse `{#id}` here:
 * strip it from the heading text and set the id. Astro's slugger respects an
 * existing id, so both the rendered `<h2 id>` and getHeadings() pick it up.
 */
export function remarkHeadingIds() {
  return (tree) => {
    visit(tree, 'heading', (node) => {
      const last = node.children[node.children.length - 1];
      if (!last || last.type !== 'text') return;
      const match = last.value.match(/\s*\{#([\w-]+)\}\s*$/);
      if (!match) return;
      last.value = last.value.replace(/\s*\{#[\w-]+\}\s*$/, '');
      node.data ??= {};
      node.data.hProperties ??= {};
      node.data.hProperties.id = match[1];
      node.data.id = match[1];
    });
  };
}
