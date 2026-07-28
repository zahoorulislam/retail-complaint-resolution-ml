# Retail Complaint Resolution ML

**Project title:** Using Machine Learning to Predict Complaint Resolution Outcomes in Retail Banking: Evidence from Open Consumer Financial Complaint Data

**Author:** Zahoor ul Islam  
**Program:** DBA Data Analytics Capstone  
**Course:** QM640: Data Analytics Capstone  
**Primary dataset:** CFPB Consumer Complaint Database  
**Repository focus:** Data extraction, exploratory analysis, hypothesis testing, machine learning, model interpretation, and business recommendations for complaint-resolution outcomes in retail banking.

---

## 1. Project Overview

This project analyzes public consumer complaint data from the Consumer Financial Protection Bureau (CFPB) to understand and predict complaint-resolution outcomes in retail banking. The study focuses on whether complaint characteristics such as product type, issue category, company group, geography, submission channel, customer narrative, and time period are associated with response timeliness and company response outcomes.

The project is designed as an applied analytics workflow. It starts with a large public complaint file, filters it for relevant retail banking products, performs exploratory data analysis and hypothesis testing, trains machine learning models, interprets model results, and converts the findings into business recommendations.

The main prediction target is **timely response**.

```text
1 = Timely response
0 = Non-timely response
```

A secondary modeling task examines **company response outcome**, including whether complaints are closed with explanation or result in relief.

---

## 2. Business Problem

Retail banking complaint operations need to identify complaints that may require closer attention, faster routing, escalation, or specialist handling. Traditional complaint review is often reactive and rule-based. This project explores whether open complaint data can be used to build an evidence-based early-warning framework for complaint timeliness risk.

The project does **not** attempt to replace human complaint handlers. Instead, it supports a decision-support approach in which machine learning helps complaint teams prioritize review queues, monitor risk segments, and improve operational governance.

---

## 3. Research Questions

The project is organized around four research questions.

| Research Question | Focus |
|---|---|
| RQ1 | Does complaint product type significantly influence timely company response? |
| RQ2 | Do complaint issue categories significantly predict company response outcome? |
| RQ3 | Do complaint narratives improve prediction performance compared with structured fields only? |
| RQ4 | Are company-level and geographic differences significantly associated with complaint resolution outcomes after controlling for product and issue? |

---

## 4. Data Source

The project uses the public CFPB Consumer Complaint Database.

| Source | Link |
|---|---|
| CFPB Consumer Complaint Database | https://www.consumerfinance.gov/data-research/consumer-complaints/ |
| CFPB Get the Data page | https://www.consumerfinance.gov/data-research/consumer-complaints/#get-the-data |
| CFPB API field reference | https://cfpb.github.io/api/ccdb/fields.html |
| Data.gov dataset catalog | https://catalog.data.gov/dataset/consumer-complaint-database |

The raw CFPB complaint file is large and is **not included directly in this repository**. Users should download the raw CSV file from the CFPB website and place it in the expected project folder before running the notebooks.

---

## 5. Raw Data Access Instructions

Download the raw data from:

```text
https://www.consumerfinance.gov/data-research/consumer-complaints/#get-the-data
```

Steps:

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

For Google Colab execution, the expected path is:

```text
/content/drive/MyDrive/retail-complaint-resolution-ml/data/raw/complaints.csv
```

---

## 6. Scope of Analysis

The project focuses on retail banking and consumer financial service complaints.

### Included product areas

- Checking or savings account
- Bank account or service
- Credit card
- Credit card or prepaid card
- Prepaid card
- Mortgage
- Vehicle loan or lease
- Consumer loan
- Payday loan, title loan, personal loan, or advance loan
- Money transfers
- Money transfer, virtual currency, or money service
- Virtual currency, where applicable to financial service complaints

### Excluded or limited areas

- Products unrelated to retail banking service delivery
- Records with unclear or incomplete product linkage
- Post-response fields as intake-stage predictors, to avoid data leakage

---

## 7. Repository Structure

```text
retail-complaint-resolution-ml/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   └── complaints.csv              # Download separately from CFPB
│   ├── processed/
│   └── data_dictionary.csv
├── notebooks/
│   ├── 01_data_extraction_colab_csv_v2.ipynb
│   ├── 02_exploratory_analysis_v2.ipynb
│   ├── 03_hypothesis_tests_v2.ipynb
│   ├── 04_model_training_v2.ipynb
│   └── 05_model_interpretation_v2.ipynb
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── models/
├── docs/
│   ├── README.md
│   ├── 01_project_overview.md
│   ├── 02_data_access_and_preparation.md
│   ├── 03_notebook_execution_guide.md
│   ├── 04_research_questions_and_hypotheses.md
│   ├── 05_eda_and_hypothesis_testing_summary.md
│   ├── 06_model_training_and_evaluation.md
│   ├── 07_model_interpretation_and_business_findings.md
│   ├── 08_governance_limitations_and_roadmap.md
│   ├── 09_data_dictionary.md
│   └── 10_literature_review_sources.md
└── reports/
```

---

## 8. Notebook Workflow

Run the notebooks in order.

| Step | Notebook | Purpose | Main outputs |
|---:|---|---|---|
| 1 | `01_data_extraction_colab_csv_v2.ipynb` | Loads the large CFPB CSV file in chunks, selects required columns, applies date and product filters, creates derived fields, and saves the processed dataset. | Processed dataset, sample dataset, metadata, selected columns |
| 2 | `02_exploratory_analysis_v2.ipynb` | Explores the processed dataset and produces descriptive summaries. | Product, issue, company, state, channel, narrative, and timeliness summaries |
| 3 | `03_hypothesis_tests_v2.ipynb` | Performs formal statistical tests for the research questions. | Chi-square tests, Cramer's V, hypothesis summary tables |
| 4 | `04_model_training_v2.ipynb` | Builds and compares predictive models. | Dummy baseline, logistic regression, TF-IDF logistic regression, random forest, model metrics |
| 5 | `05_model_interpretation_v2.ipynb` | Interprets the trained models and converts technical results into business findings. | Threshold analysis, error analysis, subgroup review, feature importance, business recommendations |

---

## 9. How to Run the Project

### Option A: Google Colab

1. Upload or clone the repository into Google Drive.
2. Download `complaints.csv` from the CFPB website.
3. Place the file in:

```text
/content/drive/MyDrive/retail-complaint-resolution-ml/data/raw/complaints.csv
```

4. Run the notebooks in order from Notebook 01 to Notebook 05.

### Option B: Local Python Environment

Create and activate a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate       # Mac/Linux
.venv\Scripts\activate          # Windows
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Place the raw file in:

```text
data/raw/complaints.csv
```

Then run the notebooks in order.

---

## 10. Requirements

Core Python libraries:

- pandas
- numpy
- matplotlib
- scipy
- statsmodels
- scikit-learn
- joblib
- jupyter

Install using:

```bash
pip install -r requirements.txt
```

---

## 11. Processed Dataset

After filtering for relevant retail banking products and the 2017–2025 study period, the processed dataset contains approximately:

```text
1,289,027 records
25 columns
```

Key derived fields include:

| Field | Description |
|---|---|
| `timely_response_binary` | Binary target variable for timely response |
| `has_narrative` | Indicator showing whether a consumer narrative is available |
| `narrative_length` | Character length of the consumer complaint narrative |
| `year_received` | Year of complaint receipt |
| `month_received` | Month of complaint receipt |
| `quarter_received` | Quarter of complaint receipt |
| `received_to_sent_lag_days` | Days between complaint receipt and date sent to company; used carefully because of timing risk |

---

## 12. Feature Engineering

The project uses structured, time-based, and text-related features.

| Feature group | Examples | Purpose |
|---|---|---|
| Product and sub-product | Product, sub-product | Capture product-level response-risk differences |
| Issue and sub-issue | Issue, sub-issue | Capture complaint type and operational complexity |
| Company and geography | Company group, state group | Capture operational and regional signals |
| Submission channel | Web, phone, referral, mail, fax | Capture intake-channel differences |
| Customer tags | Older American, Servicemember | Support subgroup review and governance |
| Time period | Year received | Capture changes in complaint and response patterns over time |
| Narrative features | Has narrative, narrative length, TF-IDF terms | Capture complaint detail and text-based context |

---

## 13. Data Leakage Controls

The project avoids using fields that may only be known after complaint handling when predicting response timeliness at or near intake.

Fields treated carefully include:

- `company_response_to_consumer`
- `company_public_response`
- `date_sent_to_company`
- `received_to_sent_lag_days`

These fields may be useful for descriptive analysis, process analysis, or outcome explanation, but they should not be used as intake-stage predictors unless their timing is clearly justified.

---

## 14. Class Imbalance Strategy

The timely-response target is highly imbalanced. Most complaints receive timely responses, while non-timely responses are rare.

Approximate target distribution:

| Class | Meaning | Share |
|---|---|---:|
| 1 | Timely response | 98.59% |
| 0 | Non-timely response | 1.41% |

Because of this imbalance, accuracy alone is not a reliable metric. A model can achieve high accuracy by predicting almost every complaint as timely while failing to detect the rare non-timely class.

The project treats class imbalance through:

- reporting class distribution before modeling;
- using stratified train-test splitting;
- applying `class_weight="balanced"` where appropriate;
- evaluating balanced accuracy, ROC-AUC, average precision, precision, recall, F1-score, and confusion matrices;
- reviewing classwise metrics from both timely and non-timely perspectives;
- performing non-timely risk threshold analysis;
- avoiding SMOTE in the main pipeline to prevent creation of synthetic complaint records.

---

## 15. Models Used

| Model | Purpose |
|---|---|
| Dummy baseline | Establishes a majority-class benchmark |
| Structured logistic regression | Provides an interpretable baseline using structured complaint fields |
| Structured + TF-IDF logistic regression | Tests whether narrative text improves prediction beyond structured fields |
| Structured random forest | Captures non-linear patterns and interaction effects across complaint characteristics |
| Company response outcome model | Explores prediction of response outcome categories, including relief provided |

---

## 16. Evaluation Metrics

The project uses multiple metrics because the target is imbalanced.

| Metric | Why it matters |
|---|---|
| Accuracy | General correctness, but misleading under severe imbalance |
| Balanced accuracy | Gives equal weight to timely and non-timely classes |
| Precision | Shows how many predicted positives are correct |
| Recall | Shows how many actual cases are captured |
| F1-score | Balances precision and recall |
| ROC-AUC | Measures ranking ability across thresholds |
| Average precision / PR-AUC | Useful for rare-class risk detection |
| Confusion matrix | Shows false positives, false negatives, true positives, and true negatives |
| Threshold analysis | Helps select an operating point based on business review capacity |

---

## 17. Key Model Results

The final model comparison selected the **Structured Random Forest** as the strongest model by ROC-AUC.

| Model | Accuracy | Balanced accuracy | F1-score | ROC-AUC | Average precision |
|---|---:|---:|---:|---:|---:|
| Dummy baseline | 0.9859 | 0.5000 | 0.9929 | 0.5000 | 0.9859 |
| Structured logistic regression | 0.7333 | 0.7908 | 0.8440 | 0.8506 | 0.9974 |
| Structured + TF-IDF logistic regression | 0.8112 | 0.7384 | 0.8947 | 0.8357 | 0.9970 |
| Structured random forest | 0.7884 | 0.8000 | 0.8802 | 0.8748 | 0.9978 |

From the non-timely risk perspective, the selected random forest model achieved:

| Metric | Value |
|---|---:|
| Non-timely precision | 0.0518 |
| Non-timely recall | 0.8120 |
| Non-timely F1-score | 0.0974 |
| ROC-AUC for non-timely risk | 0.8748 |
| Average precision for non-timely risk | 0.1181 |

The model is strong at catching many non-timely complaints, but precision is low because non-timely cases are rare. Therefore, the model should be used for triage and review queues, not automated complaint decisions.

---

## 18. Research Findings Summary

| RQ | Summary finding |
|---|---|
| RQ1 | Product type is statistically associated with timely response. Product should be treated as an operational risk signal, not a complete explanation of delay. |
| RQ2 | Issue category is associated with company response outcome. Issue-level analysis supports routing, specialist assignment, escalation, and root-cause review. |
| RQ3 | Narrative features add useful information and improve some overall metrics, but they do not improve every imbalance-sensitive metric. Text should be used as a supporting signal. |
| RQ4 | Company and state variables add predictive value beyond complaint characteristics. Company-level signals are stronger than geography but require careful interpretation. |

---

## 19. Model Interpretation Highlights

Feature-family importance from the structured random forest showed the following pattern:

| Feature family | Total importance |
|---|---:|
| Company group | 53.94% |
| Product / sub-product | 19.70% |
| Issue / sub-issue | 12.89% |
| Time period | 6.49% |
| Geography / state | 3.34% |
| Narrative availability / length | 2.05% |
| Submission channel | 0.80% |
| Customer tags | 0.79% |

The model relies most heavily on company group, followed by product/sub-product and issue/sub-issue. The broad `Other` company group showed high importance and high error concentration, so it should be refined in future work.

---

## 20. Business Value

The project can support:

- risk-based complaint triage;
- early-warning dashboards for potential non-timely responses;
- product-level complaint monitoring;
- issue-level operational review;
- company and geography monitoring;
- capacity planning for complaint review teams;
- governance and model-risk reporting;
- responsible use of machine learning in complaint management.

The strongest business value comes from combining multiple signals rather than relying on one variable.

---

## 21. Responsible Use and Governance

The model should be used only as a decision-support tool.

Required governance controls include:

- human review of flagged complaints;
- threshold documentation and approval;
- subgroup performance monitoring;
- false-positive and false-negative tracking;
- drift monitoring and periodic retraining;
- privacy controls for narrative text;
- documentation of feature exclusions and leakage controls;
- audit evidence for model changes and operating thresholds.

The model should not automatically determine complaint outcomes, customer treatment, regulatory responses, or company rankings.

---

## 22. Limitations

Key limitations:

- CFPB public complaints do not represent the full customer population.
- Complaint volume does not equal market share or service quality.
- Observational data supports prediction and association, not causation.
- Narrative availability depends on consumer consent and reporting behavior.
- Text features may include sensitive or proxy information.
- Company and state variables may reflect product mix, market presence, customer base, and case complexity.
- High-cardinality categories can influence feature importance.
- Subgroup performance varies across products, companies, states, channels, years, and tags.
- External validity is limited outside the U.S. CFPB data context.
- Operational deployment would require local validation before use in an internal bank environment.

---

## 23. Key Outputs

Outputs are saved under the `outputs/` folder.

```text
outputs/
├── figures/
├── tables/
└── models/
```

Important output tables include:

- `data_extraction_metadata.json`
- `eda_dataset_overview.csv`
- `final_hypothesis_tests_summary.csv`
- `model_training_performance_comparison.csv`
- `model_training_best_model_summary.csv`
- `final_error_analysis_by_product.csv`
- `final_error_analysis_by_issue.csv`
- `final_subgroup_performance_by_product.csv`
- `final_random_forest_feature_family_importance.csv`
- `final_business_findings_and_recommendations.csv`
- `final_implementation_roadmap.csv`
- `final_capstone_limitations.csv`
- `final_capstone_summary.csv`

---

## 24. Documentation

Additional project documentation is provided in the `docs/` folder.

| Document | Purpose |
|---|---|
| `01_project_overview.md` | Explains the project purpose, business problem, and scope |
| `02_data_access_and_preparation.md` | Explains data download, folder setup, and preparation workflow |
| `03_notebook_execution_guide.md` | Provides notebook running order and expected outputs |
| `04_research_questions_and_hypotheses.md` | Lists research questions and hypotheses |
| `05_eda_and_hypothesis_testing_summary.md` | Summarizes EDA and statistical testing |
| `06_model_training_and_evaluation.md` | Explains model training, features, and evaluation |
| `07_model_interpretation_and_business_findings.md` | Summarizes feature interpretation, errors, subgroup results, and business findings |
| `08_governance_limitations_and_roadmap.md` | Covers limitations, responsible AI controls, and implementation roadmap |
| `09_data_dictionary.md` | Describes key variables and engineered fields |
| `10_literature_review_sources.md` | Lists literature review sources and access links |

---

## 25. Suggested Git Ignore Rules

The raw data file is large and should not be committed to GitHub.

Recommended `.gitignore` entries:

```text
data/raw/
data/processed/
outputs/models/
.ipynb_checkpoints/
__pycache__/
*.pkl
*.joblib
*.zip
```

Small documentation files, selected summary tables, and figures may be committed if appropriate for review.

---

## 26. Reproducibility Notes

To reproduce the analysis:

1. Download the raw CFPB complaint CSV.
2. Save it as `data/raw/complaints.csv`.
3. Install the Python dependencies.
4. Run notebooks 01 through 05 in order.
5. Review generated outputs in `outputs/tables/`, `outputs/figures/`, and `outputs/models/`.
6. Use the `reports/` and `docs/` folders for final write-up and project documentation.

---

## 27. Citation and Data Use

When referencing the raw data, cite the CFPB Consumer Complaint Database as the official data source.

Recommended source statement:

> Data for this project were obtained from the Consumer Financial Protection Bureau Consumer Complaint Database. The analysis, filtering, modeling, and interpretation were conducted independently for academic purposes.

---

## 28. Author

**Zahoor ul Islam**  
Prepared as part of a DBA Data Analytics Capstone project.

