# Figure commission — F-baselines-timeline

**Status**: interim schematic in place at `src/content/docs/aaa-atlas/figures/F-baselines-timeline.svg`. Polish recommended but not blocking.

**Used on**: `src/content/docs/aaa-atlas/baselines.md`, at the top of the "The three baselines you'll meet" section.

**Final file path**: `src/content/docs/aaa-atlas/figures/F-baselines-timeline.svg` (overwrite interim).

## What the figure must show

A horizontal timeline from **1850 to 2100** with three coloured bars representing the three climate reference periods used in African adaptation work:

1. **1850–1900** (IPCC pre-industrial anchor) — far left, spans 50 years. Coral / warm-brown palette.
2. **1991–2020** (WMO observational normal) — near right, spans 30 years. Blue palette.
3. **1995–2014** (CMIP6 reference period) — overlapping bar 2, spans 20 years. Amber palette.

A vertical dashed line at **2026** marks "today."

Each bar carries a short label naming the baseline, what it's used for, and the institution it's anchored to. A small annotation below the chart notes the ~0.85 °C of observed warming separating the IPCC pre-industrial anchor from the modern baselines.

## Why this figure exists

Readers landing on the baselines page need to *see* that 1850–1900 is far back in time and that 1991–2020 and 1995–2014 are recent and overlapping. The visual makes the temporal asymmetry instant; without it, "three different baselines" reads as abstract numbers in a list.

## Style — follow STYLE.md

- Colour-blind-safe palette: coral + blue + amber (per STYLE.md figure conventions).
- Sentence case throughout. No font sizes below 11 px.
- 800 px-wide composition. Bars 28 px tall, with 22-px gaps between rows.
- Today marker as a dashed vertical line at x = 2026, 11-px "today" label above the plot.
- All labels in `system-ui` / sans-serif fallback so the SVG renders consistently outside Astro.

## Polish options (not blocking)

The interim SVG schematic is functional. A polished version could add:

- **Iconography** alongside each bar — small institutional logos (IPCC, WMO, CMIP) or pictograms. Use a single visual style for the icons.
- **A subtle background gradient** between historical (1850–1980) and modern (1980+) periods to visually separate "deep past" from "living memory."
- **Cleaner typography** — a designer pass via Claude Design ([claude.ai/design](https://claude.ai/design)) or Adobe Illustrator can lift the visual feel without changing the structure.
- **Two-mode rendering** — the figure could plausibly be exported in both light and dark variants if the wiki ever moves to a theme-aware Starlight install.

## Caption (already drafted in the page source)

> **Figure 1.** The three baselines you'll meet, on a single time axis. The IPCC pre-industrial anchor (1850–1900) is far back; the WMO observational normal (1991–2020) and the CMIP6 reference period (1995–2014) are both recent and overlap each other by 20 years. The headline ~0.85 °C offset between the IPCC anchor and the modern baselines is documented in [IPCC AR6 WGI SPM Box SPM.1](https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/).

## Deliverable

- Replace the interim SVG at `src/content/docs/aaa-atlas/figures/F-baselines-timeline.svg`
- Open a PR or send the file to Pete (`p.steward@cgiar.org`)

## Acceptance checklist

- [ ] All three bars labelled, institution names visible.
- [ ] "Today" marker present and dated.
- [ ] ~0.85 °C offset annotation present.
- [ ] Renders cleanly at 800 px width.
- [ ] Alt text in the `<figure>` block matches the rendered figure exactly.
