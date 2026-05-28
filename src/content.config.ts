// Astro Content Collections — Starlight schema.
//
// Starlight uses a single content collection called `docs` under
// src/content/docs/. The schema below lets us add wiki-specific
// frontmatter fields beyond Starlight's defaults (authors, version,
// CGIAR-area tags) without losing Starlight's built-in fields.

import { defineCollection } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';
import { z } from 'astro:content';

export const collections = {
  docs: defineCollection({
    loader: docsLoader(),
    schema: docsSchema({
      extend: z.object({
        // Optional extended frontmatter fields. Wiki authors can leave
        // these blank; Starlight's defaults still apply.
        version: z.string().optional(),
        authors: z
          .array(
            z.object({
              name: z.string(),
              affiliation: z.string().optional(),
            })
          )
          .optional(),
        area: z.string().optional(), // e.g. "AAA Adaptation Atlas"
        // Where the source of truth for this content lives, if it's
        // staged from another repo. e.g. "atlas_notebooks@<sha>".
        sourceOfTruth: z.string().optional(),
        // Estimated reading time in minutes — optional, used by the
        // landing-page card.
        estimatedReadingMinutes: z.number().int().positive().optional(),
      }),
    }),
  }),
};
