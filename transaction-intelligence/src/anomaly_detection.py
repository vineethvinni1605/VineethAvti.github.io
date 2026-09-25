import pandas as pd
from sklearn.ensemble import IsolationForest

# ---------------------------------
# Load engineered transaction data
# ---------------------------------

input_path = (
    "transaction-intelligence/data/"
    "transactions_features.csv"
)

df = pd.read_csv(input_path)

print("TRANSACTION INTELLIGENCE — ANOMALY DETECTION")
print("=" * 52)


# ---------------------------------
# Select model features
# ---------------------------------

features = [
    "amount",
    "hour",
    "is_weekend",
    "is_late_night",
    "customer_avg_amount",
    "customer_transaction_count",
    "amount_ratio"
]

X = df[features].fillna(0)


# ---------------------------------
# Train Isolation Forest
# ---------------------------------

model = IsolationForest(
    n_estimators=200,
    contamination=0.02,
    random_state=42
)

model.fit(X)


# ---------------------------------
# Generate anomaly predictions
# ---------------------------------

df["anomaly_prediction"] = model.predict(X)

# Isolation Forest:
#  1 = normal
# -1 = anomaly

df["is_anomaly"] = (
    df["anomaly_prediction"] == -1
).astype(int)


# Higher value = more anomalous
df["anomaly_score"] = -model.decision_function(X)


# ---------------------------------
# Add explainable risk flags
# ---------------------------------

df["risk_flag"] = "NORMAL"

df.loc[
    df["high_amount_flag"] == 1,
    "risk_flag"
] = "HIGH_AMOUNT"

df.loc[
    (df["unusual_time_flag"] == 1) &
    (df["high_amount_flag"] == 0),
    "risk_flag"
] = "UNUSUAL_TIME"

df.loc[
    (df["is_anomaly"] == 1) &
    (df["risk_flag"] == "NORMAL"),
    "risk_flag"
] = "ML_ANOMALY"


# ---------------------------------
# Results
# ---------------------------------

total_anomalies = df["is_anomaly"].sum()

print(f"\nTotal transactions: {len(df):,}")
print(f"Anomalies detected: {total_anomalies:,}")

print(
    f"Anomaly rate: "
    f"{(total_anomalies / len(df)) * 100:.2f}%"
)

print("\nRisk flag distribution:")
print(df["risk_flag"].value_counts())


# Show highest-scoring anomalies
top_anomalies = (
    df[df["is_anomaly"] == 1]
    .sort_values("anomaly_score", ascending=False)
)

print("\nTop anomalous transactions:")

print(
    top_anomalies[
        [
            "transaction_id",
            "customer_id",
            "amount",
            "amount_ratio",
            "hour",
            "risk_flag",
            "anomaly_score"
        ]
    ].head(10)
)


# ---------------------------------
# Save results
# ---------------------------------

output_path = (
    "transaction-intelligence/outputs/"
    "transaction_anomalies.csv"
)

df.to_csv(output_path, index=False)

print("\nAnomaly detection complete!")
print(f"Results saved to: {output_path}")
