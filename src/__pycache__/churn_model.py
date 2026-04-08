from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

def train_churn_model():
    # Load dataset
    df = pd.read_csv("data/raw_data.csv")

    # Convert categorical to numeric
    df = pd.get_dummies(df, columns=["feature_used"], drop_first=True)

    # Features and target
    X = df.drop(["user_id", "churn"], axis=1)
    y = df["churn"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Predict
    preds = model.predict(X_test)

    # Accuracy
    print("Model Accuracy:", accuracy_score(y_test, preds))

    return model