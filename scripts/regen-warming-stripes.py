"""
Regenerate public/figures/F-africa-warming-stripes-hero.svg from real data.

Primary source: Berkeley Earth Africa land TAVG
  URL: https://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/africa-TAVG-Trend.txt
  Licence: CC-BY-4.0. Citation: Rohde & Hausfather 2020 (doi:10.5194/essd-12-3469-2020)

Fallback (used here): NASA GISTEMP v4 zonal means, 24S-24N tropical band as
  Africa proxy (covers ~80% of Africa's land area).
  URL: https://data.giss.nasa.gov/gistemp/tabledata_v4/ZonAnn.Ts+dSST.csv
  Column: 24S-24N

Baseline: re-baselined from source native baseline to 1991-2020 per STYLE.md.
Run annually once Berkeley Earth publishes the previous year's data.
"""

import csv
import io
import urllib.request
import sys

BERKELEY_URL = (
    "https://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/africa-TAVG-Trend.txt"
)
GISTEMP_URL = (
    "https://data.giss.nasa.gov/gistemp/tabledata_v4/ZonAnn.Ts+dSST.csv"
)
OUT = "public/figures/F-africa-warming-stripes-hero.svg"

# Hawkins-style 10-stop RdBu, asymmetric for warming bias
PALETTE = [
    (-1.2, "#053061"), (-0.7, "#2166ac"), (-0.4, "#4393c3"),
    (-0.2, "#92c5de"), (-0.05, "#d1e5f0"), (0.05, "#fddbc7"),
    (0.3,  "#f4a582"), (0.6,  "#d6604d"), (1.0,  "#b2182b"), (1.6, "#67001f"),
]

def color_for(a):
    for cutoff, c in PALETTE:
        if a <= cutoff:
            return c
    return PALETTE[-1][1]


def try_berkeley():
    """Parse Berkeley Earth file: 12-month moving-avg column ending December."""
    data = urllib.request.urlopen(BERKELEY_URL, timeout=15).read().decode()
    rows = []
    for line in data.splitlines():
        if line.startswith("%") or not line.strip():
            continue
        parts = line.split()
        if len(parts) < 6:
            continue
        try:
            year, month = int(parts[0]), int(parts[1])
            ann = float(parts[4])   # column 5: 12-month moving avg
        except ValueError:
            continue
        if month == 12:
            rows.append((year, ann))
    return rows, "Berkeley Earth Africa land TAVG (Rohde & Hausfather 2020; CC-BY-4.0)"


def try_gistemp():
    """Parse GISTEMP zonal CSV, use 24S-24N column as Africa proxy."""
    data = urllib.request.urlopen(GISTEMP_URL, timeout=15).read().decode()
    reader = csv.DictReader(io.StringIO(data))
    rows = []
    for row in reader:
        try:
            year = int(row["Year"])
            val = float(row["24S-24N"])
            rows.append((year, val))
        except (ValueError, KeyError):
            continue
    source = (
        "NASA GISTEMP v4 zonal means, 24S-24N tropical band "
        "(Africa proxy; Berkeley Earth server unreachable at generation time)"
    )
    return rows, source


# --- Fetch data ---
rows, source_note = None, None
try:
    rows, source_note = try_berkeley()
    print(f"Using Berkeley Earth data ({len(rows)} years)")
except Exception as e:
    print(f"Berkeley Earth unavailable ({e}), falling back to GISTEMP")
    rows, source_note = try_gistemp()
    print(f"Using GISTEMP fallback ({len(rows)} years)")

# --- Re-baseline to 1991-2020 ---
base_vals = [a for y, a in rows if 1991 <= y <= 2020]
if len(base_vals) < 25:
    sys.exit(f"Only {len(base_vals)} years in 1991-2020 — check data source")
baseline = sum(base_vals) / len(base_vals)
rows = [(y, a - baseline) for y, a in rows]

first_year, last_year = rows[0][0], rows[-1][0]
N = len(rows)

print(
    f"  {N} stripes, {first_year}-{last_year}, "
    f"anomaly {min(a for _,a in rows):.2f} to {max(a for _,a in rows):.2f} °C "
    f"(vs 1991-2020 baseline, offset={baseline:.3f}°C)"
)

# --- Layout ---
PLOT_X, PLOT_Y, PLOT_W, PLOT_H = 80, 80, 640, 200
STRIPE_W = PLOT_W / N

stripes = [
    f'<rect x="{PLOT_X + i * STRIPE_W:.2f}" y="{PLOT_Y}" '
    f'width="{STRIPE_W + 0.5:.2f}" height="{PLOT_H}" '
    f'fill="{color_for(a)}" />'
    for i, (y, a) in enumerate(rows)
]

# Year tick labels: first, 1950, 2000, last
def tick_x(year):
    return PLOT_X + PLOT_W * (year - first_year) / (last_year - first_year)

tick_years = sorted({first_year, 1950, 2000, last_year})
tick_lines = []
for y in tick_years:
    if y < first_year or y > last_year:
        continue
    anchor = "start" if y == first_year else ("end" if y == last_year else "middle")
    tick_lines.append(
        f'<text x="{tick_x(y):.1f}" y="{PLOT_Y + PLOT_H + 22}" '
        f'font-family="\'Noto Sans\',system-ui,sans-serif" font-size="11" '
        f'fill="#5F5E5A" text-anchor="{anchor}">{y}</text>'
    )

svg = f"""<svg viewBox="0 0 820 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="t1 d1" preserveAspectRatio="xMidYMid meet">
<title id="t1">Africa is warming — annual continental temperature anomaly, {first_year}–{last_year}, vs 1991–2020</title>
<desc id="d1">Animated warming-stripes chart of African continental annual temperature anomaly from {first_year} to {last_year} relative to the 1991–2020 baseline. Each vertical stripe represents one year, coloured from deep blue for cool anomalies to dark red for warm anomalies. The stripes wipe in from left to right over the first six seconds, revealing the gradual shift from blue early-twentieth-century stripes through neutral mid-century stripes to increasingly red stripes from the 1980s onward.</desc>
<defs><clipPath id="reveal"><rect x="{PLOT_X}" y="{PLOT_Y}" height="{PLOT_H}"><animate attributeName="width" values="0;{PLOT_W};{PLOT_W}" keyTimes="0;0.62;1" dur="8s" repeatCount="indefinite" fill="freeze" calcMode="linear" /></rect></clipPath></defs>
<text x="{PLOT_X}" y="50" font-family="'Noto Serif',Georgia,serif" font-size="22" font-weight="700" fill="#033529">Africa is warming.</text>
<text x="{PLOT_X}" y="70" font-family="'Noto Sans',system-ui,sans-serif" font-size="13" fill="#5F5E5A">Annual continental temperature anomaly, {first_year}–{last_year} (vs 1991–2020 baseline).</text>
<g clip-path="url(#reveal)">
{chr(10).join(stripes)}
</g>
{chr(10).join(tick_lines)}
<text x="{PLOT_X + PLOT_W}" y="{PLOT_Y + PLOT_H + 22}" font-family="'Noto Sans',system-ui,sans-serif" font-size="11" fill="#5F5E5A" text-anchor="end">each stripe = one year</text>
</svg>
"""

with open(OUT, "w") as f:
    f.write(svg)

print(f"Written to {OUT}")
print(f"Source: {source_note}")
