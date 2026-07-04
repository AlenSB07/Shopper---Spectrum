import streamlit as st
import pandas as pd

st.set_page_config(page_title="Product Recommendation", page_icon="🛒")

st.title("🛒 Product Recommendation")
st.caption("Get similar products based on customer purchase behaviour.")

# -----------------------------
# Load Files
# -----------------------------
@st.cache_data
def load_data():
    similarity_df = pd.read_pickle("models/product_similarity.pkl")
    product_list = pd.read_pickle("models/customer_product.pkl").columns.tolist()
    return similarity_df, product_list


similarity_df, product_list = load_data()

# -----------------------------
# Product Selection
# -----------------------------
selected_product = st.selectbox(
    "Select a Product",
    sorted(product_list)
)

# -----------------------------
# Recommendation Function
# -----------------------------
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

# -----------------------------
# Button
# -----------------------------
if st.button("Get Recommendations"):

    recommendations = recommend(selected_product)

    if recommendations:

        st.success("Top 5 Recommended Products")

        for i, product in enumerate(recommendations, start=1):
            st.markdown(f"**{i}. {product}**")

    else:
        st.error("No recommendations found.")