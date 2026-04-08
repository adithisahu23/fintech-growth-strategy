import pandas as pd
from sklearn.cluster import KMeans

def segment_users():
    # Load data
    df = pd.read_csv("data/raw_data.csv")

    # Select features
    features = df[["transaction_count", "transaction_amount", "session_time"]]

    # Apply KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    df["segment"] = kmeans.fit_predict(features)

    print("\nUser Segments:")
    print(df.head())

    return df