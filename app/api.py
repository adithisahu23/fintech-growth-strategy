from flask import Flask, request, jsonify
from src.churn_model import train_churn_model
import pandas as pd

# Create app FIRST
app = Flask(__name__)

# Train model
model = train_churn_model()

# Home route
@app.route("/")
def home():
    return "Fintech Churn API Running 🚀"

# Predict route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    print("🔥 Received request:", data)

    df = pd.DataFrame([data])
    df = pd.get_dummies(df)

    # Align columns
    for col in model.feature_names_in_:
        if col not in df:
            df[col] = 0

    df = df[model.feature_names_in_]

    prediction = model.predict(df)

    return jsonify({"churn_prediction": int(prediction[0])})

# Run server
if __name__ == "__main__":
    app.run(debug=True)