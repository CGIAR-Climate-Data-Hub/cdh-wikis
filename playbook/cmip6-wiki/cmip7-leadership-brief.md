# CMIP7 — leadership brief for CGIAR Climate Action

**Audience:** CGIAR Climate Action programme leadership + Climate Data Hub steering group.
**Date:** June 2026. **Refresh trigger:** quarterly; sooner if NEX-GDDP-CMIP7 announcement lands or FY2027 US science budget signals shift.
**Source:** [`research_anchors_cmip7.md`](research_anchors_cmip7.md) (full detail + citations).

---

## The situation in one paragraph

CMIP7 is being rolled out by WCRP and the modelling centres in 2025–2027 to feed IPCC AR7. The forcings are finalised and on input4MIPs (CC-BY-4.0). Raw model output is just beginning to land on ESGF-NG (launched May 2026), with bulk publication targeted for H2 2026 and stable usability for proposal authors not before late 2027. **No CMIP7-derived downscaled product for African adaptation work exists yet, from any team, anywhere.** The six global downscaling efforts (NASA NEX-GDDP, Climate Impact Lab GDPCIR, CHELSA, ISIMIP, CORDEX, WorldClim) are all gated on raw CMIP7 output and only two (ISIMIP4 and CORDEX-CMIP7) have explicit public plans. Compounding this, the US administration's 2025 cuts have damaged staffing at NASA GISS, NOAA GFDL, and US ESGF infrastructure — Congress restored most FY2026 funding in January 2026 but FY2027 risk is elevated. **The Adaptation Atlas's existing single largest dependency — NEX-GDDP-CMIP7 — has no public release timeline.**

---

## Three decisions for leadership

### 1. Migrate primary data infrastructure to Copernicus C3S

**Recommendation:** treat **Copernicus C3S CDS** (EU-funded, treaty-protected, ECMWF-implemented) as primary; ESGF-LLNL as secondary. C3S is the only redundantly-funded international climate-data infrastructure not subject to US political cycles. **Decision needed by:** September 2026 (before any Atlas data refresh).

### 2. Re-baseline the Atlas ensemble on non-US-led models

**Recommendation:** the African ensemble must be **operational without** GFDL or CESM3. Build first on UKESM2, EC-Earth4, MPI-ICON, IPSL, CNRM, MIROC, ACCESS, CanESM (all confirmed CMIP7 participants from non-US-funding-risk sources). Add US-led models when delivered. **Decision needed by:** start of AR7 cycle planning (2027 Q1).

### 3. Claim production-space for African CMIP7 downscaling

**Recommendation:** initiate a CGIAR-led African-tuned CMIP7 downscaling pipeline (statistical downscaling + bias-correction to CHIRTS/CHIRPS, continental scope). Currently no CGIAR-led, no African-regional-centre-led, no global team has announced an African-tuned product. NEX-GDDP-CMIP7 (the implicit default) has no public timeline and elevated funding risk. **This is the largest single hedge against AAA Atlas dependency failure.** **Decision needed by:** end of 2026 (to ship by 2028 AR7 cycle).

---

## What's already true and not in dispute

- **CMIP6 stays canonical through at least 2027.** NEX-GDDP-CMIP6, CHELSA-CMIP6, ISIMIP3b remain the operational backbone for all CGIAR climate-rationale tools.
- **CMIP7 scenarios are a re-design, not a re-label.** New 7-scenario framework (H, HL, M, ML, L, LN, VL); W/m² suffix dropped; SSP5-8.5 effectively retired (CMIP7 "H" is ~0.9 °C cooler). No clean crosswalk; proposal authors using CMIP6 SSPs through 2027 should plan a re-baselining for the AR7 cycle.
- **ISIMIP4 ships first** (forcings May/June 2026, impact runs through 2026–2027). Highest CGIAR relevance for sector work; lowest funding risk (PIK-led, German-funded). Watch and pilot.
- **CORDEX-Africa CMIP7 is funded and formally chartered.** Slower than statistical downscaling but irreplaceable for dynamical fidelity on extremes and monsoon dynamics. Should anchor the Atlas's eventual extremes pipeline.

## Funding-risk specifics (US contributors)

Congress restored most FY2026 funding in January 2026, **but**:

- **NASA GISS** evicted from Columbia (May 2025). Staff continuity fragile. GISTEMP keep-publishing risk.
- **NOAA GFDL** lost ~10 staff (Feb 2025). Closure proposed and rejected; institution wounded. GFDL CMIP7 submission likely but degraded.
- **NEX-GDDP-CMIP7** — *status uncertain*. No public NASA-NCCS announcement. Direct contact (`bridget.thrasher@nasa.gov`) recommended to learn intent.
- **CESM3 (NCAR/NSF)** — most reliable US contribution. NCAR-Wyoming supercomputer preserved by court order; release targeted spring 2026.
- **ESGF US nodes** — LLNL legacy index decommissioned July 2025; ESGF-NG (Globus, multi-node) launched May 2026. Reinforces the C3S migration case.

---

## Recommended sequencing — what CGIAR does and when

| Quarter | Action |
|---|---|
| **2026 H2** | Stay on CMIP6 in production. Initiate C3S migration (decision 1). Open dialogue with NASA NEX team on CMIP7 intent. Begin scoping a CGIAR-led African downscaling pipeline (decision 3). |
| **2027 Q1** | Pilot ISIMIP4 ingest once forcings published. Confirm Atlas ensemble composition without US-led models (decision 2). |
| **2027 H2** | Adopt NEX-GDDP-CMIP7 *if* it ships and is funded; otherwise execute Climate Impact Lab GDPCIR / CHELSA-CMIP7 / CGIAR-led pipeline as primary downscaled inputs. |
| **2028** | Production CMIP7 across CGIAR, with AFR-13 sub-ensemble re-derived against new CMIP7 model identities. |

---

## What we still don't know

- NEX-GDDP-CMIP7 official timeline (no public statement).
- FY2027 US science-budget posture (signals appear May–September 2026).
- Whether any African regional centre (ICPAC, AGRHYMET, ACMAD) will move from consumer to producer for CMIP7.
- Whether CGIAR can secure funding for a CGIAR-led African downscaling product on a 2027–2028 delivery horizon.

## Key sources

- [WCRP-CMIP — CMIP7 phase page](https://wcrp-cmip.org/cmip-phases/cmip7/)
- [van Vuuren et al. 2026 — ScenarioMIP-CMIP7 design (GMD)](https://gmd.copernicus.org/articles/19/2627/2026/)
- [Dunne et al. 2025 — CMIP7 Assessment Fast Track overview (GMD)](https://gmd.copernicus.org/articles/18/6671/2025/)
- [AIP / FYI — Congress finalising FY2026 science budgets](https://www.aip.org/fyi/congress-set-to-finalize-science-budgets-rejecting-trump-cuts)
- [Carbon Brief — How CMIP7 will shape the next wave of climate science](https://www.carbonbrief.org/guest-post-how-cmip7-will-shape-the-next-wave-of-climate-science/)
- [Copernicus C3S Climate Data Store](https://climate.copernicus.eu/)
- [`research_anchors_cmip7.md`](research_anchors_cmip7.md) — full detail, citations, monitoring sources.

---

*Compiled June 2026 by P. Steward (CGIAR Climate Action / Alliance Bioversity-CIAT) with deep-research synthesis support. For the full knowledge base behind this brief, see [`research_anchors_cmip7.md`](research_anchors_cmip7.md). For ongoing updates: monitoring sources are listed in §9 of that file; this brief should be re-issued quarterly until CMIP7 downscaled products stabilise.*
