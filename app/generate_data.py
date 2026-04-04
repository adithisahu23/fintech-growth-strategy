import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "user_id": range(1, n+1),
    "transaction_count": np.random.randint(1, 50, n),
    "transaction_amount": np.random.randint(100, 5000, n),
    "session_time": np.random.randint(1, 60, n),
    "feature_used": np.random.choice(["UPI", "BillPay", "Recharge"], n),
    "churn": np.random.choice([0, 1], n, p=[0.7, 0.3])
})

data.to_csv("data/raw_data.csv", index=False)

print("Dataset generated successfully!")