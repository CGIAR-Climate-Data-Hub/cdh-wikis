# Research plan — CMIP6 ensembling for Africa wiki

**Date**: 2026-05-28
**Output**: an Astro-compatible Markdown deliverable, hosted on the **CGIAR Climate Data Hub**, drafted in this repo at `playbook/reference/african_cmip6_ensembling/`.
**Audience**: educated user writing a climate rationale (e.g. for a GCF or AF proposal). Climate-aware but not necessarily a climate-modeller.
**Authoring posture**: explanatory, honest about uncertainty, focused on "what does this mean for *my* proposal", grounded in peer-reviewed sources.
**Status**: plan + first draft of the wiki in this commit. Subsequent passes: figure commissioning, partner outreach, lay-language review.

---

## 1. Why this wiki exists

The Atlas ships per-region CMIP6 sub-ensembles (AFR-13 default plus regional subsets) to give partners better-tuned projections than a global 18-model average. But the *reason* for those choices doesn't fit in 2 paragraphs of Methods text — and partners writing proposals need a defensible answer to "*Why these models, not others?*" that they can cite.

The wiki sits **between** the technical Methods text in the notebook and the primary literature it draws on:

```
[Atlas notebook Methods]  ← 2-paragraph technical summary; links to ↓
[Climate Data Hub wiki]   ← THIS DELIVERABLE — explanatory, illustrated, citation-rich
[Peer-reviewed papers]    ← Samuel 2025, Hausfather 2022, Schwarzwald 2024, etc.
```

Done well, this is **the document a partner team forwards to their reviewer** when asked how they chose the climate ensemble for a proposal.

---

## 2. Scope decisions

**In scope** (this wiki):
- Why model selection matters at all (the orientation)
- The NEX-GDDP-CMIP6 18-model pool and what we can / can't do with it
- Per-region sub-ensembles for African AR6 reference regions, with the regional citation chain
- The hot-model / cold-model problem (CanESM5, INM family) — written in plain language
- The East African Paradox — what it is, why it matters, what we do about it
- How the Atlas's choices affect what you see in the chart
- What's coming: CMIP7 timeline + CORDEX-Africa progress
- Glossary of terms used
- Bibliography with DOI / URL links

**Out of scope** (separate work, or not for this audience):
- Mathematics of model evaluation (Taylor diagrams, skill metrics — referenced but not derived)
- General-purpose primer on climate modelling (we link out, don't reinvent)
- Per-admin1 routing logic — that's a phase-3 implementation question, not a user-facing concern
- The notebook's UI mechanics (lives in the notebook's help affordances, not here)
- Adaptation-planning guidance — separate domain; we make it easier for a planner to *trust* the projections, not tell them what to plan
- Software / implementation details (parquet layout, URL routing) — internal docs, not partner-facing

**Page length target**: ~3500-5000 words for the main page. Scan-readable structure (h2 / h3 with clear scope per heading). Callout boxes for "key takeaways" so a reader skimming for the TL;DR can find it.

---

## 3. Source map — what we cite and why

### Foundation references (cite often)

| Source | Use |
|---|---|
| **Samuel et al. 2025** (J. Climatol.) — NEX-GDDP-CMIP6 over SSA, 28 models, MSWEP + CHIRPS evaluation | Headline source for the "no single best model, but here's what works" argument. Quoted directly. |
| **Hausfather et al. 2022** (Nature) — "Climate simulations: recognize the 'hot model' problem" | Canonical citation for CanESM5 exclusion. |
| **AR6 WGI Chapter 7** (Forster et al. 2021) — IPCC AR6 climate-sensitivity assessment | The authority basis for "very likely ECS range 2.0-5.0 °C". |
| **Schwarzwald et al. 2024** (J. Climate) — East African Paradox in CMIP6 | The East African caveat. |
| **Iturbide et al. 2020** (ESSD) — AR6 reference regions definition | Anchor for the regional structure. |
| **AR6 Interactive Atlas** (Gutiérrez et al. 2021 + IPCC-WG1 Atlas GitHub) | Per-region performance metrics; partner-credible authority. |

### Regional references (cite per-region)

- **West Africa**: Akinsanola et al. 2021 (J. Climate); Makinde et al. 2024 (Int. J. Climatol.); Diallo et al. (multiple)
- **East Africa**: Park et al. 2023 (Climate Dynamics); Ayugi et al. 2021 (Water); Endris et al. 2019 (Climate Dynamics)
- **Southern Africa**: Pinto et al. 2018 (Earth System Dynamics); Lim Kam Sian et al. 2021
- **Central Africa**: limited region-specific lit; defer to Samuel 2025 continental + Pokam et al. (where applicable)
- **East African Paradox specifically**: Wainwright et al. 2019 (npj Clim Atmos Sci); Vellinga & Milton 2018; Tierney et al. 2015

### Forward-look references

- **CMIP7 Fast Track** — WCRP-CMIP pages + ScenarioMIP-CMIP7 (Geosci. Model Dev. 2026)
- **CORDEX-Africa CMIP6** — CORDEX website + CORDEX-CORE pages

### Regional / partner references (to add via outreach)

- **ICPAC** — East Africa regional centre
- **ACMAD** — pan-African centre (Niger)
- **SADC-CSC** — Southern African coordination
- **Kenya Meteorological Department** — high-priority outreach
- **South African Weather Service** — high-priority outreach
- **Ethiopian National Meteorology Agency** — high-priority outreach
- **Ghana Meteorological Agency** — Sahel perspective
- **INSTM Madagascar / Météo Madagascar** — small-island perspective

---

## 4. Figure plan

Six core figures plus a glossary diagram. Each gets a placeholder in the MD with alt-text + caption + source note. CDH team commissions / produces.

| Figure | Type | Source / production | Priority |
|---|---|---|---|
| **F1. AR6 Africa reference regions map** | Vector map, country outlines + region polygons | From Iturbide 2020 shapefile (CC-BY) + Atlas country boundaries. Pete or CDH can produce in QGIS / matplotlib. | P1 — orientation |
| **F2. Why one model isn't enough — Taylor diagram for SSA precipitation** | Taylor diagram of 18 NEX-GDDP-CMIP6 models against CHIRPS over 5 SSA sub-regions | Re-render from Samuel 2025's underlying methodology, or adapt with permission. | P1 — credibility |
| **F3. The "hot model" problem visualised** | Bar chart of the 18 models' ECS values, with AR6 very-likely range overlaid | Original, easy to make. Highlights CanESM5 outside band; INMs at lower edge. | P1 — visual proof of the CanESM5 / INM exclusion argument |
| **F4. East African Paradox — observed vs modelled MAM rainfall trends** | Map pair or scatter — observed (CHIRPS) drying vs CMIP6 modelled wetting over HoA 1981-2024 | Adapt from Schwarzwald 2024 Fig 1 with permission, OR reproduce from Atlas's own CHIRPS + CMIP6 inputs. | P1 — the most-cited caveat needs the visual |
| **F5. Per-region model selection heatmap** | Rows = 18 NEX-GDDP-CMIP6 models, cols = AR6 sub-regions, cells = inclusion in AFR-13 / each regional subset | Original to the Atlas. Designed for at-a-glance "which models for my region." | P1 — partner-facing differentiator |
| **F6. CMIP6 → CMIP7 → CORDEX-Africa roadmap** | Timeline graphic — model gen, release, what changes | Original. Sources from WCRP CMIP7 pages. | P2 — forward-look |
| **G1. (glossary) — ensemble structure diagram** | Simple schematic: forcing → 18 models → ensemble mean / sd | Original, small inline diagram. | P2 — pedagogy |

CDH team may want to produce these as vector graphics (SVG) for site embedding; preview thumbnails referenced from the MD.

---

## 5. National / regional perspectives outreach plan

The §5-§6 of the wiki — national and regional perspectives — are the highest-value content but require partner input. Approach:

### 5.1 Active outreach (preferred for initial publish)

Identify 5-6 contact people / institutions and request a 2-3 paragraph contribution covering:

- What's the position on CMIP6 model performance for our region?
- Which models do we routinely use in our operational forecasting / downscaling?
- Where do we depart from the Atlas's choices (if anywhere)?
- What's a local reference paper readers should know about?

**High-priority contacts** (with Pete's help to identify named individuals):
1. Kenya Met / ICPAC — East Africa & Horn
2. South African Weather Service — Southern Africa
3. Ethiopian NMA — Horn of Africa (paradox-affected)
4. Ghana Met — West Africa
5. Météo Madagascar / IFAS Madagascar — small island

Each contribution is reviewed by Pete + the contributing partner + integrated by the Atlas team with attribution.

### 5.2 Open contribution (after initial publish)

Once the wiki is live, the §5 / §6 sections get a clear "Contribute your perspective" affordance on the CDH page:
- Link to a contribution PR template
- Style guide (length, tone, what to include)
- Editorial review path (Pete + relevant working group)

The §5/§6 sections grow as partners contribute. The wiki commits to keeping a "last reviewed" date per regional entry.

### 5.3 Initial publish without partner contributions

If outreach can't complete in time for the partner-facing rollout, the wiki publishes with §5/§6 as **placeholder sections** that explicitly say "this section seeks contributions from partner institutions — [link]." Less ideal but honest. The wiki ships with the rest of the content intact.

---

## 6. Writing principles (audience: climate rationale writer)

Six rules of style. Reviewed against the draft before publish.

1. **Lead with "so what" for the reader.** Don't open with model architecture; open with "the Atlas is showing you projections from X models; here's why."
2. **Define jargon on first use, bold the term, then use plainly.** "An *ensemble* (a set of climate models run under the same scenario) shows you a range of plausible futures." Glossary at the end for reference.
3. **Use callouts for key takeaways.** Boxed "If you remember one thing from this section…" insertions every 800-1500 words. These are the partner-meeting talking-points.
4. **Acknowledge what we don't know, plainly.** "No CMIP6 model captures the observed East African drying. The Atlas can't fix this; we flag it." Honesty buys credibility.
5. **Show the reader what to do with the information.** Every major section ends with "How this affects your reading of the Atlas" — practical.
6. **Avoid hero-narrative writing about the Atlas.** The reader is using the Atlas; we're not selling them on it. Just give them what they need.

**Tone reference**: think the IPCC AR6 Summary for Policymakers's clarity, scaled down to 4000 words and aimed at a single specialist audience.

---

## 7. Page structure (final, with word-count targets)

| Section | Heading | ~Words | Notes |
|---|---|---|---|
| Hero / TL;DR | "What this page is" | 200 | One-paragraph framing; callout box with 3-bullet TL;DR |
| Why model selection matters | "Why doesn't the Atlas just use 'the' climate model?" | 400 | Plain-language motivation. Figure F2. |
| The model pool | "The 18 NEX-GDDP-CMIP6 models" | 500 | Where the Atlas's data comes from; what was chosen and not chosen at NASA's step. Figure G1. |
| Per-region tuning | "What 'African-tuned' means in the Atlas" | 1000 | The headline. AFR-13 + the regional subsets. Why each region differs. Figure F1 + F5. Inline citations to regional papers. |
| The hot-model problem | "Why we exclude one model called CanESM5" | 500 | The plain explanation. Figure F3. Cite Hausfather + AR6. |
| The East African Paradox | "A known issue over Ethiopia, Kenya, Somalia" | 600 | Honest treatment. Figure F4. Affected countries named. Cite Schwarzwald + Park. |
| How this affects you | "How this affects your reading of the Atlas" | 400 | Practical guidance — what to do with the projections. |
| Coming next | "CMIP7 and CORDEX-Africa — what's coming" | 400 | Forward-look. Figure F6. |
| National / regional perspectives | "Voices from regional centres" | 400 (placeholder) | Outreach pending. Contribution affordance live. |
| Glossary | "Glossary" | 300 | Inline-styled definitions |
| References | "References and further reading" | 250 | DOI / URL list |

**Total**: ~4950 words. Scannable. Defensible. Citable.

---

## 8. Review path (before publish)

1. **Internal Atlas team review** — Pete + Cesare + Brayden. Sanity check the technical claims.
2. **Partner / external sanity-check** — at least one independent climate scientist with African focus reads it cold. Goal: "would I cite this in a proposal?"
3. **Lay-reader pass** — someone from a climate-rationale writing background reads for clarity. Tag every place they had to re-read.
4. **CDH editorial pass** — formatting, links, image rendering, accessibility.
5. **French translation pass** — once English copy is locked.

---

## 9. Maintenance plan

Wiki content has a half-life. Plan for updates:

- **Annual review** anchored on AR (Atlas release cycle) — refresh against any new peer-reviewed evaluations.
- **CMIP7 trigger** — when first CMIP7 results land in late-2026 / 2027, a new section is added; the old CMIP6 section retained as "current" for transition.
- **Partner perspective updates** — open-contribution channel stays active.
- **Versioning** — each significant change increments a version number; old versions retained for citation stability (proposal authors who cited v1.2 don't lose the reference when v2 ships).

---

## 10. Schedule

Conservatively:

- **Day 0** (now): plan + first MD draft (this dispatch + the MD file).
- **Day 0-7**: figure sourcing / commissioning + active outreach begins.
- **Day 7-14**: incorporate partner contributions; review passes.
- **Day 14-21**: CDH editorial pass; publish.
- **Day 21+**: French translation pass; ongoing maintenance.

If the CMIP6 ensemble pipeline + notebook work (phases 1/2) is in flight at the same time, the wiki publishes after those land — so the wiki accurately reflects what the Atlas actually does, not what we plan to do.

---

## 11. Deliverable for this conversation

1. **This research plan** (above).
2. **First-draft Astro-compatible MD** at `playbook/reference/african_cmip6_ensembling/index.md` — covers §1-§11 of the page structure with placeholder figures, full draft text in EN, references + glossary intact, partner-perspective placeholders for §9.

The CDH team can pick the MD up, adapt to their Astro site structure (typically `src/content/<collection>/<slug>.md`), commission the figures, and publish. Pete + team review before publish.
