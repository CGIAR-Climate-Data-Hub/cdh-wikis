# STYLE.md — wikis repository style guide

This document is the single source of truth for **visual style** of commissioned figures and **per-page content conventions** across the wikis. It complements `CLAUDE.md` (which covers markdown flavour, frontmatter schema, voice, and aside syntax) — read both.

If you're commissioning a figure, see [Visual style for figures](#visual-style-for-figures). If you're writing a wiki page, see [Per-page conventions](#per-page-conventions). If you're making a baseline call, see [Baseline convention](#baseline-convention).

When a new convention emerges that needs to apply across pages, update this file *first*, then propagate. Don't let conventions live in the heads of individual contributors.

## Visual style for figures

Every figure on the wikis should look like it came from the same pen. The rules below are non-negotiable for commissioned figures; for re-used / attributed third-party figures (e.g. cropped IPCC AR6 panels), match what you can and document the deviation in the caption.

### Palette — colour-blind safe

The wiki uses a two-scenario blue / amber palette. Avoid red / green pairings.

| Use | Light fill | Mid line | Dark text |
|---|---|---|---|
| Low scenario (SSP1-2.6, SSP2-4.5, observational baseline) | `#85B7EB` | `#185FA5` | `#0C447C` |
| High scenario (SSP3-7.0, SSP5-8.5, projected upper bound) | `#FAC775` | `#854F0B` | `#412402` |
| Neutral grid / reference | `#D3D1C7` | `#888780` | `#444441` |

For more than two scenarios, add SSP1-2.6 in `#B5D4F4` (lighter blue) and SSP3-7.0 in `#EF9F27` (mid amber) — but four-scenario figures are usually busier than they need to be; if you can crop to two, do.

### Lines, fills, and grids

- **Ensemble-mean line**: 2.5 px stroke, mid-line colour, `stroke-linecap="round"`, `stroke-linejoin="round"`.
- **Inter-model spread envelope**: matching light-fill colour at `fill-opacity` 0.45–0.55, no stroke.
- **Grid lines**: `#D3D1C7` at 0.5 stroke, horizontal only unless the chart genuinely needs a vertical grid.
- **Axes**: solid 1 px stroke, `var(--color-text-primary)`.
- **No drop shadows, gradients, glows, blur, or 3-D effects.** Flat fills only.

### Typography

- **Axis tick labels**: 11 px, secondary text colour.
- **Axis titles**: 11 px, secondary text colour, placed above the y-axis (not rotated) and below the x-axis.
- **Callout labels**: 12 px primary text + 11 px secondary subtitle below if needed.
- **Legend text**: 12 px primary, 11 px secondary for descriptive sub-text.
- **Sentence case everywhere.** Never Title Case, never ALL CAPS. This applies to axis labels, callout text, legend entries, and any text inside the image.
- **No font sizes below 11 px.**
- **Two weights only**: 400 regular, 500 bold (for emphasis or label text). Never 600/700.

### Dimensions

- **Default content-column width**: 800 px. Figures should be legible at this width.
- **Vertical aspect**: time-series charts 800 × 460 (default) or 800 × 400 if compact.
- **Margins** for time-series charts: 80 px left (y-axis ticks), 80–100 px right (legend or right-side callouts), 60 px top, 80 px bottom (x-axis ticks + space for caption).

### Callouts

Annotated figures should follow the "four-callout maximum" rule. More than four becomes cluttered; if a figure needs five, redesign or split.

- **Leader lines**: 0.75 stroke, `var(--color-text-secondary)`, curved with a single Bézier or straight — never zig-zag.
- **Label position**: at the chart margins, not inside the plot area. The four corners of the margin (top-left, top-right, right-side, bottom-left) are the canonical placement.
- **Right-side brackets**: use a square bracket `[` for spanning two end-of-axis values (e.g. "scenario uncertainty" between two ensemble means at 2100).
- **Label text**: 12 px primary line for the term + 11 px secondary subtitle if a quick explanation helps the reader.

### Caption convention

Every `<figure>` caption must name:

1. **What the chart shows** — one sentence, sentence case.
2. **The baseline reference** — e.g. *"Anomalies are relative to the 1991–2020 WMO observational baseline."* Never leave a temperature anomaly without an explicit baseline.
3. **The data source + licence** — e.g. *"Adapted from IPCC AR6 WGI SPM Figure 8 (CC-BY 4.0)."*
4. **Status** if not final — e.g. *"Placeholder — to be commissioned."*

Captions live in `<figcaption>`, not embedded in the image.

### Accessibility

- **Alt text** must be a self-contained description a screen-reader user could follow without the image. Describe the structure (number of lines, what they represent), the trend (rising / falling / steady), and the key features (where lines diverge or converge).
- **No information conveyed by colour alone.** Mean lines must also differ by position or label; envelopes need a line on top of the fill, not fill-only.
- **Colour-blind-safe palette is non-optional** — the blue / amber pair tests well across the common forms of colour-vision deficiency.

## Per-page conventions

These conventions are enforced on every page. CLAUDE.md covers the markdown / frontmatter side; STYLE.md covers section-level structure.

### Section structure

- `:::tip[If you remember one thing]` at the top of any page where a single takeaway can be distilled. Optional but encouraged.
- **Lead each major section with a "so what" sentence** before the explanation. The reader gets the point first, the reasoning second.
- Use `##` for top-level sections, `###` for sub-sections only when essential. Avoid `####`.
- **Define jargon on first use** — bold the term and define inline. Repeat in the glossary if used across pages.
- **End every page with a "Further reading" section** listing 3–6 authoritative links. See below.

### Further reading section — required on every page

Each page ends with `## Further reading` containing 3–6 curated links. The audience for this section is the educated non-specialist user who wants to dig deeper on the page's topic without becoming a climate scientist.

Mix of:

- **IPCC chapters / sections** — link to the IPCC chapter landing page, not the full report PDF.
- **WMO reports** — *State of the Climate in Africa*, *State of the Global Climate*, regional WMO bulletins.
- **Carbon Brief explainers** — best for non-specialist deep dives that are still accurate.
- **Peer-reviewed reviews** — only when they're the canonical entry point for a topic, with DOI.
- **Regional centres** — ICPAC, SADC-CSC, ACMAD, AGRHYMET where appropriate.

Per-page Further reading is **curated**, not exhaustive. The master bibliography lives in `aaa-atlas/references.md`. If a paper is cited inline in the page, it doesn't need to repeat in Further reading unless it's *also* a good deep-dive entry point.

### Frontmatter version

Bump on every significant content change.

- `0.1-stub` — page scaffold; content is "to be written".
- `0.2-draft` — content written, not yet peer-reviewed.
- `0.3-validated` — content reviewed against `research_anchors.md` and externally citable.

### Asides — use sparingly

| Aside | Use for |
|---|---|
| `:::tip[...]` | Headline takeaway at top of page |
| `:::note[...]` | Sidebars, asides, "see also" pointers |
| `:::caution[...]` | Genuine warnings: paradox regions, hot models, baselines that don't unify |
| `:::danger` | Reserved; do not use casually |

### Citations

- **Inline DOI links**: `[Author Year](https://doi.org/...)` — title case the author surname only, year follows.
- **Reports without DOI**: link to the canonical landing page (e.g. IPCC report page, WMO publication page).
- **Master bibliography** lives in `aaa-atlas/references.md`. Update it whenever a new source is cited.
- **No footnotes or numbered bibliographies** — Starlight renders inline links cleanly; numbered systems don't.

## Baseline convention

Every chart that shows a temperature or precipitation anomaly **must name its baseline**. The wikis use the following defaults:

| Context | Baseline | Why |
|---|---|---|
| Wiki projection figures | **1991–2020 (WMO observational)** | Matches the baseline used in [WMO State of the Climate in Africa](https://wmo.int/publication-series/state-of-climate-africa-2024) and the Atlas's Recent Changes view; the most familiar anchor for the wiki's partner audience. |
| Wiki recent-change figures | 1991–2020 (WMO observational) | Same. |
| Re-used IPCC AR6 figures | 1850–1900 (IPCC pre-industrial) | Don't re-baseline IPCC figures — keep the original anchor and explain the offset in the caption. |
| Atlas internal Future Projections data layer | **1995–2014 (CMIP6/AR6 reference)** | Per `project_cr_baseline_conventions` — the Atlas notebook uses the CMIP6 standard reference period; this asymmetry vs the wiki figures is **intentional**. See [baselines.md](src/content/docs/aaa-atlas/baselines.md) (when authored) for the full explanation. |

The ~0.85 °C offset between 1850–1900 and 1995–2014 is documented in IPCC AR6 WGI SPM Box SPM.1. The offset between 1991–2020 and 1995–2014 is small (a few hundredths of a degree) and not always material — but always name your baseline so a reader can convert if they need to.

## Things to avoid

- **Figures without an explicit baseline named in the caption.**
- **Mid-sentence bolding** — use `code style` for entity, class, function names instead. Bold is for headings and labels only.
- **Title Case headings** — sentence case everywhere.
- **Interactive widgets** — locked by CLAUDE.md. No sliders, toggles, scroll-driven explainers, client-side JS. Reference pages stay static.
- **Red / green palette pairings** — colour-blind unsafe.
- **More than four callouts per figure** — re-design instead of cramming.
- **Per-page Further reading sections that dump everything cited inline** — curate for the non-specialist reader.

## When to update this file

Update STYLE.md *before* a new convention propagates across pages — never after. If you find yourself making the same judgement call on a second figure or a third page, that judgement belongs here.

Owner: Pete Steward (`p.steward@cgiar.org`).
