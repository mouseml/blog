import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Video-companion posts. One Markdown/MDX file per post; the filename is the id/slug
// and drives the URL (/posts/<id>/). Frontmatter is the source of truth for metadata
// shown in the feed, <head>, and OG — the post body no longer carries an <h1> title.
const posts = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    youtube: z.string().url(),
    excerpt: z.string().optional(),
    // Path under /public (passthrough images), e.g. images/posts/trees/thumbnail.jpg.
    thumbnail: z.string(),
    minutes: z.number(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { posts };
