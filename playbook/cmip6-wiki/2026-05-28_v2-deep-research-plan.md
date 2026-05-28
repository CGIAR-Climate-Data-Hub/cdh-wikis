# CMIP6 Africa Wiki — v2 Deep Research Plan

**Date**: 2026-05-28
**Trigger**: Pete reviewed the live v0.1 wiki at [https://cgiar-climate-data-hub.github.io/wikis/aaa-atlas/african-cmip6-ensembling/](https://cgiar-climate-data-hub.github.io/wikis/aaa-atlas/african-cmip6-ensembling/) — "ok but vanilla." Feedback:
> *Need images. Need to move away from just talking about NEX-GDDP. Need to introduce the topic — what are future projections, what are GCMs, why do they differ, how do we choose, what is bias correction and downscaling, what datasets are available. Include tables. Deep research so it appears authoritative; consult grey literature from major regional and global orgs.*

**Status**: research plan only — implementation across multiple sessions / multiple dispatches. This plan is the orientation document so the team (and any AI agent that picks the work up) doesn't lose the thread.

**Owner**: Pete-led. Claude / Claude Code execute phases per dispatched chunks.

---

## 1. Vision — what v2 should be

A **comprehensive, partner-credible reference** on climate-model ensemble selection for African adaptation work — structured as a teaching path that any climate-rationale writer can read top-to-bottom or skim section-by-section. The Adaptation Atlas's specific NEX-GDDP-CMIP6 choices become **one chapter** of a broader work, not the whole point.

Tone: authoritative but accessible. The reader should walk away able to:

1. Explain *what* a CMIP6 ensemble is and *why* we use them.
2. Defend the choice of dataset (NEX-GDDP vs CORDEX vs ISIMIP vs others).
3. Cite the regional evaluation literature for their proposal target.
4. Frame uncertainty honestly — including the East African Paradox.
5. Anticipate what's coming (CMIP7, CORDEX-Africa, etc.).

What v0.1 does well: focused, opinionated, defensible on its specific topic. What v0.1 lacks: scope, scientific introduction, dataset landscape, tables, figures, grey-lit grounding.

## 2. Target structure — multi-page wiki

Restructure from a single ~5,000-word page into a navigable multi-page section in Astro Starlight. Each page is self-contained but cross-linked.

| Page | Slug | Length | Audience hook |
|---|---|---|---|
| 1 | Overview | `aaa-atlas/` (existing) | "What's this section about" |
| 2 | **Climate projections for Africa — a 10-minute primer** | `aaa-atlas/projections-primer` | "I'm new to all this" |
| 3 | **Climate models 101** | `aaa-atlas/climate-models-101` | "What is a GCM?" |
| 4 | **Why models disagree** | `aaa-atlas/why-models-disagree` | "Why isn't there one number?" |
| 5 | **Downscaling: from global to local** | `aaa-atlas/downscaling` | "Why 0.25° resolution matters" |
| 6 | **Bias correction explained** | `aaa-atlas/bias-correction` | "How is the raw output adjusted?" |
| 7 | **The dataset landscape** | `aaa-atlas/dataset-landscape` | "What's available and what should I use?" |
| 8 | **Evaluating models for Africa** | `aaa-atlas/regional-evaluation` | "Per-region: who's best?" |
| 9 | **African CMIP6 Ensembling (the Atlas approach)** | `aaa-atlas/african-cmip6-ensembling` (existing — refactor) | "What we actually do" |
| 10 | **The East African Paradox** | `aaa-atlas/east-african-paradox` | "The most important caveat" |
| 11 | **What's next — CMIP7 + CORDEX-Africa** | `aaa-atlas/future-projections` | "What's coming" |
| 12 | **Voices from the field** | `aaa-atlas/voices` | Partner contributions |
| 13 | **Glossary** | `aaa-atlas/glossary` | Quick reference |
| 14 | **References** | `aaa-atlas/references` | Bibliography |

Total target: **~25,000-35,000 words** across the section. Each page targets 1,500-3,500 words — short enough to read in 8-12 minutes, long enough to be authoritative.

## 3. Research workplan — six phases

### Phase A — Foundational topic research (2-3 days)

For each foundational topic, identify the canonical primary literature and the grey-lit anchor. **The goal is not to read everything; it's to identify the 3-5 best sources per topic so the wiki cites authoritatively rather than randomly.**

| Topic | Primary literature anchor | Grey-lit anchor | Web search queries |
|---|---|---|---|
| What is future climate projection? | IPCC AR6 WGI SPM + Chapter 1 + Atlas | WMO State of the Climate; Copernicus C3S reports | "IPCC AR6 climate projection definition"; "future climate scenarios primer" |
| What is a GCM? | Eyring et al. 2016 (CMIP6 design); AR6 Chapter 1; Hourdin et al. 2017 (model tuning) | NCAS-Climate primer; Climate Lab Book (Ed Hawkins) | "CMIP6 model design overview"; "climate model primer non-specialist" |
| Why models disagree | Knutti & Sedlacek 2013 (Nature Climate Change); Tebaldi & Knutti 2007; Sanderson et al. 2015 (model genealogy); AR6 Chapter 4 | IPCC AR6 Interactive Atlas explainer; Carbon Brief explainers | "inter-model uncertainty CMIP6"; "model genealogy climate" |
| Downscaling — statistical vs dynamical | Maraun & Widmann 2018 (textbook); Gutiérrez et al. 2019; Lange 2019 (ISIMIP3 bias adjustment + downscaling) | CORDEX overview; AR6 Chapter 10 on regional information | "statistical vs dynamical downscaling"; "CORDEX dynamical downscaling Africa" |
| Bias correction | Cannon et al. 2015 (multivariate); Ehret et al. 2012 (don't always; caveats); Maraun 2016 (review) | World Bank Climate Knowledge Portal methodology; Copernicus CDS BCSD docs | "bias correction climate model"; "BCSD quantile mapping" |
| Hot model / ECS / constrained projections | Hausfather et al. 2022 (Nature); Sherwood et al. 2020; Brunner et al. 2020; Forster et al. 2021 (AR6 Ch 7) | IPCC AR6 SPM box on ECS; AR6 Interactive Atlas constrained-projections page | "CMIP6 hot model problem"; "constrained climate projection" |
| African evaluation lit | (already in v0.1) Samuel 2025, Akinsanola 2021, Park 2023, Pinto 2018, Schwarzwald 2024, Wainwright 2019, Endris 2019 | ACPC reports; SADC-CSC technical notes; ICPAC seasonal-forecast technical bulletins | "CMIP6 evaluation Africa"; "<region> CMIP6 performance" |

**Deliverable**: a `research_anchors.md` worksheet inside the wikis repo's playbook/ that lists, per topic, the 3-5 canonical references + 2-3 grey-lit links. This worksheet becomes the citation backbone for the writing.

### Phase B — Dataset landscape research (2-3 days)

Catalogue every climate dataset relevant to African adaptation work — what it is, what's in it, what it's good for, what its limitations are. Visible deliverable is **the dataset-landscape page (#7)**, which should carry a comparison table dense enough to be useful as a standalone reference.

Datasets to cover:

| Family | Specific dataset | Spatial | Temporal | Bias-corrected? | Source |
|---|---|---|---|---|---|
| **Raw CMIP6** | CMIP6 ESGF archive | Native model grid (~1°-2.5°) | Historical + SSP scenarios | No | ESGF (https://esgf.llnl.gov/) |
| **Statistical downscaling** | NEX-GDDP-CMIP6 | 0.25° (~25 km) | 1950-2100 | Yes (BCSD) | NASA NCCS |
| **Statistical downscaling** | NEX-DCP30 | ~800 m (USA only) | Older / superseded | Yes | NASA |
| **Statistical downscaling** | CHELSA-CMIP6 | 1 km | 1979-2100 | Yes | WSL Switzerland |
| **Statistical downscaling** | CIL-GDPCIR (Climate Impact Lab) | 0.25° | 1950-2100 | Yes | Climate Impact Lab |
| **Statistical downscaling** | WorldClim Future | 30s-10' | 2021-2100 timeslices | Statistical | WorldClim consortium |
| **Statistical downscaling** | NorESM-NEX | Variant | Limited | Yes | NASA |
| **Statistical bias adjustment** | ISIMIP3b | 0.5° | Historical + SSP | Yes (ISIMIP3BASD) | ISIMIP (PIK) |
| **Dynamical downscaling (CMIP5-era)** | CORDEX-Africa | 0.44° (44 km), 0.22° (22 km) | Historical + RCP | Mostly raw | CORDEX |
| **Dynamical downscaling (CMIP6-era)** | CORDEX-CMIP6 | 0.22° | In progress | Mostly raw | CORDEX |
| **Dynamical downscaling** | CORDEX-CORE | 0.22° | Historical + RCP/SSP | Mostly raw | CORDEX-CORE |
| **Reanalysis (historical baseline)** | ERA5 / ERA5-Land | 0.25° / 0.1° | 1940-present | n/a (reanalysis) | ECMWF / Copernicus |
| **Reanalysis** | MERRA-2 | 0.5° | 1980-present | n/a | NASA |
| **Reanalysis** | JRA-55 | ~55 km | 1958-present | n/a | JMA |
| **Observational gridded** | CHIRPS / CHIRTS / CHIRTS-ERA5 | 0.05° | 1981-present | n/a (obs) | UCSB CHC |
| **Observational gridded** | GMFD (Princeton) | 0.25° | Historical | n/a | Princeton |
| **Aggregated impact data** | ISIMIP3b impact-sector outputs | 0.5° | Historical + SSP | Driven by ISIMIP3b | ISIMIP |
| **Interactive Atlas data** | AR6 IPCC Interactive Atlas | 1° (CMIP6) | Per AR6 cycle | Mix | IPCC |

**Each entry on the dataset-landscape page** should answer: *what it is, what's in it, native resolution / variables / timeframe, bias-corrected by what method, where to get it, what it's best used for, what its limitations are, citation*.

**Grey-lit anchors per dataset**: each major dataset has technical documentation that explains "what we did and why" — for the wiki, find and cite these.

**Deliverable**: a worksheet `datasets_inventory.md` capturing the above table with full provenance + citations + URL-checked links, plus a 1-paragraph "what it's best for" assessment per entry.

### Phase C — Grey literature audit (3-4 days)

The most distinctive content the v0.1 wiki lacks is **grey-lit grounding**. Authoritative regional voices buy partner credibility in a way that primary literature alone doesn't. Sources to audit:

#### Continental / pan-African organisations

- **WMO Africa Regional Office** — annual State of the Climate reports, regional climate outlooks. Search target: most recent 2-3 State of Climate Africa reports.
- **ACMAD (African Centre of Meteorological Applications for Development)** — Niamey, Niger. Continental seasonal outlooks, model evaluation technical notes. Search target: any post-2020 publications on CMIP6 use in Africa.
- **UNECA-ACPC (African Climate Policy Centre)** — climate-science framing for African policy. Useful for the "audience hook" framing on the primer page.
- **AfDB Africa Adaptation Initiative** — funding-side documents that pull through climate-science context. Useful for tone-matching the climate-rationale audience.
- **WMO Regional Climate Centres (RCC) — Network for Africa** — operational climate-services centres; their methodology docs sometimes name specific GCMs.

#### Regional centres

- **ICPAC (IGAD Climate Prediction and Applications Centre)** — Nairobi. East Africa + Greater Horn. Their seasonal-forecast technical bulletins are gold for the East African Paradox section.
- **SADC-CSC (Climate Services Centre, SADC)** — Gaborone. Southern Africa. Has produced CMIP-evaluation reports.
- **AGRHYMET** — Niamey. West Africa Sahel. Strong on hydrological / agro-met modelling.
- **CSAG (Climate System Analysis Group, University of Cape Town)** — academic but functions as a regional centre. Published widely on CMIP evaluation over Southern Africa. *Bruce Hewitson + colleagues are the long-standing reference.*

#### Global organisations

- **WCRP (World Climate Research Programme)** — runs CMIP. Authoritative on what's coming in CMIP7.
- **IPCC AR6 + Atlas** — the headline authority for the synthesis voice. Reference often.
- **World Bank Climate Knowledge Portal** — partner-facing summaries; useful for tone calibration.
- **FAO climate publications** — agricultural-climate framing; matches the Atlas audience.
- **CGIAR-CCAFS legacy publications** + **AICCRA project deliverables** — closest analogues to the kind of wiki we're writing.
- **GCF technical guidance** — what reviewers expect to see; framing for the "what your reviewer will ask" voice.
- **UNFCCC NDC syntheses** — how African countries are using climate projections in NDCs.

#### Specific publications worth pulling

Tentative list — refine in Phase C as we search:

- WMO *State of the Climate in Africa 2023* (and later)
- ICPAC *Greater Horn of Africa Outlook* (most recent seasonal forecast technical document)
- AGRHYMET Special Bulletin on CMIP6 (if exists)
- ACPC reports — *Climate Risk and Adaptation in Africa* series
- CGIAR-CCAFS *Climate Information Services* working papers (multiple, ~2018-2023)
- AICCRA technical deliverables on climate-projection use
- World Bank's *Africa Climate Change Adaptation* technical reports
- Brown et al. 2017 *Modelling climate change-induced agricultural impacts in West Africa* (ECOWAS-funded; example of how regional bodies use CMIP)

**Deliverable**: a worksheet `grey_lit_inventory.md` with a per-organisation breakdown: most-recent relevant publications, contact / URL, what they're good for in the wiki.

**Note on access**: some grey lit is paywalled or behind member-only portals. Where that's the case, note it; we may need to ask partners directly for the document.

### Phase D — Imagery + tables design (1-2 days)

The v0.1 wiki references 6 figure placeholders but the v2 should have ~15-20. Design briefs to commission:

#### Figures — commission as SVG / PNG

| # | Figure | Type | Source / production approach | Page |
|---|---|---|---|---|
| F1 | The climate model "tree" — global → regional → bias-corrected → impact | Conceptual diagram | Original to wiki | Page 2 (primer) |
| F2 | AR6 reference regions over Africa | Map | From Iturbide 2020 shapefile (CC-BY) + Atlas borders | Pages 8, 9 |
| F3 | Components of a GCM (atmosphere, ocean, land, ice, vegetation) | Architecture diagram | Original; adapt from IPCC AR6 Fig 1.8 | Page 3 |
| F4 | Why models disagree — fan chart of CMIP6 projections | Original chart | Re-render from CMIP6 ESGF data | Page 4 |
| F5 | Downscaling concept (global → regional) | Conceptual diagram | Original | Page 5 |
| F6 | Statistical vs dynamical downscaling — side by side | Conceptual diagram | Original | Page 5 |
| F7 | Bias correction concept (raw vs adjusted CDF) | Conceptual diagram | Original | Page 6 |
| F8 | Dataset timeline — when each became available | Timeline graphic | Original | Page 7 |
| F9 | Dataset coverage matrix (Africa, resolution, downscaled?, bias-corrected?) | Heatmap-style table | Original | Page 7 |
| F10 | Taylor diagram for SSA precipitation — adapted from Samuel 2025 | Taylor diagram | Re-render / adapt | Page 8 |
| F11 | Per-region best-N model heatmap | Heatmap | Original to Atlas | Pages 8, 9 |
| F12 | CMIP6 model ECS distribution + AR6 ranges | Bar chart | Original | Page 9 |
| F13 | East African Paradox — observed vs modelled trend maps | Map pair | Adapt from Schwarzwald 2024 with permission | Page 10 |
| F14 | CMIP6 → CMIP7 → CORDEX-Africa roadmap | Timeline | Original | Page 11 |
| F15 | Atlas decision flowchart — "which ensemble for my country?" | Flowchart | Original | Page 9 |
| F16 | Global CMIP6 model contributing institutes | World map | Original | Page 3 |
| F17 | Continental seasonal climatology overview (Africa precipitation) | Climatology map | From CHIRPS | Pages 2, 8 |
| F18 | Mediterranean / Sahel / Guinea coast / East Africa / Southern Africa rainfall regimes | Multi-panel climatology | Original | Page 8 |

**Production approach**:
- **Originals** — produce as SVG with consistent visual style. Use a common colour palette (likely a CGIAR-aligned palette).
- **Adapted figures** — request permission from publishers / authors. For IPCC AR6 figures, CC-BY-4.0 with attribution is the standard; for journal figures, written permission needed.
- **Tooling** — Matplotlib / ggplot for data charts; Mermaid or Excalidraw for conceptual diagrams; QGIS for maps.

#### Tables — produce inline in markdown

| # | Table | Page |
|---|---|---|
| T1 | The 18 NEX-GDDP-CMIP6 models with provenance, ECS, model family | Page 9 |
| T2 | Comparison of major climate-projection datasets for African work | Page 7 |
| T3 | Downscaling methods — statistical vs dynamical (pros / cons / when to use) | Page 5 |
| T4 | Bias-correction methods — methods table (delta, quantile mapping, BCSD, ISIMIP3BASD) | Page 6 |
| T5 | AR6 reference regions for Africa — countries per region | Pages 2, 8 |
| T6 | Per-region best-N sub-ensembles (the Atlas's choice) | Page 9 |
| T7 | Glossary table | Page 13 |
| T8 | Common abbreviations table | Page 13 |

**Tables go in markdown directly**, no Astro components needed.

### Phase E — Restructure + write (1-2 weeks)

Per-page targets, page-by-page in dependency order:

1. **Glossary + References pages first** (1 day). Set up the citation infrastructure so other pages can link to it.
2. **Climate projections primer** (2 days). Establishes vocabulary + framing.
3. **Climate models 101** (2 days). Where GCMs come from, what's inside them.
4. **Why models disagree** (1.5 days). Inter-model uncertainty + structural uncertainty.
5. **Downscaling** (1 day). Statistical vs dynamical, with the textbook references.
6. **Bias correction** (1 day). What it is, why, when not to.
7. **Dataset landscape** (2 days). The big comparison table + per-dataset write-ups.
8. **Evaluating models for Africa** (2 days). Per-region literature synthesis.
9. **Atlas approach** (1 day — refactor existing). What we do specifically.
10. **East African Paradox** (1 day). Standalone page; expand from current draft.
11. **Future — CMIP7 / CORDEX** (1 day). Forward-look.
12. **Voices from the field** (placeholder + outreach).

**Total**: ~16-18 days of focused authoring time, parallelisable across Pete + Claude + Claude Code. Could compress to 8-10 days with a tight sprint.

### Phase F — Imagery + tables build (parallel to E)

Two tracks:

- **Tables** — built inline by whoever is writing each page. Fast.
- **Figures** — commission or produce. Originals can be drafted as ASCII / Mermaid placeholders during writing; replace with proper SVG / PNG before publish.

**Recommendation**: get *placeholder* figures (the same ones that ship with v0.1) into every figure slot before writing each page. The writing can reference figures with the understanding they'll be polished after. This keeps the writing from blocking on figure work.

### Phase G — Partner outreach for "Voices from the field" (parallel to E + F)

Active outreach to 5-6 partner contacts. Per the v0.1 plan in §9.5, recommend:

- Kenya Meteorological Department / ICPAC
- South African Weather Service
- Ethiopian National Meteorology Agency
- Ghana Meteorological Agency
- Météo Madagascar / INSTM Madagascar
- (Stretch) ACMAD or AGRHYMET central contacts

Ask each for 2-3 paragraphs:
- What's your institution's position on CMIP6 model performance for our region?
- Which models do you favour for operational forecasting / downscaling?
- Where do you depart from the Atlas's defaults?
- One local reference paper / report we should cite.

Each contribution credited to the contributing institution with reviewer attribution.

### Phase H — Review + polish + publish

1. **Internal Atlas team review** — Pete + Cesare + Brayden + Atlas working group.
2. **External climate scientist sanity check** — at least one independent climate scientist with African focus.
3. **Lay-reader pass** — someone from a climate-rationale writing background.
4. **CDH editorial pass** — formatting, links, accessibility, mobile readability.
5. **French translation pass** — once English is locked. Major work; budget separately.

## 4. Sequencing — recommended dispatch plan

If the work is going to be broken into dispatches handed to Claude Code (or another contributor) in chunks, suggested sequencing:

1. **Dispatch 1 — Research worksheets** (~2-3 days). Build the three worksheets: `research_anchors.md`, `datasets_inventory.md`, `grey_lit_inventory.md` in the wikis repo's playbook/. No new wiki pages yet.
2. **Dispatch 2 — Page scaffolding** (~1 day). Create empty stubs for all 14 pages with frontmatter + section-heading scaffolding + cross-link skeleton + sidebar registration. No content yet.
3. **Dispatch 3 — Glossary + References + Voices placeholder** (~1 day). Build the citation infrastructure.
4. **Dispatch 4 — Conceptual pages** (~3-4 days). Climate projections primer, Climate models 101, Why models disagree, Downscaling, Bias correction. These are the "teaching" content; they don't depend on the Atlas-specific decisions.
5. **Dispatch 5 — Dataset landscape page** (~2 days). The dataset table + per-dataset write-ups. Authority-heavy; needs careful citation.
6. **Dispatch 6 — Evaluating models for Africa** (~2 days). Per-region synthesis.
7. **Dispatch 7 — Refactor existing pages** (~1 day). Adapt the current `african-cmip6-ensembling.md` to fit the new structure; split off the East African Paradox into its own page; rebuild the AAA overview.
8. **Dispatch 8 — Future-look page** (~0.5 days). Light content.
9. **Dispatch 9 — Figures commissioned + integrated** (parallel; ~1-2 weeks elapsed).
10. **Dispatch 10 — Review cycle** (review-driven; ~1 week).

Pete can choose to action dispatches 1-3 first to set up infrastructure, then parallel-dispatch 4 + 5 + 6 to Claude Code while doing partner outreach himself.

## 5. Open decisions for Pete before dispatch 1 lands

1. **Scope confirmation**: 14 pages, ~25-35k words total. Acceptable? Or pare back to ~8 pages, ~15k words?
2. **Production approach for figures**: commission externally (CDH design team or a freelancer), or produce in-house with matplotlib / Excalidraw? My recommendation: in-house drafts → CDH design team polishes for partner-facing publish.
3. **Outreach timing**: start partner outreach now (parallel to dispatch 1) or wait until the content is more mature? My recommendation: start now — partners take time to respond; better to have their contributions land in time for the publish push.
4. **Visual style guide**: should I produce a small style guide (colour palette, font choices, callout patterns) as part of dispatch 2 so all figures match? Recommended yes.
5. **Versioning policy**: when v2 ships, does v0.1 stay at its current URL (frozen) or get overwritten? My recommendation: overwrite, but bump the `version` field in frontmatter to `1.0` so anyone who cited v0.1 sees a clear "this has been substantially expanded since you last looked."

## 6. Risks + mitigations

| Risk | Mitigation |
|---|---|
| **Scope creep** — easy to keep adding pages | Stick to the 14-page structure; new topics get queued for v3, not added to v2 |
| **Grey-lit access** — paywalled / hard-to-find docs | Where blocked, note clearly and ask partners directly; document gaps |
| **Figure delays** — commissioned figures take weeks | Use ASCII / Mermaid placeholders during writing; ship v2 with placeholders if needed and update progressively |
| **Partner-contribution delays** | §12 "Voices" can ship as an open call; contributions land iteratively |
| **Authoritative tone drift** — temptation to opinionise | Maintain the v0.1 stylebook: lead with so-what, define jargon, acknowledge uncertainty, link not opine |
| **Becoming "yet another climate primer"** | Keep the audience anchor: climate-rationale writer preparing a proposal. Every section closes with "how this affects your work." |

## 7. Maintenance plan (post-publish)

- **Annual review** — refresh against any major new African evaluation paper.
- **CMIP7 trigger** — when first results land (late 2026 / 2027), add a section; retain CMIP6 content as "current" during transition.
- **Partner contributions** — open-contribution model after initial publish.
- **Versioning** — each significant change bumps the version number; old versions retained for citation stability.

## 8. Pointers

- **v0.1 wiki (live)**: https://cgiar-climate-data-hub.github.io/wikis/aaa-atlas/african-cmip6-ensembling/
- **v0.1 source**: `wikis/src/content/docs/aaa-atlas/african-cmip6-ensembling.md`
- **v0.1 research plan** (this dispatch's predecessor): `atlas_notebooks/playbook/handovers/climateRationale/dispatches/2026-05-28_cmip6-wiki-research-plan.md`
- **v0.1 source dispatch** (the methodology paper this wiki defends): `atlas_notebooks/playbook/handovers/climateRationale/dispatches/2026-05-28_african-cmip6-sub-ensembles-research.md`
- **Wikis repo conventions**: `wikis/CLAUDE.md` and `wikis/playbook/ADDING_A_NEW_WIKI.md`

---

## End of dispatch
