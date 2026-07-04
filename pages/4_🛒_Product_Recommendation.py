import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Product Recommendation", page_icon="🛒")

st.title("🛒 Product Recommendation")
st.caption("Recommend products based on customer purchase history")

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("clean_online_retail.csv")

    df = df.dropna(subset=["CustomerID", "Description"])

    df["CustomerID"] = df["CustomerID"].astype(str)

    return df


df = load_data()

# ---------------------------------------------------
# Build Recommendation Model
# ---------------------------------------------------

@st.cache_resource
def build_similarity(df):

    customer_product = pd.pivot_table(
        df,
        index="CustomerID",
        columns="Description",
        values="Quantity",
        aggfunc="sum",
        fill_value=0
    )

    product_matrix = customer_product.T

    similarity = cosine_similarity(product_matrix)

    similarity_df = pd.DataFrame(
        similarity,
        index=product_matrix.index,
        columns=product_matrix.index
    )

    return similarity_df


with st.spinner("Building recommendation model... (First run may take 20-40 seconds)"):

    similarity_df = build_similarity(df)

# ---------------------------------------------------
# Product Selection
# ---------------------------------------------------

products = sorted(similarity_df.index.tolist())

selected_product = st.selectbox(
    "Select a Product",
    products
)

# ---------------------------------------------------
# Recommend
# ---------------------------------------------------

def recommend(product):

    similar_products = (
        similarity_df[product]
        .sort_values(ascending=False)
        .drop(product)
        .head(5)
    )

    return similar_products.index.tolist()

# ---------------------------------------------------
# Button
# ---------------------------------------------------

if st.button("Get Recommendations"):

    recommendations = recommend(selected_product)

    st.success("Top 5 Recommended Products")

    for i, item in enumerate(recommendations, start=1):
        st.write(f"**{i}. {item}**")
