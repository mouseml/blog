#!/usr/bin/env bun
/**
 * One-off migration: translate MkDocs code-fence syntax to Expressive Code.
 *
 *   ```sqlite          ->  ```sql          (Shiki has no `sqlite` grammar)
 *   hl_lines="a-b c"   ->  {a-b,c}         (EC line-highlight meta)
 *   {.no-copy}         ->  output          (program-output blocks; see ec-output.mjs)
 *
 * `title="..."` is already EC-compatible and left untouched. Only OPENING fence
 * lines are transformed (fence state is tracked). Prints the result to stdout.
 *
 * Usage: bun tools/migrate-fences.ts <file.md>
 */
import { readFileSync } from 'node:fs';

const file = process.argv[2];
if (!file) {
  console.error('usage: bun tools/migrate-fences.ts <file.md>');
  process.exit(1);
}

let inFence = false;
const out = readFileSync(file, 'utf8')
  .split('\n')
  .map((line: string) => {
    if (!line.startsWith('```')) return line;
    if (inFence) {
      inFence = false; // closing fence — leave as-is
      return line;
    }
    inFence = true; // opening fence — translate
    return line
      .replace(/^```sqlite\b/, '```sql')
      .replace(/\bhl_lines="([^"]*)"/g, (_m: string, r: string) => `{${r.trim().replace(/\s+/g, ',')}}`)
      .replace(/\{\.no-copy\}/g, 'output');
  })
  .join('\n');

process.stdout.write(out);
