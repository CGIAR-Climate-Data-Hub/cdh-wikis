# Dataset inventory — climate-projection datasets for African work

This worksheet is the source for the **Dataset landscape** wiki page (page #7 of the v2 structure). It catalogues every climate-projection or climate-baseline dataset that an African adaptation analyst is likely to encounter, with provenance, methodology, "what it's best for," and limitations. The wiki page renders a subset of this as a comparison table; this worksheet carries the full detail (and gets updated as new datasets become available).

**Convention** — each entry has the same eight fields:

```
Name — short
Sponsor / producer
Type (raw GCM / statistical downscale / dynamical downscale / reanalysis / observational)
Spatial resolution (native)
Temporal coverage (historical + future)
Bias-corrected? (which method, citation)
What it's best for
Limitations
Where to get it (DOI / portal URL)
```

**Last updated**: 2026-05-28 (initial seeding)

---

## Raw GCM archives

### CMIP6 — ESGF archive

- **Producer**: WCRP-CMIP working group + ~50 modelling centres world-wide
- **Type**: Raw GCM output
- **Native resolution**: Variable per model — typically 1° to 2.5° (~100-250 km)
- **Temporal coverage**: Historical (1850-2014) + SSP1-2.6, SSP2-4.5, SSP3-7.0, SSP5-8.5 (2015-2100); some experiments extend further
- **Bias-corrected?**: No — raw model output
- **What it's best for**: Methods development, scenario sensitivity, ensemble assembly when you need realisation members beyond r1i1p1f1
- **Limitations**: Coarse resolution unusable for impact assessment without downscaling; many variables only at monthly time-step in standard archive; significant variability in which models published which experiments
- **Source**: Earth System Grid Federation [ESGF](https://esgf.llnl.gov/) (multi-node; the LLNL node is the main reference for English-speaking users)
- **Citation**: Eyring et al. 2016 (DOI [10.5194/gmd-9-1937-2016](https://doi.org/10.5194/gmd-9-1937-2016))

### CMIP5 — ESGF archive

- **Producer**: WCRP-CMIP5 group (~40 modelling centres)
- **Type**: Raw GCM output (previous generation)
- **Native resolution**: ~1° to 2.5°
- **Temporal coverage**: Historical (1850-2005) + RCP scenarios (2006-2100)
- **Bias-corrected?**: No
- **What it's best for**: Studies that need consistency with AR5-era literature; CORDEX-Africa is mostly downscaled from CMIP5 GCMs
- **Limitations**: Older generation; AR6 / CMIP6 is the current reference. Use CMIP5 only where required for backward compatibility
- **Source**: [ESGF](https://esgf.llnl.gov/) (CMIP5 project space)
- **Citation**: Taylor, Stouffer & Meehl 2012 (DOI [10.1175/BAMS-D-11-00094.1](https://doi.org/10.1175/BAMS-D-11-00094.1))

---

## Statistically downscaled CMIP6 — global products

### NEX-GDDP-CMIP6

- **Producer**: NASA NEX / Climate Analytics Group
- **Type**: Statistically downscaled and bias-corrected
- **Native resolution**: 0.25° (~25 km)
- **Temporal coverage**: 1950-2100, daily, all four SSPs (126 / 245 / 370 / 585)
- **Bias-corrected?**: Yes — BCSD (Bias-Correction Spatial Disaggregation; Wood et al. 2004 method) against the GMFD (Global Meteorological Forcing Dataset) reference
- **Models**: 18 CMIP6 GCMs at r1i1p1f1 (ACCESS-CM2, ACCESS-ESM1-5, CanESM5, CMCC-ESM2, EC-Earth3, EC-Earth3-Veg-LR, GFDL-ESM4, INM-CM4-8, INM-CM5-0, IPSL-CM6A-LR, KACE-1-0-G, MIROC6, MPI-ESM1-2-HR, MPI-ESM1-2-LR, MRI-ESM2-0, NorESM2-LM, NorESM2-MM, TaiESM1)
- **Variables**: tasmax, tasmin, pr, hurs, huss, rlds, rsds, sfcWind (8 variables, daily)
- **What it's best for**: National and admin-1 level adaptation work over Africa. Compatible resolution for crop / hydrological models. **This is the Adaptation Atlas's primary data source.**
- **Limitations**: Some major CMIP6 models *not* downscaled (UKESM1-0-LL, HadGEM3-GC31-MM, GFDL-CM4); only r1i1p1f1 (no internal-variability realisations); BCSD assumes stationarity of bias — questionable for extreme regions
- **Source**: [NASA NEX-GDDP-CMIP6](https://www.nccs.nasa.gov/services/data-collections/land-based-products/nex-gddp-cmip6)
- **Citation**: Thrasher et al. 2022 (DOI [10.1038/s41597-022-01393-4](https://doi.org/10.1038/s41597-022-01393-4))

### CHELSA-CMIP6

- **Producer**: WSL Institute for Snow and Avalanche Research (Switzerland) + collaborators
- **Type**: Statistically downscaled and bias-corrected; very-high-resolution
- **Native resolution**: 1 km (~0.0083°)
- **Temporal coverage**: 1979-2100, monthly (some daily); SSPs 126 / 370 / 585; specific GCM × SSP subset
- **Bias-corrected?**: Yes — ISIMIP3BASD method (Lange 2019, trend-preserving)
- **Models**: A pre-selected subset of CMIP6 GCMs matched to ISIMIP3 — typically 5 models (GFDL-ESM4, IPSL-CM6A-LR, MPI-ESM1-2-HR, MRI-ESM2-0, UKESM1-0-LL)
- **Variables**: tasmin / tasmax / pr / monthly climate variables
- **What it's best for**: Ecological niche modelling, species distribution, agroecological zoning at very fine resolution. Mountain regions where 25 km is too coarse.
- **Limitations**: Smaller ensemble (5 models, not 18); monthly time-step for most variables; resolution gain partly synthetic (downscaling from 1° to 1 km can't add real information that isn't there)
- **Source**: [CHELSA-CMIP6 portal](https://chelsa-climate.org/cmip6/)
- **Citation**: Karger et al. 2017 (CHELSA v1; DOI [10.1038/sdata.2017.122](https://doi.org/10.1038/sdata.2017.122)). For CHELSA-CMIP6 specifically, cite the [product page](https://chelsa-climate.org/cmip6/) until a definitive peer-reviewed reference is identified — an earlier-cited "Brun et al. 2022 GMD" DOI was hallucinated and has been removed (see citation_verification_report.md).

### CIL-GDPCIR (Climate Impact Lab Global Downscaled Projections for Climate Impacts Research)

- **Producer**: Climate Impact Lab (UC Berkeley + RFF + Rhodium + Chicago)
- **Type**: Statistically downscaled, bias-corrected
- **Native resolution**: 0.25°
- **Temporal coverage**: 1950-2100, daily, SSPs 245 / 370 / 585
- **Bias-corrected?**: Yes — variant of quantile mapping (QDM)
- **Models**: ~25 CMIP6 GCMs (largest downscaled ensemble for the consumer side)
- **What it's best for**: Studies that need a larger ensemble than NEX-GDDP's 18; explicit handling of climate-impact research workflows; tightly licensed for analytical use
- **Limitations**: AWS/S3 access pattern; specific licensing; less penetration into the operational climate-services community than NEX-GDDP
- **Source**: [Climate Impact Lab Data Portal](https://impactlab.org/research/global-downscaled-projections-for-climate-impacts-research)
- **Citation**: Hsiang et al. (Climate Impact Lab) — published methods paper TBD; use the portal documentation

### NEX-DCP30

- **Producer**: NASA NEX (older CMIP5-era product)
- **Type**: Statistical downscale (CMIP5)
- **Native resolution**: ~800 m (USA only — not applicable to Africa)
- **Temporal coverage**: Historical + CMIP5 RCPs
- **Source**: [NEX-DCP30](https://www.nccs.nasa.gov/services/data-collections/land-based-products/nex-dcp30)
- **Notes for the wiki**: Mention only briefly — Africa-relevant readers can ignore; included for completeness.

### WorldClim Future

- **Producer**: Hijmans et al. (WorldClim consortium)
- **Type**: Statistically downscaled monthly climatologies
- **Native resolution**: 30s (~1 km), 2.5'/5'/10' (also)
- **Temporal coverage**: 2021-2040, 2041-2060, 2061-2080, 2081-2100 (time-slice means, not time-series)
- **Bias-corrected?**: Yes (delta change applied to WorldClim historical baseline)
- **What it's best for**: Species distribution modelling, ecological niche analysis. Comparable spatial footprint to WorldClim historical climatologies
- **Limitations**: Climatologies only, not full time series; can't be used for inter-annual variability or extreme-event analysis
- **Source**: [WorldClim Future](https://www.worldclim.org/data/cmip6/cmip6climate.html)
- **Citation**: Fick & Hijmans 2017 (DOI [10.1002/joc.5086](https://doi.org/10.1002/joc.5086))

---

## Statistically downscaled CMIP6 — ISIMIP framework

### ISIMIP3b

- **Producer**: ISIMIP (Inter-Sectoral Impact Model Intercomparison Project) at PIK Potsdam
- **Type**: Statistically bias-adjusted (downscaling is to half-degree, not high-resolution)
- **Native resolution**: 0.5° (~50 km)
- **Temporal coverage**: 1850-2100 daily; historical, hist-nat (counterfactual), SSPs 126 / 370 / 585
- **Bias-corrected?**: Yes — ISIMIP3BASD (Lange 2019; trend-preserving quantile mapping)
- **Models**: 5 CMIP6 GCMs — GFDL-ESM4, IPSL-CM6A-LR, MPI-ESM1-2-HR, MRI-ESM2-0, UKESM1-0-LL
- **What it's best for**: Driving impact-sector models (crops / water / fisheries / health). The standard input for ISIMIP impact-MIPs. Includes the UKESM1-0-LL model that NEX-GDDP-CMIP6 doesn't.
- **Limitations**: Coarse resolution; ensemble of only 5; bias-adjustment specific to ISIMIP's reference observations (W5E5; might not match other observational references partners trust)
- **Source**: [ISIMIP repository](https://data.isimip.org/) — ISIMIP3b bias-adjusted climate forcing
- **Citation**: Lange 2019 (DOI [10.5194/gmd-12-3055-2019](https://doi.org/10.5194/gmd-12-3055-2019)) + Frieler et al. 2024 (ISIMIP3b overview, TBC)

### ISIMIP3a (historical / counterfactual)

- **Producer**: ISIMIP / PIK
- **Type**: Historical + counterfactual atmospheric forcing
- **Native resolution**: 0.5°
- **Temporal coverage**: 1901-2019, daily
- **What it's best for**: Attribution-style studies; historical baseline driving impact models; counterfactual ("what if no human forcing") simulations
- **Limitations**: Historical only — not for future projections
- **Source**: [ISIMIP repository](https://data.isimip.org/)

---

## Dynamically downscaled CMIP — CORDEX family

### CORDEX-Africa (CMIP5-driven)

- **Producer**: CORDEX African working group (various RCM modelling centres)
- **Type**: Dynamical regional downscaling
- **Native resolution**: 0.44° (~44 km) for CORDEX-AFR-44; 0.22° (~22 km) for CORDEX-AFR-22
- **Temporal coverage**: Historical (1950-2005) + RCPs (2006-2100, RCP4.5 + RCP8.5)
- **Bias-corrected?**: Mostly no (some bias-adjusted sub-products exist)
- **Models**: ~10 GCM × RCM combinations
- **What it's best for**: Studies that need physically self-consistent regional climate, especially for extreme events / convection-permitting questions. CSAG / CSIR has worked extensively with this for Southern Africa.
- **Limitations**: CMIP5-era (older generation); much smaller ensemble than statistical products; RCM choices add another layer of model spread
- **Source**: [ESGF CORDEX project space](https://esgf.llnl.gov/) — search domain = AFR-22 or AFR-44
- **Citation**: Nikulin et al. 2012 (DOI [10.1175/JCLI-D-11-00375.1](https://doi.org/10.1175/JCLI-D-11-00375.1)) + Giorgi & Gutowski 2015 (DOI [10.1146/annurev-environ-102014-021217](https://doi.org/10.1146/annurev-environ-102014-021217))

### CORDEX-CMIP6 (Africa domain, ongoing)

- **Producer**: CORDEX African + global working group
- **Type**: Dynamical regional downscaling, CMIP6-driven
- **Native resolution**: 0.22° (~22 km), targeted
- **Temporal coverage**: Historical + SSPs (in progress; partial coverage as of 2026)
- **Status**: Active build-out 2024-2027; CORDEX-CMIP6 archiving specifications v3 released 2025/2026
- **What it's best for**: When this matures, will be the natural CORDEX-Africa successor to the CMIP5-era runs. Especially valuable for impact studies that need physically consistent extremes.
- **Limitations**: Partial coverage during build-out; check the [CORDEX 2025 activities page](https://cordex.org/domains/domain-activities-2/domain-activities-2025/) for current state
- **Source**: [CORDEX project](https://cordex.org/) + ESGF
- **Citation**: TBD as the methodology paper publishes

### CORDEX-CORE

- **Producer**: CORDEX (a coordinated initiative across all domains)
- **Type**: Standardised dynamical downscaling using a small RCM × GCM matrix
- **Native resolution**: 0.22°
- **Coverage**: All 14 CORDEX domains incl. AFR
- **What it's best for**: Methodologically consistent cross-domain comparisons; smaller ensemble but designed for homogeneity
- **Source**: [CORDEX-CORE](https://cordex.org/)
- **Citation**: cite via [CORDEX project page](https://cordex.org/) only — an earlier-cited "Coppola et al. 2021" DOI was hallucinated and has been removed (see citation_verification_report.md). The Coppola et al. 2021 *J. Geophys. Res. Atmos.* paper at DOI `10.1029/2019JD032356` exists but is about **EURO-CORDEX (Europe), not global CORDEX-CORE** — wrong fit.

---

## Reanalyses — historical reference

### ERA5 / ERA5-Land

- **Producer**: ECMWF (European Centre for Medium-Range Weather Forecasts) / Copernicus C3S
- **Type**: Atmospheric reanalysis
- **Native resolution**: ERA5: 0.25° (atmosphere); ERA5-Land: 0.1° (land-surface variables only)
- **Temporal coverage**: 1940-present, hourly (some variables 6-hourly)
- **What it's best for**: Historical baseline; observational reference for model evaluation; gap-filling where in-situ observations are sparse (most of Africa). The single most-used reanalysis for African work.
- **Limitations**: Reanalysis IS a model output (just one anchored to observations); known biases over data-sparse regions; precipitation over Africa especially uncertain pre-2000
- **Source**: [Copernicus CDS — ERA5](https://cds.climate.copernicus.eu/datasets) (search "ERA5")
- **Citation**: Hersbach et al. 2020 (DOI [10.1002/qj.3803](https://doi.org/10.1002/qj.3803))

### MERRA-2

- **Producer**: NASA GMAO
- **Type**: Atmospheric reanalysis
- **Native resolution**: ~0.5° × 0.625°
- **Temporal coverage**: 1980-present, hourly
- **What it's best for**: Alternative to ERA5; useful as a cross-check; specific advantage for aerosol-related variables
- **Source**: [NASA GMAO MERRA-2](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/)
- **Citation**: Gelaro et al. 2017 (DOI [10.1175/JCLI-D-16-0758.1](https://doi.org/10.1175/JCLI-D-16-0758.1))

### JRA-55 / JRA-3Q

- **Producer**: Japan Meteorological Agency
- **Type**: Atmospheric reanalysis
- **Native resolution**: ~55 km (~0.5°)
- **Temporal coverage**: JRA-55: 1958-present; JRA-3Q (newer): 1947-present
- **What it's best for**: Long historical baseline (longer than ERA5); cross-check vs ERA5 / MERRA-2
- **Source**: [JMA reanalysis project](https://jra.kishou.go.jp/JRA-55/)
- **Citation**: Kobayashi et al. 2015 (DOI [10.2151/jmsj.2015-001](https://doi.org/10.2151/jmsj.2015-001))

---

## Observational gridded datasets — historical reference

### CHIRPS / CHIRPS v3

- **Producer**: UCSB Climate Hazards Center
- **Type**: Satellite + gauge blended rainfall observation
- **Native resolution**: 0.05° (~5 km)
- **Temporal coverage**: 1981-present, daily / pentad / monthly
- **What it's best for**: The primary precipitation observational reference for Africa. Cited in nearly every regional CMIP evaluation paper. **The Adaptation Atlas's "Recent Changes" view uses CHIRPS.**
- **Limitations**: Bias over very wet regions (mountainous + tropical); gauge density variable across Africa
- **Source**: [CHIRPS at UCSB CHC](https://www.chc.ucsb.edu/data/chirps)
- **Citation**: Funk et al. 2015 (DOI [10.1038/sdata.2015.66](https://doi.org/10.1038/sdata.2015.66))

### CHIRTS / CHIRTS-ERA5

- **Producer**: UCSB Climate Hazards Center
- **Type**: Satellite + gauge blended temperature (CHIRTS) or ERA5-blended variant (CHIRTS-ERA5)
- **Native resolution**: 0.05°
- **Temporal coverage**: 1983-present (CHIRTS); CHIRTS-ERA5 extends with ERA5 backbone
- **What it's best for**: Temperature observational baseline for Africa. **Used by the Atlas's "Recent Changes" temperature view.**
- **Source**: [CHIRTS at UCSB CHC](https://www.chc.ucsb.edu/data/chirtsdaily)
- **Citation**: Funk et al. 2019 (DOI [10.1175/JCLI-D-18-0698.1](https://doi.org/10.1175/JCLI-D-18-0698.1))

### GMFD — Global Meteorological Forcing Dataset

- **Producer**: Princeton University / Sheffield et al.
- **Type**: Blended observational forcing
- **Native resolution**: 0.25°
- **Temporal coverage**: 1948-2010
- **What it's best for**: The reference dataset NEX-GDDP-CMIP6 was bias-corrected against. Foundational for understanding what NEX-GDDP considers "ground truth."
- **Limitations**: Coverage ends ~2010; later years require alternative observations
- **Source**: [Princeton terrestrial hydrology research](https://hydrology.princeton.edu/data.php)
- **Citation**: Sheffield, Goteti & Wood 2006 (DOI [10.1175/JCLI3790.1](https://doi.org/10.1175/JCLI3790.1))

### W5E5

- **Producer**: ISIMIP (Cucchi et al.)
- **Type**: Bias-adjusted ERA5 forcing for ISIMIP3
- **Native resolution**: 0.5°
- **Temporal coverage**: 1979-2019
- **What it's best for**: The reference dataset ISIMIP3 was bias-adjusted against (cf GMFD for NEX-GDDP). Useful when comparing across the two downscaled families.
- **Source**: [ISIMIP repository](https://data.isimip.org/)
- **Citation**: Cucchi et al. 2020 (DOI [10.5194/essd-12-2097-2020](https://doi.org/10.5194/essd-12-2097-2020))

---

## Aggregated / impact-sector products

### ISIMIP3b impact-sector outputs

- **Producer**: ISIMIP impact modelling groups + PIK coordination
- **Type**: Impact-model outputs driven by ISIMIP3b climate forcing
- **Sectors covered**: Crops, water, fisheries, biodiversity, health, energy, etc.
- **What it's best for**: Studies that need consistent climate-impact projections across sectors with a coordinated methodology
- **Source**: [ISIMIP repository](https://data.isimip.org/)

### AR6 Interactive Atlas data

- **Producer**: IPCC AR6 WGI Atlas working group
- **Type**: Pre-processed CMIP6 + CORDEX projections at 1° / 2° resolution, organised by AR6 reference regions
- **Native resolution**: 1° (CMIP6), 2° (CMIP5)
- **What it's best for**: Quick access to regional summary statistics in the same format as the AR6 report. Authoritative for any "AR6 says X" framing.
- **Source**: [AR6 Interactive Atlas](https://interactive-atlas.ipcc.ch/)
- **Citation**: Gutiérrez et al. 2021 (AR6 WGI Atlas chapter)

### World Bank Climate Knowledge Portal (CCKP) datasets

- **Producer**: World Bank Group
- **Type**: Aggregated CMIP6 + CMIP5 data at country/admin1 level
- **Native resolution**: ~50 km
- **What it's best for**: Quick access for partners who don't want to handle netCDF; aligns with World Bank operational programmes; familiar interface for international-finance partners
- **Source**: [CCKP](https://climateknowledgeportal.worldbank.org/)
- **Note for the wiki**: CCKP is the most-used non-Atlas climate data tool for the Atlas's target audience. Worth explicit comparison.

---

## What the wiki page should distil from this

The dataset-landscape page (#7) renders the inventory above as a single comparison table with columns: Name | Type | Resolution | Coverage | Bias-corrected | Africa-friendly | What it's best for. Then per-row write-ups underneath for the ~8 most-likely-relevant datasets (NEX-GDDP, ISIMIP3b, CHELSA, CORDEX-Africa, ERA5, CHIRPS, AR6 Interactive Atlas, CCKP). The remaining datasets get a one-line mention "for completeness."

**Key narrative**: NEX-GDDP-CMIP6 is the Atlas default for good reasons (resolution + ensemble size + variable suite), but it's not the only option, and for specific use cases (very-high-resolution biology = CHELSA; impact-sector modelling = ISIMIP3b; physical-consistency for extremes = CORDEX) the right choice differs.

**Outstanding work**:

- For each dataset that an Atlas partner is likely to bump into via a partner institution (CCKP, CHELSA, ISIMIP), confirm any major recent methodology change.
- Get the v3 of CORDEX-CMIP6 specs into the wiki when CORDEX publishes it.
- Add the CIL-GDPCIR methods paper citation when it publishes.
