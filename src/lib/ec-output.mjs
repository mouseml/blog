/**
 * Expressive Code plugin: program-output blocks.
 *
 * Source posts mark REPL/SQL/command output with `{.no-copy}` (MkDocs). The
 * migration script rewrites that to a bare `output` meta flag. This plugin then:
 *   - tags the block root with `is-output` for distinct "OUTPUT" styling, and
 *   - strips the copy-to-clipboard button (you don't copy program output).
 *
 * Plain hast manipulation — no helper imports, so config loading stays simple.
 */
export function pluginOutputBlocks() {
  return {
    name: 'output-blocks',
    hooks: {
      postprocessRenderedBlock(context) {
        const meta = context.codeBlock.meta ?? '';
        const isOutput =
          context.codeBlock.metaOptions.getBoolean('output') === true ||
          /(^|\s)output(\s|$)/.test(meta);
        if (!isOutput) return;

        const root = context.renderData.blockAst;
        root.properties = root.properties || {};
        const cls = root.properties.className;
        root.properties.className = Array.isArray(cls)
          ? [...cls, 'is-output']
          : cls
            ? [cls, 'is-output']
            : ['is-output'];

        const stripCopy = (node) => {
          if (!node || !Array.isArray(node.children)) return;
          node.children = node.children.filter((child) => {
            const c = child.properties && child.properties.className;
            const hasCopy = Array.isArray(c) ? c.includes('copy') : c === 'copy';
            return !hasCopy;
          });
          for (const child of node.children) stripCopy(child);
        };
        stripCopy(root);
      },
    },
  };
}
