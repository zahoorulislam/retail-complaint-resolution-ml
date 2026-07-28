# Model Interpretation and Business Findings

This document summarises model interpretation and business findings from Notebook 05.

## Best Model Interpretation

The structured random forest was selected as the best model by ROC-AUC. It provides the strongest balance between detecting response-timeliness risk and handling nonlinear interactions among complaint features.

The model should be interpreted as a **risk-ranking and triage tool**, not as an automated decision system.

## Feature Family Importance

Random forest feature-family importance showed that the model relied most heavily on company-level information.

| Feature Family | Total Importance | Importance Percent | Main Interpretation |
|---|---:|---:|---|
| Company group | 0.5394 | 53.94% | Strongest operational signal. |
| Product / sub-product | 0.1970 | 19.70% | Important product-level risk signal. |
| Issue / sub-issue | 0.1289 | 12.89% | Captures complaint type and complexity. |
| Time period | 0.0649 | 6.49% | Shows complaint patterns vary over time. |
| Geography / state | 0.0334 | 3.34% | Adds supporting regional context. |
| Narrative availability / length | 0.0205 | 2.05% | Captures basic narrative complexity. |
| Submission channel | 0.0080 | 0.80% | Minor contribution. |
| Customer tags | 0.0079 | 0.79% | Minor contribution. |

## Interpretation Caution

Random forest importance shows **predictive usefulness**, not direction or causality. Company group has high importance, but this does not mean a company causes delay. The result may reflect complaint volume, product mix, customer base, servicing model, case complexity, or grouping logic.

## Logistic Regression Coefficients

Logistic regression coefficients provide directional interpretation because the target is timely response:

```text
Positive coefficient = higher predicted probability of timely response
Negative coefficient = lower predicted probability of timely response
```

Structured logistic regression showed that several company groups had strong negative coefficients, while some product and issue categories had positive coefficients. This supports the finding that company, product, and issue characteristics influence prediction.

## Narrative Coefficients

The structured + TF-IDF logistic model showed that narrative terms can be influential. Terms related to fraud, billing, cards, dealers, disbursement, repeated contact, and time references were associated with lower predicted probability of timely response in the model.

This supports RQ3, but the terms should not be read as causal. Words are predictive signals within the dataset, not direct reasons for delay.

## Error Analysis

The final error analysis showed that model errors were concentrated in specific segments rather than randomly distributed.

High-error areas included:

- Payday loan, title loan, personal loan, or advance loan products.
- Bank account/service and consumer-loan categories.
- Mortgage and vehicle loan categories.
- Fee, loan servicing, payoff, account management, and closing issues.
- The broad `Other` company group.
- Older complaint years.

## Subgroup Performance

Subgroup performance varied by product, company, state, submission channel, year, and customer tag. This means the model is not equally stable across all segments.

Important subgroup finding:

- The `Other` company group had high feature importance and high error concentration.
- This group combines many smaller or less frequent companies and should be refined in future work.

## Company Response Outcome Modeling

A secondary model examined company response outcomes.

Response distribution:

| Response Group | Count | Percent |
|---|---:|---:|
| Closed with explanation | 1,038,396 | 80.56% |
| Relief provided | 247,704 | 19.22% |
| Other response | 2,844 | 0.22% |
| In progress | 22 | 0.00% |

The response outcome model showed useful directional value for identifying relief-provided cases, but rare categories were difficult to model. Future work should consider a simpler target:

```text
Relief provided vs. No relief provided
```

## Business Findings

| Finding Area | Business Meaning | Recommended Action |
|---|---|---|
| Best predictive model | Structured random forest can rank complaints by timeliness risk. | Use as early-warning decision support. |
| Accuracy limitation | High accuracy can be misleading due to class imbalance. | Use ROC-AUC, balanced accuracy, precision, recall, F1, and threshold analysis. |
| Non-timely risk detection | Model catches many delayed-risk cases but creates false alerts. | Use human review and capacity-based thresholds. |
| Narrative value | Text adds context but does not solve rare-risk detection alone. | Use narratives as supporting signals. |
| Company and geography | Company/state add predictive value but require caution. | Use for internal monitoring, not public ranking. |
| Product and issue errors | Some segments show more unstable predictions. | Review workflows, escalation rules, and model calibration. |
| Governance | Model reflects historical public complaint patterns. | Apply monitoring, documentation, and human oversight. |

## Final Business Recommendation

The model is best suited for a **risk-based complaint triage framework**. It can help complaint teams prioritise review queues, monitor high-risk segments, and support governance reporting. It should not be used to automatically decide complaint outcomes or customer treatment.
