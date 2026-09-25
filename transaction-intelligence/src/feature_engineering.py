import pandas as pd

# Load cleaned data
input_path = "transaction-intelligence/data/transactions_clean.csv"
df = pd.read_csv(input_path)

df["transaction_time"] = pd.to_datetime(df["transaction_time"])

print("TRANSACTION INTELLIGENCE — FEATURE ENGINEERING")
print("=" * 50)

# ---------------------------------
# Time-based features
# ---------------------------------

df["hour"] = df["transaction_time"].dt.hour
df["day_of_week"] = df["transaction_time"].dt.dayofweek

# Weekend indicator
df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)

# Late-night transaction indicator
df["is_late_night"] = (
    (df["hour"] >= 23) | (df["hour"] <= 5)
).astype(int)


# ---------------------------------
# Customer behavioral features
# ---------------------------------

customer_stats = (
    df.groupby("customer_id")["amount"]
    .agg(["mean", "std", "count"])
    .reset_index()
)

customer_stats.columns = [
    "customer_id",
    "customer_avg_amount",
    "customer_amount_std",
    "customer_transaction_count"
]

df = df.merge(
    customer_stats,
    on="customer_id",
    how="left"
)


# ---------------------------------
# Amount deviation
# ---------------------------------

df["amount_deviation"] = (
    df["amount"] - df["customer_avg_amount"]
)

df["amount_ratio"] = (
    df["amount"] /
    df["customer_avg_amount"].replace(0, 1)
)


# ---------------------------------
# Simple behavioral risk flags
# ---------------------------------

df["high_amount_flag"] = (
    df["amount_ratio"] >= 3
).astype(int)

df["unusual_time_flag"] = (
    df["is_late_night"]
).astype(int)


# ---------------------------------
# Save engineered dataset
# ---------------------------------

output_path = (
    "transaction-intelligence/data/"
    "transactions_features.csv"
)

df.to_csv(output_path, index=False)


print(f"\nTransactions processed: {len(df):,}")

print("\nNew features created:")
print("""
- hour
- day_of_week
- is_weekend
- is_late_night
- customer_avg_amount
- customer_amount_std
- customer_transaction_count
- amount_deviation
- amount_ratio
- high_amount_flag
- unusual_time_flag
""")

print("Feature engineering complete!")
print(f"Saved to: {output_path}")