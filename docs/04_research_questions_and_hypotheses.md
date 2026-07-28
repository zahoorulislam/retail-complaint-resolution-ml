# Research Questions and Hypotheses

The project is organised around four research questions.

## RQ1: Product Type and Timely Response

**Research question:**  
Does product type influence whether a company gives a timely response?

**Null hypothesis (H0):**  
Product type and timely response are independent.

**Alternative hypothesis (H1):**  
Product type and timely response are significantly associated.

**Methods used:**

- Chi-square test of independence.
- Cramer's V effect size.
- Product-level timely-response rates.
- Product-level error and subgroup performance analysis.

**Business meaning:**  
This question helps identify whether some retail banking products have higher response-timeliness risk and may require different staffing, routing, escalation, or workflow controls.

## RQ2: Issue Category and Company Response Outcomes

**Research question:**  
Are complaint issue categories associated with company response outcomes?

**Null hypothesis (H0):**  
Issue category and company response outcome are independent.

**Alternative hypothesis (H1):**  
Issue category and company response outcome are significantly associated.

**Methods used:**

- Chi-square test of independence.
- Cramer's V effect size.
- Grouped response outcome analysis.
- Relief-rate ranking by issue.
- Company response outcome modeling.

**Business meaning:**  
This question supports complaint routing, specialist assignment, issue-level prioritisation, root-cause analysis, and response playbook design.

## RQ3: Customer Narratives and Predictive Value

**Research question:**  
Do customer-written narratives improve predictive performance beyond structured complaint fields?

**Null hypothesis (H0):**  
Narrative text features do not improve model performance beyond structured variables.

**Alternative hypothesis (H1):**  
Narrative text features improve model performance beyond structured variables.

**Methods used:**

- Narrative coverage analysis.
- Structured logistic regression.
- Structured + TF-IDF logistic regression.
- Comparison of accuracy, balanced accuracy, F1-score, recall, precision, ROC-AUC, and average precision.

**Business meaning:**  
This question evaluates whether complaint narratives contain useful signals about complaint complexity, customer effort, fraud concerns, billing disputes, repeated contact, or unresolved issues.

## RQ4: Company, Geography, and Timely Response

**Research question:**  
Do company and geography add predictive value beyond complaint characteristics?

**Null hypothesis (H0):**  
Company and geography do not add predictive value after accounting for complaint characteristics.

**Alternative hypothesis (H1):**  
Company and geography add predictive value after accounting for complaint characteristics.

**Methods used:**

- Chi-square tests for company group and state group.
- Base model using complaint characteristics.
- Extended model adding company and state variables.
- Incremental value comparison using model metrics.
- Feature-family importance analysis.

**Business meaning:**  
This question supports internal monitoring and governance review. Company and geography are treated as operational signals, not direct performance rankings.

## Summary Table

| RQ | Main Topic | Primary Method | Main Business Use |
|---|---|---|---|
| RQ1 | Product and timely response | Chi-square, Cramer's V, product rates | Product-level monitoring and workflow review |
| RQ2 | Issue and response outcome | Chi-square, grouped response analysis | Routing, specialist assignment, root-cause analysis |
| RQ3 | Narrative value | Structured vs TF-IDF model comparison | NLP-supported triage and complaint complexity review |
| RQ4 | Company and geography signals | Base vs extended model comparison | Governance review and operational monitoring |
