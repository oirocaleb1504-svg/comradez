import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# -----------------------------
# Mock Sales Data Generator
# -----------------------------
def generate_mock_data():
    products = ["Coke", "Water", "Chips", "Energy Drink"]
    data = []
    for p in products:
        daily_sales = np.random.randint(5, 25)  # simulate daily sales
        stock_left = np.random.randint(10, 50)
        data.append([p, daily_sales, stock_left])
    df = pd.DataFrame(data, columns=["Product", "Sales_Today", "Stock_Left"])
    return df

# -----------------------------
# Inventory & Restock Logic
# -----------------------------
def check_restock(df):
    alerts = []
    for _, row in df.iterrows():
        days_left = row["Stock_Left"] / max(row["Sales_Today"], 1)
        if days_left < 3:
            alerts.append(f"⚠️ **Restock {row['Product']} in {days_left:.1f} days**")
    return alerts

# -----------------------------
# Pricing Suggestions
# -----------------------------
def pricing_suggestions(df):
    suggestions = []
    for _, row in df.iterrows():
        if row["Sales_Today"] > 20:
            suggestions.append(f"⬆️ Increase price of **{row['Product']}** by 5% (high demand)")
        elif row["Sales_Today"] < 8:
            suggestions.append(f"⬇️ Decrease price of **{row['Product']}** by 5% (low demand)")
    return suggestions

# -----------------------------
# Streamlit Web App
# -----------------------------
st.markdown(
    "<h1 style='color:#FF7300; font-family:cursive; text-align:center;'>🍊 Comradez Vending Report</h1>", 
    unsafe_allow_html=True
)

st.markdown(
    "<p style='color:#FFFFFF; font-size:18px; text-align:center;'>Smart automation for the future of vending 🍹</p>", 
    unsafe_allow_html=True
)

# Generate mock data
df = generate_mock_data()

# Display table
st.subheader("📊 Today's Sales & Stock")
st.dataframe(df.style.background_gradient(cmap="Oranges"))

# Restock Alerts
st.subheader("🛒 Restock Alerts")
alerts = check_restock(df)
if alerts:
    for a in alerts:
        st.warning(a)
else:
    st.success("✅ All stock levels are healthy.")

# Pricing Suggestions
st.subheader("💸 Pricing Suggestions")
prices = pricing_suggestions(df)
if prices:
    for p in prices:
        st.info(p)
else:
    st.success("✅ Pricing is optimal today.")

# Daily Report Summary
st.subheader("📑 Report Summary")
st.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
st.write(f"**Total Items Sold Today:** {df['Sales_Today'].sum()}")
st.write(f"**Total Revenue (est.):** KSh {df['Sales_Today'].sum() * 100}")
