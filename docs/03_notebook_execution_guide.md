# Notebook Execution Guide

Run the notebooks in sequence. Each notebook creates outputs that are used by the next stage.

## 1. Data Extraction

Notebook:

```text
01_data_extraction_colab_csv_v2.ipynb
```

Purpose:

- Load the raw CFPB complaint file.
- Filter retail banking-related complaints.
- Filter the 2017–2025 study period.
- Clean column names.
- Create derived variables.
- Save the processed dataset.

Main inputs:

```text
data/raw/complaints.csv
```

Main outputs:

```text
data/processed/cfpb_retail_complaints_2017_2025.csv
outputs/tables/data_extraction_metadata.json
```

## 2. Exploratory Data Analysis

Notebook:

```text
02_exploratory_analysis_v2.ipynb
```

Purpose:

- Profile the processed dataset.
- Review missing values and target distribution.
- Analyse product, issue, company, state, channel, narrative, and time patterns.
- Generate figures and EDA tables for the report.

Main outputs:

```text
outputs/tables/
outputs/figures/
```

## 3. Hypothesis Testing

Notebook:

```text
03_hypothesis_tests_v2.ipynb
```

Purpose:

- Test RQ1 using product type and timely response.
- Test RQ2 using issue category and response outcomes.
- Support RQ3 through narrative coverage and model-comparison design.
- Test RQ4 using company and state associations.
- Use chi-square tests, Cramer's V, grouped response outcomes, and supporting tables.

Main outputs:

```text
outputs/tables/hypothesis_*.csv
outputs/tables/rq*_*.csv
```

## 4. Model Training

Notebook:

```text
04_model_training_v2.ipynb
```

Purpose:

- Prepare modeling features.
- Create a stratified train-test split.
- Train baseline and predictive models.
- Compare structured logistic regression, structured + TF-IDF logistic regression, and structured random forest.
- Evaluate models using metrics appropriate for class imbalance.
- Save models, metrics, and interpretation inputs.

Main outputs:

```text
outputs/tables/model_performance.csv
outputs/tables/final_model_performance_comparison.csv
outputs/models/
```

## 5. Model Interpretation

Notebook:

```text
05_model_interpretation_v2.ipynb
```

Purpose:

- Load model outputs.
- Select the best model by ROC-AUC.
- Analyse non-timely risk performance.
- Review threshold trade-offs.
- Interpret feature importance and coefficients.
- Conduct error analysis and subgroup performance review.
- Create business findings, roadmap, limitations, and final summary tables.

Main outputs:

```text
outputs/tables/final_business_findings_and_recommendations.csv
outputs/tables/final_executive_ready_business_observations.csv
outputs/tables/final_capstone_limitations.csv
outputs/tables/final_capstone_summary.csv
outputs/figures/final_random_forest_feature_family_importance.png
```

## Recommended Execution Environment

The notebooks were designed for Google Colab with Google Drive mounted. A local environment can also be used if the folder paths are adjusted.

Recommended Python libraries:

```text
pandas
numpy
matplotlib
scikit-learn
scipy
joblib
```

## Execution Notes

- Run Notebook 01 first because all later notebooks depend on the processed dataset.
- For model training, a controlled stratified sample is used to keep runtime practical.
- The raw CFPB file is large; chunk processing is used in Notebook 01.
- If model files are missing, rerun Notebook 04 before Notebook 05.
- If optional interpretation tables are missing, Notebook 05 continues where possible and reports available results.
