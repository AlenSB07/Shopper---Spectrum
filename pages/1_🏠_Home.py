import streamlit as st

st.title("🏠 Home")

st.markdown(
"""
# 🛒 Shopper Spectrum

### Customer Segmentation & Product Recommendation System
"""
)

st.markdown("---")

st.write(
"""
This application helps businesses understand customer behaviour using
Machine Learning.

### Features

- 👥 Customer Segmentation
- 🛍 Product Recommendation
- 📊 Business Dashboard
- 📈 Business Insights

---
"""
)

c1,c2,c3,c4=st.columns(4)

c1.metric("Customers","4,338")
c2.metric("Products","3,684")
c3.metric("Orders","18,536")
c4.metric("Revenue","£8.3M")

st.markdown("---")

st.subheader("Workflow")

st.code("""
Dataset
      ↓
Data Cleaning
      ↓
EDA
      ↓
RFM Analysis
      ↓
KMeans Clustering
      ↓
Customer Segmentation
      ↓
Recommendation System
""")