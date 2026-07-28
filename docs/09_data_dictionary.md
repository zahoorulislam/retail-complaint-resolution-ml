# Data Dictionary

This document defines the key processed variables used in the project.

| Variable Name | Definition | Type | Notes |
|---|---|---|---|
| `date_received` | Date the complaint was received. | Date | Used for time-period filtering and year/month/quarter features. |
| `date_received_raw` | Original raw date received value. | String | Retained for traceability. |
| `product` | Main financial product category. | Categorical | Supports RQ1 and model training. |
| `sub_product` | More detailed product category. | Categorical | Used in EDA and modeling. |
| `issue` | Main complaint issue. | Categorical | Supports RQ2 and model training. |
| `sub_issue` | More detailed complaint issue. | Categorical | Used in modeling and interpretation. |
| `consumer_complaint_narrative` | Customer-written complaint text. | Text | Used for narrative availability, length, and TF-IDF modeling where available. |
| `company_public_response` | Company's public response text/category. | Categorical/Text | Excluded from intake-stage timeliness prediction to prevent leakage. |
| `company` | Company named in complaint. | Categorical | Used to create grouped company features. |
| `company_grouped` | Grouped company variable. | Categorical | Used in RQ4 and model training. |
| `state` | U.S. state associated with complaint. | Categorical | Used in geography analysis. |
| `state_grouped` | Grouped state variable. | Categorical | Used in RQ4 and model training. |
| `zip_code` | ZIP code field from CFPB data. | String | Retained for reference; not central to final modeling. |
| `tags` | Consumer tags such as Older American or Servicemember. | Categorical | Used for subgroup and fairness-related review. |
| `submitted_via` | Complaint submission channel. | Categorical | Used in modeling and subgroup analysis. |
| `date_sent_to_company` | Date complaint was sent to company. | Date | Used to calculate lag; handled carefully to avoid leakage depending on prediction stage. |
| `date_sent_to_company_raw` | Original raw date sent to company value. | String | Retained for traceability. |
| `company_response_to_consumer` | Company response outcome. | Categorical | Used for secondary response outcome analysis; excluded from timeliness prediction. |
| `company_response_group` | Grouped company response outcome. | Categorical | Used for response outcome modeling. |
| `timely_response` | Original timely response field. | Categorical | Source field for the primary target. |
| `timely_response_binary` | Binary target for timely response. | Integer | `1 = timely`, `0 = non-timely`. |
| `complaint_id` | Unique complaint identifier. | String/Integer | Used for duplicate checks and traceability. |
| `year_received` | Year extracted from `date_received`. | Integer/Categorical | Used in EDA and modeling. |
| `month_received` | Month extracted from `date_received`. | String | Used for trend analysis. |
| `quarter_received` | Quarter extracted from `date_received`. | String | Used for trend analysis. |
| `has_narrative` | Indicator for whether complaint narrative exists. | Integer | `1 = narrative available`, `0 = narrative missing`. |
| `narrative_length` | Character length of complaint narrative. | Numeric | Used as a proxy for narrative detail or complaint complexity. |
| `received_to_sent_lag_days` | Days between receipt and date sent to company. | Numeric | Used for operational description; use carefully depending on prediction timing. |

## Target Variable

Primary modeling target:

```text
timely_response_binary
```

Coding:

```text
1 = Timely response
0 = Non-timely response
```

## Leakage-Control Note

The following variables are excluded from intake-stage response-timeliness prediction because they may contain post-response information:

```text
company_response_to_consumer
company_public_response
```

Other variables should be reviewed depending on the intended prediction timing.
