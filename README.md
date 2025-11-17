# Insurance Affordability Risk Score (IARS)

This mini-project implements an innovative real-estate investment metric:  
**Insurance Affordability Risk Score (IARS)** — a measure of how insurance costs may impact the long-term viability of a residential property investment in Australia.

The project includes:
- a data generator that uses part of the provided `transactions.parquet`,
- a clean sample dataset,
- a Python implementation of the metric,
- and a simple interpretation guide.

---

## Why this metric?

Insurance premiums in Australia have risen sharply due to flood, bushfire, storm and climate-related risk factors.  
High insurance costs can quietly erode:

- rental yield  
- long-term affordability  
- future buyer demand  
- resale liquidity

Despite this, insurance affordability is almost invisible in mainstream property analytics.

**IARS provides a simple, intuitive measure of how exposed a property is to insurance-driven financial pressure.**

---

##Metric definition

**Base formula:**

IARS_base = InsuranceCost / MedianIncome

**Extended formula usd in this project**

IARS_extended = IARS_base x ClimateRiskWeight x BuildingAgeFactor

Where:

| Factor | Values |
|--------|--------|
| **ClimateRiskWeight** | low = 1.0, medium = 1.2, high =1.5 |
| **BuildingAgeFactor** | <10 yrs = 0.9, 10–30 yrs = 1.1,>30 yrs = 1.2 |

A **higher score** means **higher insurance affordability risk**, implying weaker long-term investment resilience.

---

## Project structure

insurnce-affordability-risk-score/
|
|-- build_sample_from_transactions.py # converts parquet -> sample CSV
|-- iars_metric.py # computes IARS
|-- sample_properties.csv # generated dataset
|-- transactions.parquet # provided data (not included in repo)
|-- requirements.txt
|-- README.md

## How to run the project

### Install dependencies
pip install -r requirements.txt

##Create a sample file for analysis out of the transactions.parquet file provided by company Google Drive
python build_sample_from_transactions.py

##YOU SHOULD SEE: 
Generated sample_properties.csv with 10 rows.

##TO CALCULATE IARS Metrics: 
python iars_metric.py


## Interpretation Guide: 

Approximate risk ranges:

IARS_extended	Meaning
< 0.03	Low insurance affordability risk
0.03 – 0.06	Moderate risk
> 0.06	High risk / potential pressure on yields

This helps investors quickly identify suburbs or properties where rising insurance costs may erode future returns.


##Notes
1. transactions.parquet is not committed to this repository due to size and license restrictions, but the project is designed to work directly with that file.
2. The sample dataset is generated dynamically to demonstrate real integration with the provided data.
3. The metric is designed to be simple, interpretable, and extendable for future productisation.


