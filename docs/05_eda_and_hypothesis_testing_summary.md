# EDA and Hypothesis Testing Summary

This document summarises the exploratory analysis and statistical testing completed in Notebooks 02 and 03.

## Dataset Overview

The processed dataset contains retail banking-related complaints from 2017 through 2025. The unit of analysis is one CFPB complaint record.

Key processed dataset size:

```text
Rows: 1,289,027
Columns: 25
```

The target variable is `timely_response_binary`:

```text
1 = Timely response
0 = Non-timely response
```

## Target Distribution

The target variable is highly imbalanced:

| Target Class | Count | Percent |
|---|---:|---:|
| Timely response | 1,270,902 | 98.59% |
| Non-timely response | 18,125 | 1.41% |

This imbalance shaped the full modeling strategy. Accuracy alone was treated as misleading, and the project used balanced accuracy, ROC-AUC, precision, recall, F1-score, average precision, and threshold analysis.

## Narrative Coverage

Customer narratives are useful but incomplete. About half of the records have complaint narratives available. This supports the RQ3 design decision to compare structured-only models with structured + TF-IDF models rather than relying only on text.

## RQ1 Result: Product Type and Timely Response

The chi-square test showed that product type is statistically associated with timely response.

Key result:

```text
Chi-square statistic: 11,098.27
Degrees of freedom: 13
p-value: < .001
Cramer's V: 0.0928
Effect size: Very weak
```

**Interpretation:**  
The association is statistically significant because the dataset is very large, but the effect size is very weak. Product type is useful as an operational signal, but it does not fully explain response delay.

## RQ2 Result: Issue Category and Company Response Outcome

The chi-square test showed that issue category is statistically associated with company response outcome.

Key result:

```text
Chi-square statistic: 226,378.93
Degrees of freedom: 125
p-value: < .001
Cramer's V: 0.1874
Effect size: Weak
```

Grouped response outcomes showed that most complaints were closed with explanation, while a smaller but meaningful share resulted in relief.

| Company Response Group | Count | Percent |
|---|---:|---:|
| Closed with explanation | 1,038,396 | 80.56% |
| Relief provided | 247,704 | 19.22% |
| Other response | 2,844 | 0.22% |
| In progress | 22 | 0.00% |

**Interpretation:**  
Issue categories help explain likely response outcomes and may support routing, root-cause analysis, and specialist assignment.

## RQ3 EDA Support: Narrative Features

Narrative features include:

```text
has_narrative
narrative_length
narrative_text
```

EDA confirmed that narratives are not available for all complaints, so the analysis treats text as a supporting signal rather than a complete data source. The model comparison in Notebook 04 evaluates whether TF-IDF improves prediction.

## RQ4 Result: Company and State Association

Company group and state group were statistically associated with timely response.

Company group result:

```text
Chi-square statistic: 20,007.22
p-value: < .001
Cramer's V: 0.1246
Effect size: Weak
```

State group result:

```text
Chi-square statistic: 449.34
p-value: < .001
Cramer's V: 0.0187
Effect size: Very weak
```

**Interpretation:**  
Company group is a stronger signal than state group. However, company and geography should not be interpreted as direct performance rankings because the dataset does not fully control for market share, customer base, complaint volume, product mix, or case complexity.

## Main EDA Business Insights

- Timely responses dominate the dataset, creating a rare-risk prediction problem.
- Product, issue, company, and state variables are associated with complaint outcomes, but effect sizes vary.
- Product and issue categories are useful for operational triage.
- Company-level patterns are important but require careful governance interpretation.
- Narrative data adds context but is incomplete and may include sensitive information.
