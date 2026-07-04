import streamlit as st

st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ Shopper Spectrum")
st.subheader("Customer Intelligence & Recommendation Platform")

st.markdown("""
Welcome to **Shopper Spectrum**, a Business Intelligence and Machine Learning application built using the Online Retail dataset.

### 🚀 Features

- 📊 Business Dashboard
- 👥 Customer Segmentation (KMeans)
- 🛒 Product Recommendation (Cosine Similarity)
- 📈 Business Insights
- ℹ️ About Project

Use the **sidebar** to navigate between pages.
""")

st.info("👈 Select a page from the left sidebar to begin.")

st.divider()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Customers", "4,338")
col2.metric("Products", "3,684")
col3.metric("Transactions", "541,909")
col4.metric("Countries", "38")

st.divider()

st.success("Developed using Python • Streamlit • Pandas • Plotly • Scikit-learn")