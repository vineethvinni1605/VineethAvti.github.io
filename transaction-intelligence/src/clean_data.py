import pandas as pd

# Load transaction data
input_path = "transaction-intelligence/data/transactions.csv"
df = pd.read_csv(input_path)

print("TRANSACTION INTELLIGENCE — DATA QUALITY")
print("=" * 45)

# Convert timestamp
df["transaction_time"] = pd.to_datetime(df["transaction_time"])

# Initial dataset information
print(f"\nTotal transactions: {len(df):,}")
print(f"Unique customers: {df['customer_id'].nunique():,}")

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate transaction IDs
duplicate_count = df["transaction_id"].duplicated().sum()
print(f"\nDuplicate transaction IDs: {duplicate_count}")

# Invalid transaction amounts
invalid_amounts = (df["amount"] <= 0).sum()
print(f"Invalid transaction amounts: {invalid_amounts}")

# Remove duplicate transactions
df = df.drop_duplicates(subset="transaction_id")

# Remove invalid amounts
df = df[df["amount"] > 0]

# Sort chronologically
df = df.sort_values("transaction_time")

# Save cleaned dataset
output_path = "transaction-intelligence/data/transactions_clean.csv"
df.to_csv(output_path, index=False)

print("\nDATA QUALITY CHECK COMPLETE")
print(f"Clean transactions: {len(df):,}")
print(f"Saved to: {output_path}")