# Transaction Intelligence

An end-to-end financial transaction analytics project designed to identify unusual transaction behavior using data-quality validation, behavioral feature engineering, rule-based risk indicators, and unsupervised machine learning.

## Project Overview

Transaction Intelligence analyzes synthetic financial transaction data to identify behavioral patterns and potentially anomalous activity.

The project combines traditional data processing with explainable risk rules and an Isolation Forest anomaly-detection model.

## Dataset

The project uses a synthetically generated dataset containing:

- 10,000 transactions
- 500 customers
- Multiple merchant categories
- Online, POS, Mobile, and ATM transaction channels
- Transaction timestamps and amounts

Synthetic data was used so the complete analytics pipeline could be developed without exposing real customer or banking information.

## Pipeline

Raw Transactions
→ Data Quality Validation
→ Data Cleaning
→ Feature Engineering
→ Behavioral Analysis
→ Isolation Forest
→ Risk Flags
→ Anomaly Analysis

## Data Quality

Before modeling, the pipeline validates:

- Missing values
- Duplicate transaction IDs
- Invalid transaction amounts
- Timestamp formatting
- Transaction consistency

## Feature Engineering

Behavioral features include:

- Transaction hour
- Day of week
- Weekend indicator
- Late-night activity
- Customer average transaction amount
- Customer transaction frequency
- Amount deviation
- Amount-to-customer-average ratio

These features allow individual transactions to be evaluated relative to a customer's broader behavior.

## Risk Signals

The system generates interpretable risk indicators including:

- `HIGH_AMOUNT`
- `UNUSUAL_TIME`
- `ML_ANOMALY`
- `NORMAL`

## Anomaly Detection

Isolation Forest was used as the unsupervised anomaly-detection algorithm.

The model evaluates transaction characteristics and customer behavioral features to identify observations that differ substantially from common patterns.

The model was configured with a 2% contamination assumption.

Therefore, detected anomalies represent unusual transactions under the modeling assumptions and should not be interpreted as confirmed fraud.

## Results

The pipeline processed 10,000 transactions and identified 200 observations as anomalous under the configured Isolation Forest threshold.

Average transaction amount:

- Normal transactions: $51.26
- Detected anomalies: $585.91

Risk flag distribution:

- Normal: 6,635
- Unusual Time: 2,790
- High Amount: 542
- ML Anomaly: 33

The results demonstrate that anomalous observations tended to have substantially higher transaction values while the rule-based layer provided additional behavioral context.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Isolation Forest
- Data Quality Validation
- Feature Engineering
- Behavioral Analytics

## Project Structure

transaction-intelligence/
- data/
- notebooks/
- outputs/
- sql/
- src/
- README.md

## Key Takeaway

The project demonstrates how data engineering, behavioral feature engineering, explainable rules, and unsupervised machine learning can be combined into a simple transaction-monitoring pipeline.

The system identifies unusual behavior rather than making direct fraud determinations, allowing detected transactions to be prioritized for further analysis.