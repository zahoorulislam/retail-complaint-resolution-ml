# Retail Complaint Resolution ML

## Project Title
Using Machine Learning to Predict Complaint Resolution Outcomes in Retail Banking: Evidence from Open Consumer Financial Complaint Data

## Project Purpose
This project uses open CFPB Consumer Complaint Database records to predict complaint-resolution outcomes in retail banking. The study examines response timeliness, company response outcomes, complaint product type, issue categories, submission channel, company, geography, and consumer complaint narratives.

## Main Research Questions
1. Does complaint product type significantly influence timely company response?
2. Do complaint issue categories significantly predict company response outcome?
3. Do complaint narratives improve prediction performance compared with structured fields only?
4. Are company-level and geographic differences significantly associated with complaint resolution outcomes after controlling for product and issue?

## Folder Structure
```text
retail-complaint-resolution-ml/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   ├── processed/
│   ├── external/
│   └── data_dictionary.csv
├── notebooks/
│   ├── 01_data_extraction.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_hypothesis_tests.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_model_interpretation.ipynb
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── modeling.py
│   └── evaluation.py
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── models/
├── docs/
└── reports/
```

## Data Source
Primary data source: CFPB Consumer Complaint Database  
Official website: https://www.consumerfinance.gov/data-research/consumer-complaints/  
API field reference: https://cfpb.github.io/api/ccdb/fields.html  

