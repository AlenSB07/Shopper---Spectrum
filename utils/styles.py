import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* Background */
    .stApp{
        background-color:#F5F7FA;
    }

    /* Main title */
    h1{
        color:#0F172A;
        font-weight:700;
    }

    h2,h3{
        color:#1E3A8A;
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background:#1E293B;
    }

    section[data-testid="stSidebar"] *{
        color:white;
    }

    /* KPI Cards */
    .metric-card{
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0px 3px 12px rgba(0,0,0,0.12);
        text-align:center;
        transition:0.3s;
    }

    .metric-card:hover{
        transform:translateY(-5px);
    }

    .metric-title{
        font-size:18px;
        color:#6B7280;
        font-weight:600;
    }

    .metric-value{
        font-size:32px;
        color:#2563EB;
        font-weight:bold;
    }

    /* Buttons */
    .stButton>button{
        width:100%;
        border-radius:10px;
        background:#2563EB;
        color:white;
        border:none;
        font-weight:bold;
        height:45px;
    }

    .stButton>button:hover{
        background:#1D4ED8;
    }

    /* Tables */
    .stDataFrame{
        border-radius:10px;
    }

    </style>
    """, unsafe_allow_html=True)