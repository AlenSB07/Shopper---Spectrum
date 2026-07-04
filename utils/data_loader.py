import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("clean_online_retail.csv")

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    if "Month" not in df.columns:
        df["Month"] = df["InvoiceDate"].dt.strftime("%B")

    return df