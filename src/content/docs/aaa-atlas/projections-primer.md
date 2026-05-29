---
title: "Climate projections for Africa — a 10-minute primer"
description: "An accessible orientation to what climate projections are, what they're used for, and how to read them — written for non-specialists who are about to use them in adaptation work."
area: AAA Adaptation Atlas
version: "0.2-draft"
estimatedReadingMinutes: 10
sidebar:
  order: 5
  label: "Projections primer"
tableOfContents:
  minHeadingLevel: 2
  maxHeadingLevel: 3
---

:::tip[If you remember one thing]
A climate projection isn't a forecast of what will happen. It's a model's answer to "*if emissions follow trajectory X, here's what the physics says could happen.*" The honest reading of any projection chart is always: **which scenario, which models, and how much do they agree** — not a single number.
:::

## What this page covers

Your 10-minute orientation to climate projections for African adaptation work. By the end you'll know:

- What a "future climate projection" actually is (and what it isn't)
- The three sources of uncertainty in every projection chart you'll see
- How to read a projection chart honestly — central estimate, spread, scenario dependence
- Where projections fit into a climate-rationale workflow
- What the rest of this wiki section can answer for you

## What a projection is, and isn't

A **climate projection** is a model-based answer to the question *what would happen to the climate if greenhouse-gas emissions and land use follow a specific future trajectory?* That trajectory is called a **scenario**. For CMIP6, scenarios are the [Shared Socioeconomic Pathways](/wikis/aaa-atlas/glossary/) (SSPs) — SSP1-2.6 (sustainability), SSP2-4.5 (middle of the road), SSP3-7.0 (regional rivalry), SSP5-8.5 (fossil-fuelled development).

Projections are **not predictions**. A prediction would assume we know which scenario will play out; we don't. A projection says: *given* this scenario, the climate would behave roughly like this. Every projection chart you read is conditional on a choice the chart-maker made about emissions ([IPCC AR6 WGI Ch 1](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-1/); [AR6 WGI Summary for Policymakers](https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_SPM.pdf)).

## Where projections come from — the short version

Projections come from **global climate models** ([GCMs](/wikis/aaa-atlas/glossary/)) — large physics-based simulations run at major modelling centres around the world. CMIP6, the current coordinated experiment, gathered runs from ~50 models; the Atlas ingests 18 of them via NASA's statistically-downscaled NEX-GDDP-CMIP6 product. The next page goes deep: [Climate models 101](/wikis/aaa-atlas/climate-models-101/).

## The three sources of uncertainty

[Hawkins & Sutton (2009)](https://doi.org/10.1175/2009BAMS2607.1) gives the standard framing — every projection carries three layered uncertainties, and you should know which one dominates for your time horizon:

- **Scenario uncertainty** — we don't know which emissions path will play out (which SSP humanity ends up on).
- **Model uncertainty** — even given a scenario, different models give different answers because they represent atmosphere, ocean, land, and clouds differently.
- **Internal variability** — the climate's own year-to-year and decade-to-decade noise, driven by modes like ENSO and the monsoon. It doesn't go away with averaging across models.

A rough rule: for **near-term horizons (2030s)**, internal variability dominates the spread. For **end-of-century horizons (2080s+)**, scenario uncertainty does. Model uncertainty is in the middle and matters most at the **regional** scale — which is exactly where you're working.

## How to read a projection chart

A typical chart shows two things layered on top of each other:

- An **ensemble mean** — a single thick line through the average of multiple models. This is your central estimate.
- A **spread band** — usually shaded — showing the inter-model range (typically ±1 standard deviation, or the 17–83% inter-model interval). This is the uncertainty.

If multiple emissions scenarios are shown, each one gets its own coloured mean-and-spread band. The bands almost always overlap in the near term and diverge later as scenario uncertainty grows.

If a chart shows **only the mean and not the spread**, half the story is missing — treat it with caution and look for the source's underlying data. Honest charts always include the spread.

<figure>
<img src="./figures/F-projection-chart-anatomy.png" alt="Annotated time-series chart showing two SSP scenario bands from 2020 to 2100. Each band has a thick central line (ensemble mean) and a shaded envelope (inter-model spread). The bands overlap near-term and diverge after 2050. Labels point to: ensemble mean, inter-model spread, scenario uncertainty, and near-term overlap zone.">
<figcaption><strong>Figure 1.</strong> Anatomy of a multi-model projection chart. Each coloured band represents one emissions scenario: the thick line is the ensemble mean across models; the shading is the inter-model spread (typically the 17–83 % range). Near-term bands overlap because internal variability dominates; end-of-century bands diverge as scenario choice becomes the largest source of uncertainty. placeholder — to be commissioned</figcaption>
</figure>

## Where this fits in a climate rationale

A defensible climate rationale for a Green Climate Fund concept note, an Adaptation Fund proposal, or a national NAP submission usually has four parts:

1. **Observed climate context** — the current baseline. Best continental source: [WMO State of the Climate in Africa 2024](https://wmo.int/publication-series/state-of-climate-africa-2024) (African temperature anomaly +0.86 °C vs the 1991–2020 baseline; North Africa fastest-warming; 2024 saw Sahel floods and Kenya MAM floods).
2. **Observed change** — recent trends in temperature, rainfall, extremes.
3. **Projected change** — what *this* wiki section helps you cite defensibly.
4. **Adaptation logic** — how the projected changes drive the intervention you're proposing.

Projections sit in part (3), but always read alongside (1) and (2) — a projection that *contradicts* the observed trend (as for East African long rains; see [East African Paradox](/wikis/aaa-atlas/east-african-paradox/)) is a known-difficult case, not a free pass to use the model number.

## What this wiki section can answer

| Question | Page |
|---|---|
| What's actually inside a climate model? | [Climate models 101](/wikis/aaa-atlas/climate-models-101/) |
| Why do models disagree? | [Why models disagree](/wikis/aaa-atlas/why-models-disagree/) |
| What does "downscaled" mean? | [Downscaling](/wikis/aaa-atlas/downscaling/) |
| What does "bias-corrected" mean? | [Bias correction](/wikis/aaa-atlas/bias-correction/) |
| Which datasets exist and what should I use? | [Dataset landscape](/wikis/aaa-atlas/dataset-landscape/) |
| Which models work best over my region? | [Regional evaluation](/wikis/aaa-atlas/regional-evaluation/) |
| What does the Atlas specifically use? | [Atlas approach](/wikis/aaa-atlas/african-cmip6-ensembling/) |
| Why is East African rainfall a special case? | [East African Paradox](/wikis/aaa-atlas/east-african-paradox/) |
| What's coming next? | [CMIP7 + CORDEX-Africa](/wikis/aaa-atlas/future-projections/) |
