import streamlit as st
import pandas as pd

st.title("📈 Business Insights")
st.caption("Key findings generated from the Online Retail dataset")

# -----------------------
# Load Data
# -----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("clean_online_retail.csv")
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    return df

df = load_data()

# Create TotalPrice if it doesn't exist
if "TotalPrice" not in df.columns:
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# -----------------------
# KPIs
# -----------------------


total_revenue = df["TotalPrice"].sum()
total_customers = df["CustomerID"].nunique()
total_orders = df["InvoiceNo"].nunique()
total_products = df["Description"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Revenue", f"£{total_revenue:,.0f}")
col2.metric("👥 Customers", f"{total_customers:,}")
col3.metric("🧾 Orders", f"{total_orders:,}")
col4.metric("📦 Products", f"{total_products:,}")

st.divider()

# -----------------------
# Business Insights
# -----------------------

top_country = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

top_product = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

highest_customer = (
    df.groupby("CustomerID")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

avg_order = total_revenue / total_orders

st.subheader("📌 Key Insights")

st.success(f"""
### 🌍 Top Revenue Country

**{top_country}**

This country contributes the highest overall sales revenue.
""")

st.info(f"""
### 🛒 Best Selling Product

**{top_product}**

This product has the highest quantity sold.
""")

st.warning(f"""
### 👑 Highest Spending Customer

**Customer ID: {int(highest_customer)}**

This customer generated the highest revenue.
""")

st.success(f"""
### 💳 Average Order Value

**£{avg_order:,.2f}**

Average revenue earned per order.
""")

st.divider()

# -----------------------
# Business Recommendations
# -----------------------

st.subheader("💡 Business Recommendations")

st.markdown("""
### 1️⃣ Focus on High Revenue Countries
Increase marketing efforts and inventory for countries contributing the highest revenue.

### 2️⃣ Reward Loyal Customers
Offer loyalty rewards and exclusive promotions to repeat customers.

### 3️⃣ Promote Best Selling Products
Ensure top-selling products remain well stocked and visible.

### 4️⃣ Target At-Risk Customers
Use personalized offers and email campaigns to re-engage inactive customers.

### 5️⃣ Improve Cross-Selling
Recommend related products to increase average basket value.
""")

st.divider()

st.subheader("📄 Dataset Summary")

summary = pd.DataFrame({
    "Metric": [
        "Total Customers",
        "Total Orders",
        "Total Products",
        "Total Revenue"
    ],
    "Value": [
        total_customers,
        total_orders,
        total_products,
        f"£{total_revenue:,.2f}"
    ]
})

st.dataframe(summary, use_container_width=True)