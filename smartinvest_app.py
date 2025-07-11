import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="SmartInvest Assistant", layout="centered")

st.markdown("""
    <style>
    body {
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background-color: #f4faff;
    }
    .css-1d391kg {background-color: #f4faff;}
    .stButton>button {
        background-color: #0066cc;
        color: white;
        border-radius: 5px;
        font-size: 16px;
        padding: 0.5em 1.5em;
    }
    .stButton>button:hover {
        background-color: #004999;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💸 SmartInvest Assistant")
st.markdown("A simple tool to help new investors understand their risk and get AI-powered suggestions.")

st.header("Step 1: Know Yourself")
experience = st.selectbox("Your investing experience level:", ["Beginner", "Intermediate", "Experienced"])
risk = st.selectbox("Your risk tolerance:", ["Low", "Medium", "High"])
amount = st.slider("How much are you thinking of investing?", min_value=500, max_value=100000, step=500)

st.header("Step 2: Get a Suggestion")
if st.button("Suggest My Portfolio"):
    if risk == "Low":
        suggestion = {
            "Strategy": "Defensive + Income",
            "Recommended Portfolio": ["VTI (40%)", "BND (40%)", "VNQ (20%)"],
            "Style": "Stable, low-volatility, income-focused"
        }
    elif risk == "Medium":
        suggestion = {
            "Strategy": "Balanced Growth",
            "Recommended Portfolio": ["VTI (60%)", "VXUS (20%)", "BND (20%)"],
            "Style": "Moderate growth with diversification"
        }
    else:
        suggestion = {
            "Strategy": "Aggressive Growth",
            "Recommended Portfolio": ["QQQ (50%)", "ARKK (30%)", "VTI (20%)"],
            "Style": "High-risk, tech-forward, innovation focused"
        }
    st.subheader("📊 Your Suggested Portfolio")
    st.write(f"**Strategy:** {suggestion['Strategy']}")
    st.write(f"**Allocation:** {', '.join(suggestion['Recommended Portfolio'])}")
    st.write(f"**Style:** {suggestion['Style']}")

st.header("Step 3: Visualize a Sample Investment")
ticker = st.text_input("Enter a stock or ETF symbol (e.g., AAPL, VTI, QQQ):", value="AAPL")

if st.button("Run Simulation"):
    try:
        df = yf.download(ticker, start="2022-01-01")
        entry_price = df['Close'][0]
        final_price = df['Close'][-1]
        return_pct = ((final_price - entry_price) / entry_price) * 100
        st.metric(label="Investment Return", value=f"{return_pct:.2f} %")
        st.line_chart(df['Close'])
    except Exception as e:
        st.error("Unable to fetch data. Please try a different symbol.")
Add smartinvest_app.py
