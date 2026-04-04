import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw_data.csv")

st.title("💳 Fintech Growth Dashboard")

# -----------------------
# Churn Distribution
# -----------------------
st.subheader("📉 Churn Distribution")
st.bar_chart(df["churn"].value_counts())

# -----------------------
# Transaction Behavior
# -----------------------
st.subheader("📊 Transaction Behavior")
fig, ax = plt.subplots()
ax.scatter(df["transaction_count"], df["transaction_amount"])
ax.set_xlabel("Transaction Count")
ax.set_ylabel("Transaction Amount")
st.pyplot(fig)

# -----------------------
# Feature Usage
# -----------------------
st.subheader("⚙️ Feature Usage")
st.bar_chart(df["feature_used"].value_counts())

# -----------------------
# Insights
# -----------------------
st.subheader("💡 Key Insights")

churn_rate = df["churn"].mean()
st.write(f"🔹 Churn Rate: {round(churn_rate*100,2)}%")

high_value = df[df["transaction_amount"] > 3000].shape[0]
st.write(f"🔹 High Value Users: {high_value}")