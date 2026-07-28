# Model Training and Evaluation

This document summarises the model training design and evaluation from Notebook 04.

## Modeling Objective

The main modeling objective is to predict whether a complaint will receive a timely response. The target variable is:

```text
1 = Timely response
0 = Non-timely response
```

The rare operational risk class is **non-timely response**.

## Modeling Sample

The project uses a controlled stratified sample for model training to keep runtime practical in Google Colab.

```text
Modeling sample size: 150,000 records
Training set: 105,000 records
Test set: 45,000 records
```

The train-test split is stratified so that timely and non-timely classes remain proportionally represented.

## Class Imbalance

The full dataset is highly imbalanced:

| Class | Count | Percent |
|---|---:|---:|
| Timely response | 1,270,902 | 98.59% |
| Non-timely response | 18,125 | 1.41% |

In the modeling sample, the same imbalance pattern is retained.

## How Class Imbalance Is Treated

The project treats class imbalance using several controls:

1. **Stratified train-test split**  
   The rare non-timely class is preserved in both training and test data.

2. **Class-weighted models**  
   Logistic regression and random forest models use class weighting where appropriate so the minority class receives more attention.

3. **Metrics beyond accuracy**  
   Accuracy is reported but not used alone. The analysis emphasises:

   - Balanced accuracy
   - ROC-AUC
   - Average precision
   - Classwise precision
   - Classwise recall
   - Classwise F1-score
   - Confusion matrices

4. **Non-timely risk perspective**  
   The default target uses timely response as class 1, but the business risk is non-timely response. Therefore, the notebook reports non-timely precision, recall, F1-score, ROC-AUC, and average precision.

5. **Threshold analysis**  
   Different non-timely risk thresholds are tested to show the trade-off between catching more delayed-risk cases and reducing false alerts.

## Why SMOTE Was Not Used in the Main Pipeline

Synthetic oversampling such as SMOTE was not used as the main approach because the dataset contains high-cardinality categorical variables and sparse text features. Creating synthetic complaint records may make interpretation harder and could produce unrealistic combinations of company, product, issue, and narrative patterns. The project instead uses stratified sampling, class weighting, classwise metrics, and threshold analysis.

## Models Trained

| Model | Feature Set | Purpose |
|---|---|---|
| Dummy baseline | No meaningful predictors | Shows why accuracy is misleading under class imbalance. |
| Structured logistic regression | Structured complaint fields | Interpretable baseline with coefficients. |
| Structured + TF-IDF logistic regression | Structured fields plus narrative text | Tests whether narratives improve prediction. |
| Structured random forest | Structured complaint fields | Flexible nonlinear model selected as best by ROC-AUC. |

## Main Features

Structured features include:

```text
product
sub_product
issue
sub_issue
submitted_via
state_grouped
company_grouped
tags
year_received
has_narrative
narrative_length
```

The TF-IDF model additionally uses:

```text
narrative_text
```

## Leakage Controls

Fields created after complaint handling are excluded from intake-stage timely-response prediction. Examples:

```text
company_response_to_consumer
company_public_response
```

These variables are useful for secondary response-outcome analysis but should not be used to predict timeliness at intake.

## Model Performance Summary

| Model | Accuracy | Balanced Accuracy | F1 | ROC-AUC | Average Precision | Main Takeaway |
|---|---:|---:|---:|---:|---:|---|
| Dummy baseline | 0.9859 | 0.5000 | 0.9929 | 0.5000 | 0.9859 | Misleading high accuracy; no risk discrimination. |
| Structured logistic regression | 0.7333 | 0.7908 | 0.8440 | 0.8506 | 0.9974 | Strong and interpretable baseline. |
| Structured + TF-IDF logistic regression | 0.8112 | 0.7384 | 0.8947 | 0.8357 | 0.9970 | Narratives improve some overall metrics but reduce non-timely recall. |
| Structured random forest | 0.7884 | 0.8000 | 0.8802 | 0.8748 | 0.9978 | Best model by ROC-AUC and balanced risk-detection performance. |

## Best Model

The selected model is the **Structured Random Forest** because it achieved the strongest ROC-AUC and balanced accuracy among the tested models.

Key results:

```text
ROC-AUC: 0.8748
Balanced accuracy: 0.8000
F1-score: 0.8802
Average precision: 0.9978
```

## Non-Timely Risk Performance

From the non-timely risk perspective, the final random forest achieved:

```text
Non-timely precision: 0.0518
Non-timely recall: 0.8120
Non-timely F1-score: 0.0974
ROC-AUC for non-timely risk: 0.8748
Average precision for non-timely risk: 0.1181
```

**Interpretation:**  
The model captures many actual non-timely complaints, but precision is low because the minority class is rare. Many flagged complaints are false alerts. Therefore, the model should be used for triage and review, not automated decisions.

## Threshold Analysis

Threshold choice is a business decision. Lower thresholds catch more non-timely complaints but create larger review queues. Higher thresholds create smaller, higher-confidence review queues but miss more actual non-timely cases.

The final report should document:

- Selected threshold.
- Flagged volume.
- Non-timely precision.
- Non-timely recall.
- F1-score.
- Workload impact.
