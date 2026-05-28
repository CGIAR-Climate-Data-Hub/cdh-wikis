// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// CGIAR Climate Data Hub — wikis site.
//
// Deployed to GitHub Pages at:
//   https://cgiar-climate-data-hub.github.io/wikis/
//
// To add a new wiki:
//   1. Drop a markdown / mdx file under src/content/docs/<area>/<slug>.md
//   2. Update the `sidebar` config below to surface it
//   3. Commit & push to main; the GitHub Action deploys automatically
//
// See ./playbook/ADDING_A_NEW_WIKI.md for the full guide.

export default defineConfig({
  // GitHub Pages serves the site under /wikis/ — Starlight needs both
  // site (full URL) and base (repo path) so internal links resolve.
  site: 'https://cgiar-climate-data-hub.github.io',
  base: '/wikis',

  integrations: [
    starlight({
      title: 'CGIAR Climate Data Hub — Wikis',
      description:
        'Reference and knowledge wikis from the CGIAR Climate Data Hub community — staging and publishing area for partner-facing climate-science reference material.',

      // Edit-on-GitHub link in each page footer.
      editLink: {
        baseUrl:
          'https://github.com/CGIAR-Climate-Data-Hub/wikis/edit/main/',
      },

      // Last-updated timestamps in the footer use the git history.
      lastUpdated: true,

      social: {
        github: 'https://github.com/CGIAR-Climate-Data-Hub/wikis',
      },

      // Sidebar — grouped by "area" (the source institution / programme
      // contributing the wiki). When a new wiki lands, either drop it in
      // an existing group or add a new group here.
      sidebar: [
        {
          label: 'About',
          items: [
            { label: 'Welcome', slug: '' },
            { label: 'Contributing a wiki', slug: 'contributing' },
          ],
        },
        {
          label: 'Climate model selection',
          items: [
            { label: 'Overview', slug: 'aaa-atlas' },
            {
              label: 'African CMIP6 Ensembling',
              slug: 'aaa-atlas/african-cmip6-ensembling',
            },
          ],
        },
      ],

      // CSS overrides for CGIAR branding go here once design lands.
      // customCss: ['./src/styles/cgiar.css'],

      // Don't fight Starlight's defaults on the components — Asides
      // (`:::note` `:::tip` `:::caution` `:::danger`) cover the callout
      // patterns we use today; richer custom components can be added per
      // wiki via MDX if needed.
    }),
  ],
});
