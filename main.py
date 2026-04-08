from src.churn_model import train_churn_model
from src.segmentation import segment_users

print("Training churn model...")
train_churn_model()

print("\nSegmenting users...")
segment_users()