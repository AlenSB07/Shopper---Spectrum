import streamlit as st
import pickle
import numpy as np

st.title("👥 Customer Segmentation")
st.caption("Predict customer segment using trained KMeans model")

# -----------------------------
# Load Model + Scaler
# -----------------------------
with open("models/kmeans_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# -----------------------------
# Input Section
# -----------------------------
st.subheader("Enter Customer RFM Values")

col1, col2, col3 = st.columns(3)

with col1:
    recency = st.number_input("Recency (Days)", min_value=1, max_value=500, value=30)

with col2:
    frequency = st.number_input("Frequency", min_value=1, max_value=1000, value=10)

with col3:
    monetary = st.number_input("Monetary (£)", min_value=1.0, value=500.0)

# -----------------------------
# Prediction Logic
# -----------------------------
if st.button("Predict Customer Segment"):

    # Convert input to array
    data = np.array([[recency, frequency, monetary]])

    # Scale data (IMPORTANT)
    data_scaled = scaler.transform(data)

    # Predict cluster
    cluster = int(kmeans.predict(data_scaled)[0])

    # -----------------------------
    # Cluster Mapping (FIXED LOGIC)
    # -----------------------------
    segment_map = {
        0: {
            "name": "🟢 Regular Customer",
            "desc": "Makes occasional purchases with average spending.",
            "rec": "Offer discounts and personalized promotions."
        },
        1: {
            "name": "🔴 At Risk Customer",
            "desc": "Has not purchased recently and may stop buying.",
            "rec": "Send re-engagement emails and offers."
        },
        2: {
            "name": "👑 VIP Customer",
            "desc": "High-value customer with very high spending & frequency.",
            "rec": "Provide premium rewards and exclusive benefits."
        },
        3: {
            "name": "🔵 Loyal Customer",
            "desc": "Regular repeat customer with good engagement.",
            "rec": "Reward loyalty and encourage retention."
        }
    }

    result = segment_map.get(cluster, segment_map[0])

    # -----------------------------
    # Output UI
    # -----------------------------
    st.success(result["name"])

    st.markdown("### 📋 Customer Description")
    st.write(result["desc"])

    st.markdown("### 💡 Business Recommendation")
    st.info(result["rec"])

    st.markdown("---")

    st.subheader("Input Summary")

    c1, c2, c3 = st.columns(3)
    c1.metric("Recency", recency)
    c2.metric("Frequency", frequency)
    c3.metric("Monetary", f"£{monetary:,.2f}")