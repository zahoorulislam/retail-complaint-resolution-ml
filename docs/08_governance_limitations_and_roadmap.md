# Governance, Limitations, and Implementation Roadmap

## Responsible Use Position

The complaint response model should be used as **decision support**, not as an automated complaint decision system. Human review is required before escalation, remediation, customer treatment, or governance action.

## Key Limitations

| Limitation | Meaning | Mitigation |
|---|---|---|
| Public complaint data is not the full customer population | CFPB complaints do not represent all customers or all internal bank complaints. | Avoid using results as market-share or company-quality rankings. |
| Observational data does not prove causation | The models identify associations, not causal effects. | Use cautious language such as associated with or predictive of. |
| Class imbalance affects behavior | Non-timely complaints are rare. | Use balanced metrics, classwise metrics, and threshold analysis. |
| Non-timely precision remains low | Many flagged complaints may still be timely. | Use human review and threshold governance. |
| Narrative availability is incomplete | Not every complaint has a narrative. | Report narrative coverage and treat text as a supporting signal. |
| Narrative text may contain sensitive information | Text may include location, hardship, identity, or fraud details. | Use privacy controls, data minimisation, and responsible AI review. |
| Company and state need careful interpretation | Results may reflect volume, product mix, and case complexity. | Do not treat as direct performance rankings. |
| Broad `Other` company group creates interpretation risk | It combines many different companies. | Refine company grouping in future work. |
| Feature importance may favour high-cardinality categories | Company and issue fields contain many categories. | Use feature-family interpretation and business review. |
| Model drift may occur | Complaint patterns can change over time. | Monitor year-level performance and retrain periodically. |
| External validity is limited | CFPB U.S. data may not transfer directly to other jurisdictions. | Validate locally before operational deployment. |

## Governance Controls

Before operational use, the following controls should be in place:

- Model documentation.
- Target definition and feature dictionary.
- Leakage-control documentation.
- Threshold approval and review process.
- False-positive and false-negative monitoring.
- Subgroup performance monitoring.
- Human-in-the-loop review.
- Privacy controls for narrative text.
- Periodic model retraining.
- Audit trail of model changes and approvals.

## Implementation Roadmap

| Phase | Focus | Activities | Risk Control |
|---|---|---|---|
| Phase 1 | Analytical validation | Validate final model results, feature interpretation, subgroup analysis, error analysis, and leakage controls. | Document assumptions, limitations, class imbalance, and threshold rationale. |
| Phase 2 | Business validation | Review high-risk product, issue, company, state, and year segments with operations experts. | Do not interpret model outputs as causal findings or direct rankings. |
| Phase 3 | Threshold calibration | Select the non-timely risk threshold based on review capacity, false-alert tolerance, and missed-risk tolerance. | Document precision, recall, flagged volume, F1-score, and workload impact. |
| Phase 4 | Pilot dashboard | Build a dashboard showing risk score, product, issue, company group, state, channel, narrative indicators, and top risk segments. | Clearly label predictions as decision-support indicators. |
| Phase 5 | Workflow integration | Route selected high-risk complaints for earlier review, specialist handling, or supervisor monitoring. | Keep human-in-the-loop controls and prohibit automated decisions. |
| Phase 6 | Governance monitoring | Track model drift, subgroup performance, false positives, false negatives, and threshold performance. | Maintain audit trail, privacy controls, retraining schedule, and model-risk review. |
| Phase 7 | Future enhancement | Refine company grouping, test relief-vs-no-relief modeling, and improve narrative features. | Validate enhancements before adoption using balanced metrics and business review. |

## Final Governance Conclusion

The project demonstrates that machine learning can support complaint-risk triage in retail banking. However, the model reflects historical patterns in public complaint data and should be used only with clear governance, human oversight, and monitoring.
