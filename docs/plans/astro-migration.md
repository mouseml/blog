# Migration plan: MkDocs Material → raw Astro

- **Status:** in progress — Phases 1–3 done (steps 1–13 ✓): pipeline, brutalist design, and full content (all 5 posts ported, images + static downloads). `astro check` clean (0/0); all routes serve under /blog. Next: Phase 4 (Pagefind search in the ⌘K palette), then Phase 5 (deploy + retire MkDocs/Python). Branch `astro-migration`.
- **Date:** 2026-06-16 (rev. 3 — dropped URL preservation; retired Python/Manim incl. deleting `scripts/`; in-place on a branch, not a new repo; folded in design prototype)
- **Owner:** мыш (single dev)
- **Verdict:** proceed. Migrate now while the corpus is ~7 posts.

---

## 1. Decision (locked)

Replace MkDocs Material with **hand-built Astro**, on a **single Bun + TypeScript toolchain** (Bun is already installed and is what the design prototype's dc-runtime builds with):

- **Astro** (general content framework, not a docs theme) — the site is a video-companion content blog (a reverse-chron "Лента" feed of YouTube-thumbnail posts + full-text search), not an API-docs site.
- **Build the look from scratch** (no Starlight). The design prototype (`../blog-prototype/`) is the reference: **dark-only brutalist** — pure black, white text, hairline `rgba(255,255,255,.16)` borders, no radius, no shadows.
  - Fonts: **Golos Text** (display/headings, 800–900), **Onest** (body), **JetBrains Mono** (code + all meta/labels). Self-host via Fontsource (Cyrillic subsets).
  - Components: flat card feed (16:9 thumbnails, grayscale→color on hover), article with sticky TOC + scroll-progress bar + scrollspy, YouTube CTA card, prev/next nav, ⌘K command-palette search, license page, footer.
- **MDX + Astro islands** for *selective* interactivity — static HTML by default, hydrate only the rare component worth it. The prototype's hand-rolled "block model" is **replaced by Markdown/MDX rendering** (`<Content/>`).
- **Code blocks:** [Expressive Code](https://expressive-code.com) — titles, line highlighting, copy button. Terminal/`OUTPUT` blocks get a distinct frame (matches the prototype's joined-output treatment).
- **Math:** `remark-math` + `rehype-katex` — build-time, removes runtime MathJax.
- **Search:** [Pagefind](https://pagefind.app) — build-time static full-text index, client-side, Russian stemming. Drives the ⌘K palette UI (we use Pagefind's API, not its default UI). Added **after** the redesign.
- **URLs:** clean and free (see §4.1 — preservation is no longer required). Default scheme: `/posts/<slug>/` under base `/blog`.

### Retired in this migration

- **Python entirely — no double env.** Drop `pyproject.toml`, `uv.lock`, `.python-version`, `.venv/`, `.ruff_cache/` and the `manim`/`pandas`/`mkdocs` deps. The repo becomes Node/TypeScript only.
- **Manim entirely.** The already-rendered PNGs are ported as static assets; the **Manim source (`scripts/`) is deleted — git history is the archive**, no dead code in the tree. Future visuals will be Remotion/MDX or reworked.
- **Execution:** in-place on branch `astro-migration` cut from `main` — *not* a new repo/folder. Preserves the GitHub identity (`mouseml/blog`), Pages deployment, and history.

---

## 2. Content feature inventory (what must port)

Measured across all 6 posts (4,291 lines):

| Feature | Usage | Astro mapping |
|---|---|---|
| Code blocks | 178 — `.no-copy` ×95, `hl_lines` ×45, `title=` ×30; langs python/text/sqlite/shell/json/sql | Expressive Code (+ distinct OUTPUT frame for `.no-copy`) |
| LaTeX math | 4/6 posts, up to 29 spans (nn.md) | remark-math + rehype-katex (KaTeX) |
| Rendered images (ex-Manim PNGs) | every post + per-post thumbnail | static assets ported into Astro |
| Content tabs `=== "…"` | 2 total (torch.md) | small `<Tabs>` component (hand-convert) |
| Heading IDs `{#id}` | a handful (sql_ds.md etc.) | rehype-slug + explicit-id plugin; feeds TOC |
| Frontmatter | `date`, `slug`, `categories`, `links` (YouTube) | content-collection Zod schema |
| `<!-- more -->` excerpt | every post | `excerpt`/`description` field |
| Admonitions `!!!` / inline video / Mermaid | **0** — not used | n/a |

The prototype's `P/H2/IMG/F/C/O` block objects are a prototyping-tool workaround for lacking a Markdown renderer — **not ported**. Markdown/MDX *is* the block model.

---

## 3. Syntax translation map (the mechanical core)

| MkDocs source | Astro target |
|---|---|
| ` ```python title="load.py" ` | ` ```python title="load.py" ` (same) |
| ` ```python hl_lines="15-20" ` | ` ```python {15-20} ` |
| ` ```python hl_lines="2-3 13-17" ` | ` ```python {2-3,13-17} ` |
| ` ```text {.no-copy} ` | EC OUTPUT/terminal frame, copy disabled |
| ` ```sqlite ` | ` ```sql ` (Shiki has no `sqlite` grammar) |
| `$...$` / `$$...$$` | unchanged (remark-math) |
| `## Heading {#task}` | `## Heading {#task}` (via plugin) or hand-keep |
| `<!-- more -->` | excerpt boundary |
| frontmatter `links:` | schema `youtube:` field |

One-pass script handles the code fences; `.no-copy` and the 2 tab blocks are the only hand-touches.

---

## 4. Top risks

1. **Math is unproven in the design.** The prototype *stubs* formulas as serif-italic Unicode text; it does not show real KaTeX in the dark theme. With up to 29 spans (nn.md), validate KaTeX rendering + display-math alignment on black early (KaTeX inherits `currentColor`, so white-on-black should work — confirm). **Spike this in step 5.**
2. **Search quality.** The prototype's search is `String.includes()` over a hand-written keyword bag — not the real use case. "I remember the author mentioning X, which video?" needs Pagefind indexing full post bodies, with `<html lang="ru">` for Russian stemming. Wiring Pagefind into the ⌘K palette is the one real integration (step 14).
3. **Base path `/blog`.** GitHub project page (`mouseml.github.io/blog`). `astro.config` needs `site: 'https://mouseml.github.io'` + `base: '/blog'`; every internal link/asset must respect `base`. Verify on the *deployed* site.
4. **Real content density vs thin prototype.** Prototype posts are paraphrased (~5–25 blocks); real posts are 425–1216 lines with wide unicode box-art output tables and heavy code. Check the widest `┌──┬──┐` OUTPUT block scrolls cleanly inside the column.
5. **Faithful inline-style → component CSS.** The prototype is all inline `style` + a `dc`-specific `style-hover` attr. Re-express as Astro components with real CSS `:hover`, and convert `<div onClick>` cards to real `<a href>` (needed for URLs/SEO/middle-click anyway).
6. **Clean single-toolchain cutover.** When retiring Python, ensure nothing in CI/build references it and the archived Manim source isn't stranded (it stays as files, just out of the build).

Premature-deletion guard: keep MkDocs working until the deployed Astro site passes the parity gate (step 16); retire the old stack only in step 17.

### 4.1 URL preservation — dropped

Confirmed: shared links only ever pointed at the site root, not deep post URLs, so there are **no inbound links to preserve**. We are free to design clean URLs from scratch (`/posts/<slug>/`). This removes the former #1 risk, the date-based dynamic route, and the category/archive URL-matching work.

---

## 5. Plan (each step = one commit; all unfinished)

### Phase 0 — Scaffold (Node/TypeScript only)

- [x] **1. Scaffold Astro at repo root. ✓**
  - *Changes:* `package.json`, `astro.config.mjs` (`site` + `base: '/blog'` + passthrough image service), `tsconfig.json`, `src/pages/index.astro` placeholder; gitignore `node_modules/`, `dist/`, `.astro/`. Bun resolved Astro 6.4.7. Coexists with MkDocs.
  - *Verify:* ✓ `bun run build` succeeds; preview serves the placeholder at `/blog` (HTTP 200), `/` 404s. No Python or Node required.
  - *Commit:* `Scaffold Astro project` (ec41a46)

- [x] **2. Define the posts content collection. ✓** (4535a42)
  - *Changes:* `src/content/config.ts` — Zod schema: `date` (Date), `slug` (string), `categories` (string[]), `youtube` (string), `excerpt`/`description`, `thumbnail` (`image()`).
  - *Verify:* `astro check` flags a deliberately malformed frontmatter sample.
  - *Commit:* `Add posts content collection schema`

### Phase 1 — Markdown/MDX pipeline parity

- [x] **3. Wire Expressive Code. ✓** (0e2c9e3)
  - *Changes:* `astro-expressive-code`; dark brutalist theme; titles, line markers, copy button; a distinct OUTPUT/terminal frame for `.no-copy` output blocks.
  - *Verify:* scratch post with `title=`, `{15-20}`, copy button, and an OUTPUT block render correctly.
  - *Commit:* `Wire Expressive Code for code blocks`

- [x] **4. Add the code-fence translation pass. ✓** (ded98ab)
  - *Changes:* one-off Node script converting `hl_lines="…"`→`{…}`, `sqlite`→`sql`, `{.no-copy}`→OUTPUT frame.
  - *Verify:* diff torch.md + sql_ds.md output; copy absent on OUTPUT blocks.
  - *Commit:* `Add MkDocs→Astro code-fence translation script`

- [x] **5. Wire KaTeX; drop runtime MathJax. ✓ (math spike — passed)** (80fcc27)
  - *Changes:* `remark-math` + `rehype-katex` + KaTeX CSS in base layout.
  - *Breaks:* math rendering if delimiters/macros differ.
  - *Verify:* nn.md (29 spans) + torch.md render correctly and look right on black. **This is the risk-1 spike — do it before committing to the design details.**
  - *Commit:* `Render math with KaTeX at build time`

- [x] **6. Heading slugs + explicit IDs + TOC source. ✓** (7995c90)
  - *Changes:* `rehype-slug` (+ honor `{#id}`); expose `getHeadings()` for the TOC.
  - *Verify:* `#task`/`#load`/`#join`/`#cloud` resolve; headings list is correct.
  - *Commit:* `Add heading slugs and TOC extraction`

### Phase 2 — Brutalist design (prototype is the reference)

- [x] **7. Base layout + global styles + `<head>`. ✓** (9097975)
  - *Changes:* `<html lang="ru">`; dark brutalist global CSS; self-hosted fonts (Golos Text / Onest / JetBrains Mono via Fontsource); GA `G-T1L5SBV3KR`; OG/meta; favicon + `icon.svg` brand mark.
  - *Verify:* Lighthouse; GA debug hit fires; Cyrillic renders in all three fonts.
  - *Commit:* `Add base layout and brutalist global styles`

- [x] **8. Feed (channel-grid landing). ✓** (63d1594)
  - *Changes:* flat reverse-chron card grid (`auto-fill,minmax(340px,1fr)`), 16:9 thumbnails, **CSS** grayscale→color hover, mono meta, "ТЕКСТ ВИДЕО" tag, post count + last-updated. Cards are real `<a href>`.
  - *Verify:* reads like a YouTube channel page; middle-click opens in new tab.
  - *Commit:* `Add channel-grid feed`

- [x] **9. Article layout. ✓** (c6f8808)
  - *Changes:* title header + meta; YouTube CTA card; two-column (article + sticky 232px TOC); scroll-progress bar + scrollspy (vanilla `<script>`/IntersectionObserver); prose/code/math/figure styling; prev/next nav; mobile collapsible TOC.
  - *Verify:* one ported post reads end-to-end. **← REVIEW CHECKPOINT: confirm the aesthetic before bulk content port** (prototype already sets the direction).
  - *Commit:* `Add article layout`

- [x] **10. License page + footer. ✓** (aa3b97e; footer shipped with step 7)
  - *Changes:* CC BY-NC-ND license page (can/cannot/condition table from prototype); footer with YouTube / Telegram / License links.
  - *Verify:* links resolve; license text intact.
  - *Commit:* `Add license page and footer`

### Phase 3 — Content port

- [x] **11. Slug-based post route. ✓** (landed in step 9, c6f8808 — `/posts/<id>/`)
  - *Changes:* `src/pages/posts/[...slug].astro` → clean `/posts/<slug>/` URLs.
  - *Verify:* every post resolves at its slug URL.
  - *Commit:* `Add slug-based post route`

- [x] **12. Port all posts (full bodies). ✓** (894200f — via `tools/port-post.ts`, which supersedes the step-4 `migrate-fences.ts`)
  - *Changes:* copy `docs/posts/*.md` → `src/content/posts/*.{md,mdx}`; run step-4 script; convert the 2 torch.md tab blocks to `<Tabs>`; map `<!-- more -->`→`excerpt`. Use the **real full** posts, not the prototype's abbreviated blocks. (Also port the `history.md` draft when ready; fix its broken image path.)
  - *Verify:* each post diffed visually against live MkDocs.
  - *Commit:* `Port all posts to Astro content collection`

- [x] **13. Port images + download assets. ✓** (images: 63d1594; static downloads: eab3953)
  - *Changes:* move rendered PNGs/thumbnails into Astro (`src/` for optimization where it helps); put `.pt`/`.csv`/`model.py` download assets in `public/`; update in-post links to their new locations.
  - *Verify:* no broken images; every download link resolves.
  - *Commit:* `Port post images and download assets`

### Phase 4 — Search (⌘K palette + Pagefind)

- [ ] **14. Add Pagefind behind the command palette.**
  - *Changes:* run `pagefind` as a postbuild step over `dist/`; build the ⌘K palette UI from the prototype (⌘K and `/` open, ↑↓↵ nav, Esc close) driving Pagefind's JS API; confirm `lang="ru"`.
  - *Verify:* "I remember the author mentioning X" finds content across full post bodies; Russian queries in other grammatical cases still match.
  - *Commit:* `Add Pagefind full-text search in command palette`

### Phase 5 — Deploy & retire the old stack

- [ ] **15. GitHub Actions → Pages.**
  - *Changes:* workflow building Astro + Pagefind, deploying to Pages; `@astrojs/sitemap`. Switch Pages source from the MkDocs gh-pages flow to the Action.
  - *Verify:* deployed `/blog` works — base path, assets, search.
  - *Commit:* `Deploy Astro via GitHub Actions`

- [ ] **16. Parity gate (GO/NO-GO).**
  - *Verify (no code):* all posts render; images + downloads resolve; math, code, and search work on the live deployment. Do not proceed until green.

- [ ] **17. Retire MkDocs + the Python toolchain (single-toolchain cutover).**
  - *Changes:*
    - Delete MkDocs: `mkdocs.yaml`, `docs/javascripts/mathjax.js`, the old `docs/` MkDocs tree (content now in `src/content`).
    - Delete Python project: `pyproject.toml`, `uv.lock`, `.python-version`, `.venv/`, `.ruff_cache/`; remove `manim`/`pandas`/`mkdocs` deps.
    - Delete `scripts/` (Manim source) — retained in git history; no dead code in the tree. (Independent of MkDocs, so it can land earlier as its own commit.)
    - Rewrite `README.md`: Bun dev (`bun install` / `bun run dev`); remove `uv sync` / `mkdocs serve` / Manim reproducibility steps; keep the CC license section.
    - Slim `.gitignore` to Node-oriented.
  - *Verify:* a fresh clone builds and serves with **Node only** — no Python anywhere in the path.
  - *Commit:* `Retire MkDocs and Python toolchain`

---

## 6. Out of scope / follow-ups (optional)

- **RSS feed** (`@astrojs/rss`) for the subscriber audience.
- **First interactive island / Remotion or MDX remaster** of one visual — the seed of the "interactive learning platform" direction. Keep rare to protect the brutalist feel.
- **Light theme** — dropped for now (dark-only per prototype); revisit only if wanted.

## 7. Deferred decisions (sensible defaults chosen; easy to change)

- **URL scheme:** `/posts/<slug>/` (default). Free choice now that preservation is dropped.
- **Theme:** dark-only (per prototype).
- **Category pages:** none — flat feed + search (per prototype). Categories stay as display metadata; add filtering later if wanted.
- **Fonts:** self-host via Fontsource (recommended) vs Google CDN.
- **Runtime + package manager:** Bun (resolved — installed, and already used for the prototype's dc-runtime). Astro 6, static output.
