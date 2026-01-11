# Smartphone Market Insights

Exploratory data analysis on smartphones scraped from Smartprix, with insights on pricing and specifications.

Analysis of scraped smartphone specifications to understand brand presence, pricing, and feature trends. Pipeline: scrape → clean → EDA → export visuals.

## Contents
- Scraping: [workspace/advWebScrapping/scrappingSmartPrix.py](workspace/advWebScrapping/scrappingSmartPrix.py)
- Cleaning notebook: [workspace/data-cleaning/clean.ipynb](workspace/data-cleaning/clean.ipynb)
- EDA notebook: [workspace/EDA/eda-smart-phone.ipynb](workspace/EDA/eda-smart-phone.ipynb)
- Sample cleaned dataset: [smartphone_cleaned_v2.csv](smartphone_cleaned_v2.csv)

## Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## How to Reproduce
1. Scrape (local HTML): ensure `smartprix.html` is present, then run `python workspace/advWebScrapping/scrappingSmartPrix.py` → outputs `smartprix_mobiles_with_specs.csv`.
2. Clean: open [workspace/data-cleaning/clean.ipynb](workspace/data-cleaning/clean.ipynb) and run all cells to tidy columns (RAM/ROM split, display parsing, camera separation, outlier fixes). Save the cleaned file as `smartphone_cleaned_v2.csv` in the repo root.
3. EDA: run [workspace/EDA/eda-smart-phone.ipynb](workspace/EDA/eda-smart-phone.ipynb) against the cleaned dataset. For each plot, call `plt.savefig('images/<name>.png', dpi=200, bbox_inches='tight')` before `plt.show()` to capture artifacts.

## What to Commit
- Data: `smartprix_mobiles_with_specs.csv` (scraped) and `smartphone_cleaned_v2.csv` (cleaned).
- Notebooks: cleaning and EDA notebooks above.
- Scripts: scraping script.
- Visuals: PNGs exported into `images/` (create the folder). Include key charts: top brands bar, price distribution, feature mix pies (5G, NFC, IR), heatmap of numeric correlations.

## Insights (from current EDA)
- Price is right-skewed; ultra-premium outliers were removed above ₹200k for clearer trends.
- Ratings are roughly normal with missing values handled; median ratings cluster high.
- Brand landscape: a handful of brands dominate model counts; median price varies sharply by brand.
- Feature mix: majority of models advertise 5G; NFC and IR blaster are less common; most devices cluster around mid RAM/internal storage tiers.
- Performance: more cores and higher refresh rates show positive association with price; processor_brand matters for pricing tiers.

## Publishing Checklist
- Verify images exist in `images/` and are referenced in the README if desired.
- Ensure absolute paths in notebooks/scripts are adjusted if running outside `/Users/karangautam/Desktop/Data` (or define a `BASE_DIR`).
- Remove extraneous intermediate files; keep datasets and outputs small enough for GitHub limits.
- Add a short repo description on GitHub: "Scraped smartphone specs, cleaned dataset, and EDA-driven insights."
