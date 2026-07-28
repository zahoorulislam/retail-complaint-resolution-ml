# Project Overview

## Project Title

**Using Machine Learning to Predict Complaint Resolution Outcomes in Retail Banking: Evidence from Open Consumer Financial Complaint Data**

## Business Problem

Retail banking complaint teams handle large volumes of complaints across products such as checking accounts, credit cards, prepaid cards, mortgage, vehicle loans, payday or personal loans, and money-transfer services. Although most complaints receive timely responses, a small share of cases are non-timely or operationally complex. These rare delayed-response cases are important because they may create regulatory, customer-experience, reputational, and operational risk.

The project addresses the challenge of identifying complaint patterns that are more likely to be associated with delayed response or different company response outcomes. The goal is not to replace human judgment. The goal is to support earlier triage, monitoring, and governance review.

## Project Objective

The project uses public Consumer Financial Protection Bureau (CFPB) complaint data to:

- Examine product-level and issue-level complaint patterns.
- Test whether product, issue, company, and geography are associated with response timeliness and response outcomes.
- Evaluate whether customer narratives improve predictive performance.
- Train and compare machine learning models for response-timeliness risk.
- Interpret model behavior using feature importance, error analysis, subgroup performance, and business findings.

## Stakeholders

| Stakeholder | Why the Project Matters |
|---|---|
| Complaint operations teams | Helps prioritise cases that may require early review or escalation. |
| Risk and compliance teams | Supports monitoring of delayed-response risk and governance reporting. |
| Product owners | Identifies product areas where complaint workflows may require improvement. |
| Customer experience leaders | Supports better understanding of complaint drivers and resolution patterns. |
| Analytics and data science teams | Demonstrates a reproducible ML workflow using public complaint data. |
| Academic reviewers | Shows application of statistical testing, machine learning, interpretation, and governance. |

## Scope

The analysis focuses on retail banking-related complaints from 2017 through 2025. The primary target is **timely response**, represented as:

```text
1 = Timely response
0 = Non-timely response
```

A secondary response-outcome analysis examines grouped company response categories such as closed with explanation and relief provided.

## Business Value

The project provides value through:

- Risk-based complaint triage.
- Early-warning dashboards for complaint operations.
- Product-level and issue-level monitoring.
- Company and geography signal review.
- Narrative-based complaint complexity analysis.
- Model governance and subgroup performance monitoring.

## Final Business Position

The final model should be used as a **decision-support tool** with human review. It should not automatically determine complaint outcomes, customer treatment, escalation decisions, or company rankings.
