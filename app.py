import streamlit as st
import pandas as pd
import random
from datetime import datetime
import matplotlib.pyplot as plt

# -------------------------------
# Custom CSS for Fanta-inspired Theme
# -------------------------------
st.markdown("""
    <style>
        body {
            color: #000000; /* Black text for readability */
        }
        .stApp {
            background: url("https://i.ibb.co/W5KzPzj/snack-pattern.png");
            background-size: 150px 150px;
            background-repeat: repeat;
            background-attachment: fixed;
        }
        h1, h2, h3, h4 {
            font-family: 'Baloo 2', cursive;
            color: #ff6600; /* Bright Fanta orange */
        }
        .big-title {
            font-size: 50px !important;
            font-weight: bold;
            color: #ff6600;
            text-align: center;
            text-shadow: 2px 2px #fff;
        }
        .block-container {
            background-color: rgba(255, 230, 204, 0.9); /* Fanta peach */
            border-radius: 15px;
            padding: 20px;
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# -------------------------------
# Title & Subtitle
# -------------------------------
st.markdown("<h1 class='big-title'>🍊 Comradez Vending Report</h1>", unsafe_allow_html=True)
st.markdown("### Automated snack vending insights with a Fanta vibe 🥤")

# -------------------------------
# Mock Data Generator
# -------------------------------
def generate_mock_data():
    products = ["Soda", "Water", "Juice", "Chips", "Candy", "Chocolate"]
    sales = [random.randint(10, 100) for _ in products]
    stock = [random.randint(20, 200) for _ in products]
    return pd.DataFrame({
        "Product": products,
        "Sales Today": sales,
        "Stock Remaining": stock
    })

# -------------------------------
# Editable Inventory Section
# -------------------------------
st.header("✏️ Update Inventory")
with st.form("inventory_form"):
    product_name = st.text_input("Enter product name:")
    qty_bought = st.number_input("Enter quantity bought:", min_value=0, step=1)
    submitted = st.form_submit_button("Add to Inventory")

if submitted and product_name:
    st.success(f"✅ {qty_bought} units of **{product_name}** added to inventory!")

# -------------------------------
# Today's Report
# -------------------------------
st.header("📊 Today's Sales & Stock")
df = generate_mock_data()
st.dataframe(df, use_container_width=True)

# -------------------------------
# Stock Bar Chart
# -------------------------------
st.subheader("📦 Stock Levels (Bar Chart)")
fig, ax = plt.subplots()
ax.bar(df["Product"], df["Stock Remaining"], color="#ff6600")
ax.set_ylabel("Units Remaining")
ax.set_title("Stock by Product")
st.pyplot(fig)

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
