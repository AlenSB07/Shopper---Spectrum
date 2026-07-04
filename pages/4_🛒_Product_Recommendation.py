import streamlit as st
from joblib import load
import os

st.set_page_config(page_title="Product Recommendation", page_icon="🛒")

st.title("🛒 Product Recommendation")
st.caption("Get similar products based on customer purchase behaviour")

# ----------------------------------------------------
# Check Model Files
# ----------------------------------------------------

SIMILARITY_FILE = "models/product_similarity.joblib"
CUSTOMER_FILE = "models/customer_product.joblib"

if not os.path.exists(SIMILARITY_FILE):
    st.error("❌ product_similarity.joblib not found.")
    st.stop()

if not os.path.exists(CUSTOMER_FILE):
    st.error("❌ customer_product.joblib not found.")
    st.stop()

# ----------------------------------------------------
# Load Models
# ----------------------------------------------------

@st.cache_resource
def load_models():

    similarity_df = load(SIMILARITY_FILE)
    customer_product = load(CUSTOMER_FILE)

    return similarity_df, customer_product

similarity_df, customer_product = load_models()

product_list = sorted(customer_product.columns.tolist())

# ----------------------------------------------------
# Product Selection
# ----------------------------------------------------

selected_product = st.selectbox(
    "Select a Product",
    product_list
)

# ----------------------------------------------------
# Recommendation Function
# ----------------------------------------------------

def recommend(product):

    if product not in similarity_df.index:
        return []

    recommendations = (
        similarity_df.loc[product]
        .sort_values(ascending=False)
        .iloc[1:6]
        .index
        .tolist()
    )

    return recommendations

# ----------------------------------------------------
# Button
# ----------------------------------------------------

if st.button("Get Recommendations"):

    recommendations = recommend(selected_product)

    if len(recommendations) == 0:
        st.warning("No recommendations found.")

    else:

        st.success("Top 5 Recommended Products")

        for i, product in enumerate(recommendations, 1):
            st.write(f"**{i}. {product}**")
