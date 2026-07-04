import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.title("📊 Business Dashboard")
st.caption("Analyze customer purchases and business performance")

df = load_data()

# -------------------------
# Sidebar Filters
# -------------------------

st.sidebar.header("Dashboard Filters")

country = st.sidebar.multiselect(
    "Select Country",
    sorted(df["Country"].unique()),
    default=sorted(df["Country"].unique())
)

month = st.sidebar.multiselect(
    "Select Month",
    sorted(df["Month"].unique()),
    default=sorted(df["Month"].unique())
)

filtered_df = df[
    (df["Country"].isin(country)) &
    (df["Month"].isin(month))
]

# -------------------------
# KPIs
# -------------------------

customers = filtered_df["CustomerID"].nunique()
products = filtered_df["Description"].nunique()
orders = filtered_df["InvoiceNo"].nunique()
revenue = filtered_df["TotalPrice"].sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("👥 Customers", f"{customers:,}")
c2.metric("📦 Products", f"{products:,}")
c3.metric("🧾 Orders", f"{orders:,}")
c4.metric("💰 Revenue", f"£{revenue:,.0f}")

st.divider()

# -------------------------
# Charts
# -------------------------

left, right = st.columns(2)

top_products = (
    filtered_df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(
    top_products,
    x="Quantity",
    y="Description",
    orientation="h",
    color="Quantity",
    title="Top 10 Selling Products"
)

left.plotly_chart(fig1, use_container_width=True)

top_country = (
    filtered_df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    top_country,
    x="Country",
    y="TotalPrice",
    color="TotalPrice",
    title="Revenue by Country"
)

right.plotly_chart(fig2, use_container_width=True)

# -------------------------
# Monthly Revenue
# -------------------------

# -------------------------
# Monthly Revenue Trend
# -------------------------

monthly = (
    filtered_df.groupby("Month", as_index=False)["TotalPrice"]
    .sum()
)

# Since Month is already in YYYY-MM format,
# simply sort it chronologically.
monthly = monthly.sort_values("Month")

fig3 = px.line(
    monthly,
    x="Month",
    y="TotalPrice",
    markers=True,
    title="📈 Monthly Revenue Trend"
)

fig3.update_layout(
    xaxis_title="Month",
    yaxis_title="Revenue (£)",
    hovermode="x unified"
)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------
# Business Summary
# -------------------------

st.subheader("📌 Business Summary")

summary1, summary2 = st.columns(2)

summary1.info(f"""
### Key Metrics

- Customers : **{customers:,}**
- Orders : **{orders:,}**
- Products : **{products:,}**
""")

summary2.success(f"""
### Revenue

**£{revenue:,.2f}**

Current filters applied successfully.
""")

# -------------------------
# Recent Transactions
# -------------------------

st.subheader("🧾 Recent Transactions")

st.dataframe(
    filtered_df.tail(15),
    use_container_width=True
)