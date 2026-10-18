# Retail Customer Segmentation

Customer segmentation for an online retailer using **RFM analysis** (Recency, Frequency, Monetary) and **K-Means clustering**, with a **Streamlit dashboard** for exploring the resulting segments.

## What it does

1. **Cleans** the transaction data: drops rows without a customer ID and rows with non-positive quantity or price, then computes the value of each order line.
2. **Builds RFM features** per customer:
   - *Recency*: days since the customer's last purchase (reference date = last transaction date + 1 day)
   - *Frequency*: number of unique orders
   - *Monetary*: total spend
3. **Clusters customers** with K-Means on standardized RFM features (`StandardScaler`). The Elbow Method (k = 2 to 8) was reviewed and **k = 4** was selected; the silhouette score for k = 4 is **0.59**.
4. **Visualizes** the clusters with a 2-D PCA projection, an RFM correlation heatmap, cluster-average heatmaps, and box plots for frequency and spend.
5. **Defines business segments** with RFM quartile rules, and flags loyal customers (top-quartile recency, frequency and spend).
6. **Analyzes** the best-selling products among VIP customers and the distribution of transactions by country (Plotly map).
7. **Exports** `rfm_output.csv` and `vip_customers.csv`, and serves the segments in a Streamlit dashboard.

## Results (from the notebook)

**K-Means clusters (k = 4, 5,878 customers)**

| Cluster | Customers | Avg. recency (days) | Avg. frequency (orders) | Avg. spend |
|---|---|---|---|---|
| 0 | 1,998 | 463 | 2.2 | 765 |
| 1 | 3,841 | 67 | 7.3 | 3,009 |
| 2 | 35 | 26 | 103.7 | 83,086 |
| 3 | 4 | 3.5 | 212.5 | 436,836 |

**Rule-based business segments**

| Segment | Customers | Rule |
|---|---|---|
| VIP Loyal | 674 | Recency in the best quartile, frequency and spend in the top quartile |
| At Risk | 847 | Recency in the worst quartile and frequency in the bottom quartile |
| Regular | 2,637 | Frequency at or above the median (remaining customers) |
| Occasional | 1,720 | All other customers |

## Dashboard

`app.py` is a Streamlit app that reads `rfm_output.csv`. Choose a segment to see its number of customers, a table of the first 20 customers, and a histogram of their spend.

## Tech stack and skills used

- **Python**, **Jupyter Notebook**
- **Pandas**, **NumPy**: data cleaning, aggregation, RFM feature engineering
- **scikit-learn**: `StandardScaler`, `KMeans`, `PCA`, `silhouette_score`
- **Matplotlib**, **Seaborn**, **Plotly**: histograms, heatmaps, box plots, scatter plots, choropleth map
- **Streamlit**: interactive dashboard
- **Git / GitHub**

## Project structure

```
.
├── rfm_analysis.ipynb   # cleaning, RFM, clustering, segmentation, charts, CSV export
├── app.py               # Streamlit dashboard
└── .gitignore           # excludes retail.csv, rfm_output.csv, vip_customers.csv
```

## Getting started

```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn streamlit jupyter
```

1. Place the transaction file `retail.csv` in the project folder. It is not included in the repository. Expected columns: `Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID, Country`.
2. Run all cells in `rfm_analysis.ipynb`. This creates `rfm_output.csv` and `vip_customers.csv`.
3. Start the dashboard:
```bash
   streamlit run app.py
```

## Notes

- Two of the four clusters contain only 35 and 4 customers, because a few very high-spend customers pull away from the rest. A log transform of the RFM values or outlier handling would give more balanced clusters.
- The silhouette score was calculated for the final k = 4 model only; k was chosen from the Elbow plot.
- Segment rules use quartiles of this dataset, so thresholds change with new data.

## Author

**Anitha Reddy Bapathu** · M.S. Computer Science, University at Albany, SUNY
