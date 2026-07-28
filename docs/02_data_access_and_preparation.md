# Data Access and Preparation

## Raw Data Source

The raw dataset is the public **Consumer Complaint Database** from the Consumer Financial Protection Bureau (CFPB).

Raw data can be downloaded from:

https://www.consumerfinance.gov/data-research/consumer-complaints/#get-the-data

## Download Instructions

1. Open the CFPB Consumer Complaint Database page.
2. Scroll to **Get the data**.
3. Download the complaint database in CSV format.
4. Rename the file to:

```text
complaints.csv
```

5. Place the file in:

```text
retail-complaint-resolution-ml/data/raw/complaints.csv
```

For Google Colab, the expected path is:

```text
/content/drive/MyDrive/retail-complaint-resolution-ml/data/raw/complaints.csv
```

## Why the Raw Data Is Not Stored in GitHub

The CFPB raw complaint file is large. To keep the repository lightweight and avoid upload limits, the raw CSV should be downloaded directly from CFPB by each user. The repository contains the notebooks and documentation needed to reproduce the processed dataset.

## Notebook 01: Data Extraction and Basic Review

Notebook used:

```text
01_data_extraction_colab_csv_v2.ipynb
```

Notebook 01 performs the following work:

- Sets up project folders.
- Checks that the raw `complaints.csv` file exists.
- Reads the large CSV file in chunks.
- Selects required columns from the current CFPB file version.
- Filters records to the 2017–2025 study period.
- Filters records to retail banking-related products.
- Cleans column names into Python-friendly format.
- Creates derived date and narrative features.
- Saves the processed dataset for later notebooks.
- Creates a 1,000-row sample file for inspection.
- Saves extraction metadata as JSON.

## Required Raw Columns

The extraction notebook expects the following CFPB columns when available:

| Original CFPB Column | Use in Project |
|---|---|
| Date received | Complaint intake date and time-period features. |
| Product | Main product category used for RQ1 and modeling. |
| Sub-product | More detailed product category used in modeling. |
| Issue | Main issue category used for RQ2 and modeling. |
| Sub-issue | Detailed issue category used in modeling. |
| Consumer complaint narrative | Text field used for narrative availability, length, and TF-IDF modeling. |
| Company public response | Excluded from intake-stage timeliness prediction to prevent leakage. |
| Company | Company grouping and RQ4 analysis. |
| State | Geography and RQ4 analysis. |
| ZIP code | Retained for reference; not central to final model. |
| Tags | Customer tag information, such as Older American or Servicemember. |
| Submitted via | Complaint channel. |
| Date sent to company | Used to calculate lag and describe operations. |
| Company response to consumer | Secondary response outcome analysis; excluded from timeliness prediction. |
| Timely response? | Primary target variable. |
| Complaint ID | Unique complaint identifier. |

## Processed Output

The processed dataset is saved as:

```text
data/processed/cfpb_retail_complaints_2017_2025.csv
```

The sample file is saved as:

```text
data/processed/cfpb_retail_complaints_sample_1000.csv
```

Extraction metadata is saved as:

```text
outputs/tables/data_extraction_metadata.json
```

## Important Data Preparation Notes

- The project uses the 2017–2025 period.
- Date filtering uses a start date of `2017-01-01` and an exclusive end date of `2026-01-01`.
- The primary target is created from `timely_response`:

```text
Yes -> 1
No  -> 0
```

- Narrative features include:

```text
has_narrative
narrative_length
```

- Post-response variables are excluded from intake-stage response-timeliness prediction to reduce data leakage risk.
