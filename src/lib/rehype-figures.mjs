import { visit } from 'unist-util-visit';

/**
 * Wrap standalone block images in <figure> and turn their alt text into a
 * <figcaption>. Markdown renders `![caption](src)` as `<p><img></p>`; the post
 * design wants bordered figures with a caption line (every Manim image has a
 * descriptive alt that doubles as its caption).
 */
export function rehypeFigures() {
  return (tree) => {
    visit(tree, 'element', (node, index, parent) => {
      if (node.tagName !== 'p' || !parent || index === null) return;
      const meaningful = node.children.filter(
        (c) => !(c.type === 'text' && c.value.trim() === ''),
      );
      if (meaningful.length !== 1) return;
      const img = meaningful[0];
      if (img.type !== 'element' || img.tagName !== 'img') return;

      const alt = (img.properties && img.properties.alt) || '';
      const figure = {
        type: 'element',
        tagName: 'figure',
        properties: {},
        children: [img],
      };
      if (alt) {
        figure.children.push({
          type: 'element',
          tagName: 'figcaption',
          properties: {},
          children: [{ type: 'text', value: alt }],
        });
      }
      parent.children[index] = figure;
    });
  };
}
