# Figure commission — F-africa-warming-stripes-hero

**Status**: interim animated SVG live at `public/figures/F-africa-warming-stripes-hero.svg`. Polish to real-data version pending.

**Used on**: top of `src/content/docs/aaa-atlas/projections-primer.md`, before the `:::tip` callout. The hero image of the section.

**Final file path**: `public/figures/F-africa-warming-stripes-hero.svg` (overwrite interim).

## What the figure must show

An **animated warming-stripes chart** of African continental annual temperature anomaly from 1901 to 2025 (or the longest defensible record available). Each vertical stripe = one year; colour = anomaly relative to a stated baseline; stripes wipe in left to right over ~5–6 seconds and hold at full reveal for ~3 seconds before looping.

Conceptual basis: Ed Hawkins's `#ShowYourStripes` design ([showyourstripes.info](https://showyourstripes.info)), applied to African continental data.

## Why animated

A static stripes chart works as a still image. The animated reveal adds a "watch Africa warm over the twentieth century" beat that gives the page an emotional opening before the analytical content. The animation is the engagement; the data is the rigour.

## Data source — pick one for the production version

The interim SVG is **plotted from hand-tuned plausible values** — it must be replaced with a citable series before publication. Candidate sources, in order of recommendation:

| Source | Coverage | Why | Citation |
|---|---|---|---|
| **Berkeley Earth — Africa land annual temperature** | 1850–present | Longest record; CC-BY-4.0; methodology peer-reviewed; ready CSV exports. Best academic defensibility. | [berkeleyearth.org/data](https://berkeleyearth.org/data/) |
| **WMO *State of the Climate in Africa* annual series** | ~1900–present | UN-published; matches the 1991–2020 baseline used elsewhere in the wiki. | [WMO 2024](https://wmo.int/publication-series/state-of-climate-africa-2024) |
| **NOAA GHCNm V4 + NASA GISTEMP Africa zonal mean** | 1880–present | Familiar to reviewers; CC0. Continental average derivable from public gridded product. | [NASA GISS GISTEMP](https://data.giss.nasa.gov/gistemp/) |
| **CHIRTS-ERA5 (UCSB)** | 1983–present | African-tuned; already named in `cgiar-recommendations.md` as the preferred observational temperature dataset. Shorter record. | [Funk et al. 2019](https://doi.org/10.1175/JCLI-D-18-0698.1) |

**Recommendation**: Berkeley Earth Africa annual land temperature, with a 1991–2020 baseline applied (re-anchor from the source's native baseline). Name the data source and baseline in the caption.

The intent of this figure is *engagement* + *defensibility*. Hand-tuned values would fail the second test if a reviewer audited the figure.

## Style — follow STYLE.md

- **Palette**: Hawkins blue-to-red diverging scale. Deliberately *not* the CGIAR Climate Action brand palette — the hero needs to visually contrast with the chrome to grab attention. The brand palette resumes elsewhere on the page.
- **Title**: serif (Noto Serif), large, in CGIAR Primary `#033529`. "Africa is warming." or similar one-sentence framing.
- **Subtitle / labels**: Noto Sans, 11–13 px, in Grey 5 `#5F5E5A`.
- **Year ticks**: 1901, 1950, 2000, 2025 (or analogous).
- **No legend on the figure itself** — the colour scale is intuitive enough; explanatory prose lives in the page below.

## Animation requirements

- SMIL `<animate>` on a `clip-path` rectangle is the simplest approach (used in the interim).
- Cycle: 5–6 s reveal → 2–3 s hold → loop.
- Must work without JavaScript.
- Respect `prefers-reduced-motion` if possible — for the production version, wrap the animation in a `@media (prefers-reduced-motion: no-preference)` block so users with reduced-motion preferences see the static final frame.

## Caption (current draft on the page)

> Africa is warming. Each stripe is one year of continental annual temperature anomaly, 1901–2025; animation reveals the trend year-by-year. *Interim schematic conceptually based on Ed Hawkins's [#ShowYourStripes](https://showyourstripes.info/) design and the AR6 + WMO continental record; the production version will plot from CHIRTS or ERA5.*

For the production version, update to name the actual data source + baseline + the analysis script that produced the values.

## Alt text (current on the page)

Already includes a screen-reader-accessible description of the animation, structure, colour mapping, and the year-by-year reveal. Keep this when replacing the SVG.

## Deliverable

- Overwrite `public/figures/F-africa-warming-stripes-hero.svg` with the real-data version.
- Update the caption in `projections-primer.md` to name the data source and baseline.
- Open a PR or send the file directly to Pete (`p.steward@cgiar.org`).

## Acceptance checklist

- [ ] Real data plotted (CHIRTS / ERA5 / WMO continental series).
- [ ] Baseline named in caption.
- [ ] SMIL reveal animation works in all modern browsers (test in Chromium, Firefox, Safari).
- [ ] Honours `prefers-reduced-motion` — static final frame for reduced-motion users.
- [ ] Alt text matches what the rendered figure actually shows.
- [ ] Legible at 800 px wide on the wiki content column.
