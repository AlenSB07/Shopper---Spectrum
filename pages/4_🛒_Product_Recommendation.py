import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Product Recommendation", page_icon="🛒")

st.title("🛒 Product Recommendation")
st.caption("Get similar products based on customer purchase behaviour.")

# --------------------------------------------------
# Check if required model files exist
# --------------------------------------------------

similarity_file = "models/product_similarity.pkl"
customer_file = "models/customer_product.pkl"

if not (os.path.exists(similarity_file) and os.path.exists(customer_file)):

    st.warning("⚠️ Product Recommendation model is not available in this deployed version.")

    st.info("""
This page requires two large machine learning model files:

- product_similarity.pkl
- customer_product.pkl

These files exceed GitHub's 100 MB file size limit and therefore are not included in the deployed application.

The rest of the Shopper Spectrum application works normally.
""")

    st.stop()

# --------------------------------------------------
# Load Files
# --------------------------------------------------

@st.cache_data
def load_data():
    similarity_df = pd.read_pickle(similarity_file)
    product_list = pd.read_pickle(customer_file).columns.tolist()
    return similarity_df, product_list


similarity_df, product_list = load_data()

# --------------------------------------------------
# Product Selection
# --------------------------------------------------

selected_product = st.selectbox(
    "Select a Product",
    sorted(product_list)
)

# --------------------------------------------------
# Recommendation Function
# --------------------------------------------------

def recommend(product_name):

    if product_name not in similarity_df.index:
        return []

    recommendations = (
        similarity_df.loc[product_name]
        .sort_values(ascending=False)
        .iloc[1:6]
        .index
        .tolist()
    )

    return recommendations

# --------------------------------------------------
# Button
# --------------------------------------------------

if st.button("Get Recommendations"):

    recommendations = recommend(selected_product)

    if recommendations:

        st.success("Top 5 Recommended Products")

        for i, product in enumerate(recommendations, start=1):
            st.write(f"{i}. {product}")

    else:
        st.error("No recommendations found.")