# Literature Review Sources

This document lists key sources used to support the literature review, data source discussion, methodology, class imbalance treatment, text analytics, model interpretation, and governance sections.

## Public Data and CFPB Documentation

| Source | Title | Relevance | URL |
|---|---|---|---|
| Consumer Financial Protection Bureau | Consumer Complaint Database | Main public dataset for the project. | https://www.consumerfinance.gov/data-research/consumer-complaints/ |
| Consumer Financial Protection Bureau | How We Share Complaint Data | Supports discussion of narrative sharing, privacy, and public complaint data governance. | https://www.consumerfinance.gov/complaint/data-use/ |
| CFPB Open Tech | Consumer Complaint Database API Documentation | Supports field definitions and data dictionary. | https://cfpb.github.io/api/ccdb/ |
| Data.gov | Consumer Complaint Database | Confirms the dataset in the U.S. government open-data catalogue. | https://catalog.data.gov/dataset/consumer-complaint-database |

## Complaint Management and Service Recovery

| Author | Year | Title | Relevance | URL |
|---|---:|---|---|---|
| Tax, Brown, & Chandrashekaran | 1998 | Customer Evaluations of Service Complaint Experiences: Implications for Relationship Marketing | Supports business context that complaint handling affects customer trust and relationship outcomes. | https://doi.org/10.1177/002224299806200205 |
| Maxham & Netemeyer | 2002 | Modeling Customer Perceptions of Complaint Handling Over Time | Supports discussion of complaint handling, perceived justice, satisfaction, and future customer intent. | https://doi.org/10.1016/S0022-4359(02)00100-8 |
| Homburg & Fürst | 2005 | How Organizational Complaint Handling Drives Customer Loyalty | Supports operational complaint handling, escalation, and process maturity discussion. | https://doi.org/10.1509/jmkg.69.3.95.66367 |

## Machine Learning and Evaluation

| Author | Year | Title | Relevance | URL |
|---|---:|---|---|---|
| Hosmer, Lemeshow, & Sturdivant | 2013 | Applied Logistic Regression | Supports logistic regression as an interpretable baseline model. | https://doi.org/10.1002/9781118548387 |
| Breiman | 2001 | Random Forests | Supports the random forest model used for final prediction. | https://doi.org/10.1023/A:1010933404324 |
| Pedregosa et al. | 2011 | Scikit-Learn: Machine Learning in Python | Supports reproducible implementation using scikit-learn. | https://www.jmlr.org/papers/v12/pedregosa11a.html |
| Chawla et al. | 2002 | SMOTE: Synthetic Minority Over-Sampling Technique | Supports class imbalance discussion and explains an alternative not used in the main pipeline. | https://doi.org/10.1613/jair.953 |
| Davis & Goadrich | 2006 | The Relationship Between Precision-Recall and ROC Curves | Supports ROC-AUC, precision-recall, and threshold analysis for imbalanced classification. | https://doi.org/10.1145/1143844.1143874 |
| Kaufman, Rosset, & Perlich | 2012 | Leakage in Data Mining | Supports leakage-control discussion and exclusion of post-response fields. | https://doi.org/10.1145/2382577.2382579 |

## Text Analytics and Responsible AI

| Author | Year | Title | Relevance | URL |
|---|---:|---|---|---|
| Blei, Ng, & Jordan | 2003 | Latent Dirichlet Allocation | Supports possible future topic modeling for complaint narratives. | https://www.jmlr.org/papers/v3/blei03a.html |
| Loughran & McDonald | 2011 | When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks | Supports caution that financial text has domain-specific language. | https://doi.org/10.1111/j.1540-6261.2010.01625.x |
| Ribeiro, Singh, & Guestrin | 2016 | “Why Should I Trust You?”: Explaining the Predictions of Any Classifier | Supports explainability and model interpretation discussion. | https://doi.org/10.1145/2939672.2939778 |
| Mehrabi et al. | 2021 | A Survey on Bias and Fairness in Machine Learning | Supports subgroup monitoring and fairness governance. | https://doi.org/10.1145/3457607 |
| Barocas, Hardt, & Narayanan | 2023 | Fairness and Machine Learning: Limitations and Opportunities | Supports responsible AI, fairness, and governance discussion. | https://mitpress.mit.edu/9780262048613/fairness-and-machine-learning/ |

## CFPB Complaint Analytics Examples

| Author | Year | Title | Relevance | URL |
|---|---:|---|---|---|
| Vaishnav, Neethinayagam, Khaire, & Woo | 2024 | Predictive Analysis of CFPB Consumer Complaints Using Machine Learning | Directly relevant CFPB complaint ML benchmark. | https://arxiv.org/abs/2407.06399 |
| Gao, Sun, Wang, Yang, & Zitikis | 2023 | NLP-Based Detection of Systematic Anomalies Among the Narratives of Consumer Complaints | Supports narrative analytics using CFPB complaint text. | https://arxiv.org/abs/2308.11138 |
| Wang, Zhu, & Chen | 2026 | From Complaint Narratives to Monetary Relief | Supports future work on relief prediction, narratives, and class imbalance. | https://arxiv.org/abs/2606.22664 |

## APA 7 Note

When writing the formal report, use DOI links where available. For public data and documentation, use the official CFPB, CFPB GitHub, or Data.gov URL.
