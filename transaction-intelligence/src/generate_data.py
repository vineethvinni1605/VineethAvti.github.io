import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

NUM_TRANSACTIONS = 10000
NUM_CUSTOMERS = 500

customers = [f"CUST_{i:04d}" for i in range(1, NUM_CUSTOMERS + 1)]

categories = [
    "Grocery",
    "Restaurant",
    "Shopping",
    "Travel",
    "Entertainment",
    "Utilities",
    "Healthcare",
    "Electronics"
]

channels = [
    "Online",
    "POS",
    "Mobile",
    "ATM"
]

start_date = datetime(2026, 1, 1)

records = []

for i in range(NUM_TRANSACTIONS):

    customer = np.random.choice(customers)

    amount = round(np.random.lognormal(mean=3.5, sigma=1), 2)

    category = np.random.choice(categories)

    channel = np.random.choice(
        channels,
        p=[0.35, 0.35, 0.20, 0.10]
    )

    transaction_time = start_date + timedelta(
        minutes=int(np.random.randint(0, 60 * 24 * 180))
    )

    records.append({
        "transaction_id": f"TXN_{i+1:06d}",
        "customer_id": customer,
        "transaction_time": transaction_time,
        "amount": amount,
        "merchant_category": category,
        "channel": channel
    })


df = pd.DataFrame(records)

# Inject unusual high-value transactions
anomaly_indices = np.random.choice(
    df.index,
    size=100,
    replace=False
)

df.loc[anomaly_indices, "amount"] *= 15

df["amount"] = df["amount"].round(2)


output_path = "transaction-intelligence/data/transactions.csv"

df.to_csv(output_path, index=False)

print("Dataset created successfully!")
print(f"Transactions: {len(df):,}")
print(f"Customers: {df['customer_id'].nunique():,}")
print("\nSample:")
print(df.head())