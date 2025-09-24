import streamlit as st
import pandas as pd
import random
from datetime import datetime

# -------------------------------
# Custom CSS for Theme
# -------------------------------
st.markdown("""
    <style>
        body {
            background-color: #fff5eb; /* soft peach background */
            color: #222;
        }
        .stApp {
            background-color: #fff5eb;
        }
        h1, h2, h3, h4 {
            font-family: 'Trebuchet MS', 'Comic Sans MS', sans-serif;
            color: #ff6600; /* bright orange */
        }
        .big-title {
            font-size: 48px !important;
            font-weight: bold;
            color: #ff6600;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Title & Subtitle
# -------------------------------
st.markdown("<h1 class='big-title'>🍊 Comradez Vending Report</h1>", unsafe_allow_html=True)
st.markdown("### Smart automation for the future of vending 🥤")

# -------------------------------
# Mock Data Generator
# -------------------------------
def generate_mock_data():
    products = ["Soda", "Water", "Juice", "Chips", "Candy"]
    sales = [random.randint(10, 100) for _ in products]
    stock = [random.randint(20, 200) for _ in products]
    return pd.DataFrame({
        "Product": products,
        "Sales Today": sales,
        "Stock Remaining": stock
    })

# -------------------------------
# Today's Report
# -------------------------------
st.header("📊 Today's Sales & Stock")
df = generate_mock_data()
st.dataframe(df, use_container_width=True)

# -------------------------------
# Insights
# -------------------------------
st.header("🔎 Insights")
best_seller = df.loc[df["Sales Today"].idxmax()]["Product"]
low_stock = df.loc[df["Stock Remaining"].idxmin()]["Product"]

st.success(f"🔥 Best Seller Today: **{best_seller}**")
st.warning(f"⚠️ Low Stock Alert: **{low_stock}** — restock soon!")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption(f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Comradez Vending Automation 🍊")
