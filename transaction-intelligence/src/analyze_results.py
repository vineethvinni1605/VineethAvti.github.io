import pandas as pd

# Load anomaly detection results
input_path = (
    "transaction-intelligence/outputs/"
    "transaction_anomalies.csv"
)

df = pd.read_csv(input_path)

print("TRANSACTION INTELLIGENCE — RESULTS")
print("=" * 45)

# Basic results
total_transactions = len(df)
total_anomalies = df["is_anomaly"].sum()

print(f"\nTotal transactions: {total_transactions:,}")
print(f"Detected anomalies: {total_anomalies:,}")
print(
    f"Anomaly rate: "
    f"{(total_anomalies / total_transactions) * 100:.2f}%"
)

# Risk flags
print("\nRISK FLAG DISTRIBUTION")
print("-" * 30)
print(df["risk_flag"].value_counts())

# Normal vs anomalous transaction amounts
normal_avg = df.loc[
    df["is_anomaly"] == 0, "amount"
].mean()

anomaly_avg = df.loc[
    df["is_anomaly"] == 1, "amount"
].mean()

print("\nTRANSACTION AMOUNT ANALYSIS")
print("-" * 30)

print(
    f"Average normal transaction: "
    f"${normal_avg:,.2f}"
)

print(
    f"Average anomalous transaction: "
    f"${anomaly_avg:,.2f}"
)

# Highest anomaly scores
top_anomalies = (
    df[df["is_anomaly"] == 1]
    .sort_values(
        "anomaly_score",
        ascending=False
    )
)

print("\nTOP 5 ANOMALIES")
print("-" * 30)

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
    ].head()
)

# Save anomalies only
anomalies_only = df[
    df["is_anomaly"] == 1
]

output_path = (
    "transaction-intelligence/outputs/"
    "flagged_transactions.csv"
)

anomalies_only.to_csv(
    output_path,
    index=False
)

print(
    "\nFlagged transactions saved to:",
    output_path
)

print("\nAnalysis complete!")