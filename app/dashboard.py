import streamlit as st
import pandas as pd
import os

st.title("Fintech Growth Dashboard 🚀")

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw_data.csv")

st.write("Loading data...")

df = pd.read_csv(file_path)

st.write("Dataset Preview")
st.dataframe(df.head())