# Smartphone Market Insights

**Exploratory data analysis on smartphones scraped from Smartprix, focusing on pricing, brand presence, and technical specifications.**

This project implements an end-to-end data pipeline: **Scrape → Clean → EDA → Export Visuals**. It analyzes smartphone specifications to identify trends in the current market landscape, cleaning raw web data into a structured dataset for analysis.

## Technical Approach
* **Dynamic Data Extraction:** The scraping strategy addresses the dynamic nature of modern web pages (infinite scrolling/AJAX), ensuring the retrieval of the complete dataset rather than just the initial viewport.
* **Robust Parsing:** Utilizes `BeautifulSoup` to navigate complex nested DOM structures and extract attributes hidden within dynamic containers.
* **Data Cleaning Pipeline:** Systematically handles dirty data, including splitting compound strings (e.g., "8GB RAM + 128GB Storage"), normalizing prices, and imputing missing specification values.

## Repository Structure
- Scraping Script: [workspace/advWebScrapping/scrappingSmartPrix.py](workspace/advWebScrapping/scrappingSmartPrix.py)
- Raw Scrapped Data : [smartprix_mobiles_with_specs.csv](smartprix_mobiles_with_specs.csv)
- Cleaning notebook: [workspace/data-cleaning/clean.ipynb](workspace/data-cleaning/clean.ipynb)
- EDA notebook: [workspace/EDA/eda-smart-phone.ipynb](workspace/EDA/eda-smart-phone.ipynb)
- Cleaned dataset: [smartphone_cleaned_v2.csv](smartphone_cleaned_v2.csv)


## Key Insights
- Price is right-skewed; ultra-premium outliers were removed above ₹200k for clearer trends.
- Ratings are roughly normal with missing values handled; median ratings cluster high.
- Brand landscape: a handful of brands dominate model counts; median price varies sharply by brand.
- Feature mix: majority of models advertise 5G; NFC and IR blaster are less common; most devices cluster around mid RAM/internal storage tiers.
- Performance: more cores and higher refresh rates show positive association with price; processor_brand matters for pricing tiers.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
## How to Run

1. Scrape Data

  -  Visit Smartprix and save the mobile category page as smartprix.html in the root directory (ensure all dynamic content is loaded).

  -  Run the scraping script:

```bash

  python workspace/advWebScrapping/scrappingSmartPrix.py
  Output: smartprix_mobiles_with_specs.csv
  ```

2.  Clean Data

  -  Open ```workspace/data-cleaning/clean.ipynb``` and run all cells.

  -  This processes the raw data (handling RAM/ROM splits, camera parsing, and outlier removal) and saves the clean file.

  -  Output: ```smartphone_cleaned_v2.csv```

3.  Exploratory Data Analysis (EDA)

  -  Open ```workspace/EDA/eda-smart-phone.ipynb``` and run all cells.

  -  This generates insights and visualization charts.



## Future Improvements
* **Price Prediction Model:** Build a regression model (e.g., Random Forest or XGBoost) to predict smartphone prices based on specifications like RAM, processor, and camera.
* **Interactive Dashboard:** Specificly Develop a Streamlit dashboard to allow users to filter smartphones and visualize trends dynamically.
* **Sentiment Analysis:** Expand scraping to include user reviews and perform sentiment analysis to correlate specs with user satisfaction.

