# `playbook/cmip6-wiki/` — orientation

This directory holds the planning + research artefacts behind the **AAA Atlas CMIP6 Ensembling** wiki section. The wiki pages themselves live in `src/content/docs/aaa-atlas/`; everything here is the *upstream* infrastructure that the wiki writing draws on.

## Files

- **`2026-05-28_v1-research-plan.md`** — the original (focused) research plan for the v0.1 wiki. Shipped as a single page in May 2026.
- **`2026-05-28_v2-deep-research-plan.md`** — the expanded plan covering the v2 multi-page rebuild (14 pages, ~25-35k words). Authored after Pete's "ok but vanilla" review of the v0.1.
- **`research_anchors.md`** — citation backbone: per-topic, the 3-5 best peer-reviewed sources + 2-3 grey-lit anchors. Every claim on a wiki page should map to a source in here.
- **`datasets_inventory.md`** — full catalogue of climate-projection / climate-baseline datasets relevant to African work. Source for the [Dataset landscape](../../src/content/docs/aaa-atlas/dataset-landscape.md) page's comparison table.
- **`grey_lit_inventory.md`** — per-organisation publications inventory. Source for grey-lit citations and partner-outreach planning.

## How to use this when writing a wiki page

1. **Pick the wiki page** you're writing (e.g. `src/content/docs/aaa-atlas/why-models-disagree.md`).
2. **Find the matching section** in `research_anchors.md` (e.g. §A3).
3. **Cite from the 3-5 sources listed.** Use inline DOI / URL links — no footnotes.
4. **Cross-check the grey-lit inventory** (`grey_lit_inventory.md`) for any institutional voice that should be added.
5. **Update `references.md`** in the wiki proper to ensure every cited source also appears in the bibliography.

If you cite a source not yet in `research_anchors.md`, add it — this file evolves with the wiki.

## Status of the v2 build-out

| Phase | Status |
|---|---|
| Phase A — Foundational topic research | ✅ Anchors seeded for §A1-A9 |
| Phase B — Dataset landscape research | ✅ Initial inventory complete |
| Phase C — Grey-lit audit | ✅ Initial inventory complete |
| Phase D — Imagery + tables design | ⏳ Briefs drafted; figures not yet commissioned |
| Phase E — Restructure + write | 🟡 Page stubs scaffolded; per-page content in progress |
| Phase F — Imagery + tables build | ⏳ Tables inline as pages are written; figures pending |
| Phase G — Partner outreach for "Voices" | ⏳ Not yet started |
| Phase H — Review + polish + publish | ⏳ Pending content completion |

See the [v2 deep research plan](./2026-05-28_v2-deep-research-plan.md) for the full phased breakdown.

## Contributing

Both the planning artefacts here and the wiki pages they back are open for contributions. See the top-level `playbook/ADDING_A_NEW_WIKI.md` for the contributor flow.
