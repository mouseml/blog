#!/usr/bin/env bun
/**
 * Port a MkDocs post into the Astro content collection. Keeps the already-authored
 * src/content/posts/<slug>.md frontmatter and replaces the body with the
 * transformed docs/posts/<slug>.md body:
 *   - strip the H1 title, the ![Обложка] cover image, and the <!-- more --> marker
 *   - rewrite ../images/ and ../static/ to base-absolute /blog/... public paths
 *   - translate code fences: sqlite -> sql, hl_lines="a b" -> {a,b},
 *     ```{.text .no-copy} -> ```text output, ```{.lang} -> ```lang
 *
 * Single fence-aware pass: body transforms apply only outside code, and fence
 * rewrites only on fence-open lines. (Torch's indented `=== "tab"` block is the
 * one thing this can't do — handled by hand afterwards.)
 *
 * Usage: bun tools/port-post.ts <slug>
 */
import { readFileSync, writeFileSync } from 'node:fs';

const slug = process.argv[2];
if (!slug) {
  console.error('usage: bun tools/port-post.ts <slug>');
  process.exit(1);
}

const srcPath = `src/content/posts/${slug}.md`;
const docPath = `docs/posts/${slug}.md`;

const frontmatter = readFileSync(srcPath, 'utf8').match(/^---\n[\s\S]*?\n---/)?.[0] ?? '';
const docBody = readFileSync(docPath, 'utf8').replace(/^---\n[\s\S]*?\n---\n/, '');

function openFence(line: string): string {
  // brace attribute form: ```{.text .no-copy}  ->  ```text output
  line = line.replace(/```\{([^}]*)\}/, (_m, attrs: string) => {
    const cls = attrs
      .split(/\s+/)
      .filter(Boolean)
      .map((s) => s.replace(/^\./, ''));
    const lang = cls.find((c) => c !== 'no-copy') ?? 'text';
    return '```' + lang + (cls.includes('no-copy') ? ' output' : '');
  });
  return line
    .replace(/^```sqlite\b/, '```sql')
    .replace(/\bhl_lines="([^"]*)"/g, (_m: string, r: string) => `{${r.trim().replace(/\s+/g, ',')}}`);
}

let inFence = false;
let titleStripped = false;
const out: string[] = [];

for (const line of docBody.split('\n')) {
  if (line.startsWith('```')) {
    out.push(inFence ? line : openFence(line));
    inFence = !inFence;
    continue;
  }
  if (inFence) {
    out.push(line);
    continue;
  }
  if (!titleStripped && /^# /.test(line)) {
    titleStripped = true;
    continue;
  }
  if (/^!\[Обложка\]/.test(line)) continue;
  if (/^<!-- more -->/.test(line)) continue;
  out.push(
    line
      .replace(/\.\.\/images\//g, '/blog/images/')
      .replace(/\.\.\/static\//g, '/blog/static/')
      // strip Material/pymdownx inline syntax; behaviour is restored by rehype-links
      .replace(/\s?:octicons-link-external-16:/g, '')
      .replace(/:material-file:/g, '↓')
      .replace(/\{:[^}]*\}/g, ''),
  );
}

const body = out.join('\n').replace(/^\n+/, '');
writeFileSync(srcPath, `${frontmatter}\n\n${body}\n`);
console.log(`ported ${slug}`);
