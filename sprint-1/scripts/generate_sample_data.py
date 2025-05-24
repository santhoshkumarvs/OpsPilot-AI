import pandas as pd
import os

data = {
    "transaction_id": range(1, 6),
    "user_id": [101, 102, 103, 104, 105],
    "amount": [250.0, 140.5, 560.3, 80.0, 1000.0],
    "timestamp": pd.date_range(start="2024-01-01", periods=5, freq="D"),
    "age": [25, 34, 45, 29, 60],
    "income": [45000, 54000, 75000, 39000, 100000],
    "transaction_count": [5, 10, 2, 8, 20],
    "fraud_flag": [0, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

os.makedirs("./data", exist_ok=True)
df.to_csv("./data/transactions.csv", index=False)
print("✅ Dummy transaction data generated with full schema.")
