# Retail Complaint Resolution ML

## Project Title

**Using Machine Learning to Predict Complaint Resolution Outcomes in Retail Banking: Evidence from Open Consumer Financial Complaint Data**

## Project Purpose

This project uses open data from the CFPB Consumer Complaint Database to analyze and predict complaint-resolution outcomes in retail banking. The study focuses on response timeliness, company response outcomes, complaint product type, issue categories, submission channel, company, geography, and consumer complaint narratives.

The project combines exploratory data analysis, hypothesis testing, and machine learning to understand which complaint characteristics are associated with resolution outcomes and whether narrative text improves predictive performance beyond structured fields alone.

## Main Research Questions

1. Does complaint product type significantly influence timely company response?
2. Do complaint issue categories significantly predict company response outcome?
3. Do complaint narratives improve prediction performance compared with structured fields only?
4. Are company-level and geographic differences significantly associated with complaint resolution outcomes after controlling for product and issue?

## Data Source

Primary data source: **CFPB Consumer Complaint Database**

- Official website: https://www.consumerfinance.gov/data-research/consumer-complaints/
- API field reference: https://cfpb.github.io/api/ccdb/fields.html

The dataset includes public complaint records submitted to the Consumer Financial Protection Bureau. The project uses the current public file structure, including fields such as date received, product, issue, consumer complaint narrative, company, state, submitted via, company response to consumer, timely response, and complaint ID.

## Scope of Analysis

The project focuses on complaint records related to retail banking service delivery.

### Include

- Checking or savings account complaints
- Credit card or prepaid card complaints
- Mortgage complaints
- Vehicle loan or lease complaints
- Personal loan complaints
- Money transfer complaints
- Other consumer banking products directly linked to retail banking service delivery

### Include with Caution

- Debt collection complaints only when clearly linked to a consumer retail banking product

### Exclude

- Complaints unrelated to retail banking
- Records with unclear product linkage if they cannot be reasonably classified

## Folder Structure

```text
retail-complaint-resolution-ml/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   ├── processed/
│   └── data_dictionary.csv
├── notebooks/
│   ├── 01_data_extraction.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_hypothesis_tests.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_model_interpretation.ipynb
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── models/
├── docs/
└── reports/
```

## Notebook Workflow

### 1. `01_data_extraction.ipynb`

Loads the large CFPB complaint CSV file in chunks, selects required columns, applies date and product filters, creates derived fields, and saves the processed dataset.

Main outputs:

- processed complaint dataset
- sample dataset
- raw column list
- extraction metadata
- basic count tables

### 2. `02_exploratory_analysis.ipynb`

Explores the processed dataset and creates descriptive summaries.

Main analyses:

- dataset overview
- missing-value review
- product, issue, company, state, and channel distributions
- timely response distribution
- company response distribution
- narrative availability
- yearly and monthly complaint trends
- product-level timely response rates

### 3. `03_hypothesis_tests.ipynb`

Performs formal statistical tests for the research questions.

Main analyses:

- chi-square test for product type and timely response
- chi-square test for issue category and company response outcome
- preliminary structured vs narrative model comparison
- company and state association tests
- final hypothesis summary table

### 4. `04_model_training.ipynb`

Builds and compares predictive machine learning models.

Main models:

- dummy baseline model
- structured logistic regression
- structured plus TF-IDF narrative logistic regression
- structured random forest
- optional company response outcome model

Class imbalance is addressed using stratified train-test splitting, class-weighted models, and evaluation metrics beyond accuracy.

### 5. `05_model_interpretation.ipynb`

Interprets the trained models and converts technical findings into business recommendations.

Main outputs:

- best model evaluation
- threshold analysis
- error analysis
- subgroup performance review
- feature interpretation
- business findings and recommendations
- implementation roadmap
- limitations table
- final capstone summary

## Methodology Summary

The project uses a structured analytics workflow:

1. Data extraction and filtering
2. Exploratory data analysis
3. Statistical hypothesis testing
4. Machine learning model training
5. Model interpretation and business recommendation

The primary prediction target is `timely_response_binary`, derived from the CFPB field `Timely response?`.

```text
1 = Timely response
0 = Not timely response
```

A secondary outcome, `company_response_to_consumer`, is used for response outcome analysis.

## Class Imbalance Strategy

Complaint resolution outcomes may be imbalanced. The project addresses this by:

- reporting target class distribution during EDA;
- using stratified train-test splits;
- applying `class_weight="balanced"` in logistic regression and random forest models;
- evaluating models with balanced accuracy, precision, recall, F1-score, ROC-AUC, and average precision;
- using threshold analysis to examine precision-recall trade-offs.

SMOTE and synthetic oversampling are not used in the main pipeline to avoid creating artificial complaint records.

## Data Leakage Controls

The project avoids using fields that may only be known after the company responds when predicting timely response.

Fields treated carefully include:

- `company_response_to_consumer`
- `company_public_response`
- `date_sent_to_company`
- `received_to_sent_lag_days`

These variables may be useful for descriptive or process analysis, but they should not be used as intake-stage predictors unless their timing is clearly justified.

## Key Outputs

The project generates reusable outputs under the `outputs/` folder.

```text
outputs/
├── figures/   # charts and visualizations
├── tables/    # summary tables, test results, model metrics
└── models/    # saved trained models
```

Examples of important outputs:

- `eda_dataset_overview.csv`
- `final_hypothesis_tests_summary.csv`
- `model_training_performance_comparison.csv`
- `model_training_best_model_summary.csv`
- `final_business_findings_and_recommendations.csv`
- `final_capstone_summary.csv`

## Requirements

The project uses Python and common data science libraries.

Core libraries include:

- pandas
- numpy
- matplotlib
- scipy
- statsmodels
- scikit-learn
- joblib

Install dependencies using:

```bash
pip install -r requirements.txt
```

## How to Run

Run the notebooks in order:

```text
01_data_extraction.ipynb
02_exploratory_analysis.ipynb
03_hypothesis_tests.ipynb
04_model_training.ipynb
05_model_interpretation.ipynb
```

The first notebook expects the raw CFPB CSV file to be placed in:

```text
data/raw/complaints.csv
```

In Google Colab, the expected project path is:

```text
/content/drive/MyDrive/retail-complaint-resolution-ml
```

## Data Storage Note

The raw CFPB complaint file is large and should not be committed to GitHub. The `.gitignore` file should exclude large raw and processed data files, model files, and temporary notebook checkpoints.

Recommended exclusions include:

```text
data/raw/
data/processed/
outputs/models/
.ipynb_checkpoints/
```

Small sample files, metadata, charts, and summary tables may be included if appropriate for review.

## Limitations

This project uses public complaint data and should be interpreted carefully.

Key limitations:

- CFPB complaints do not represent the full customer population.
- Complaint volume does not equal market share or company performance.
- Observational data supports association and prediction, not causal claims.
- Narrative availability depends on consumer consent.
- Company and geographic differences may reflect product mix, customer base, regulation, or reporting behavior.
- Model outputs should support human decision-making, not replace it.

## Business Value

The project can support:

- complaint triage;
- early warning dashboards;
- product-level complaint monitoring;
- issue-level operational review;
- response timeliness analysis;
- governance and risk reporting;
- responsible use of machine learning in complaint management.

## Author

Zahoor ul Islam
Prepared as part of a DBA data analytics capstone project.
