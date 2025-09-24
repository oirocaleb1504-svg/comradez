import streamlit as st
import pandas as pd
import random
from datetime import datetime

# -------------------------------
# Custom CSS for Theme + Wallpaper
# -------------------------------
st.markdown("""
    <style>
       <script>
  const ctx = document.getElementById('stockChart').getContext('2d');
  const stockChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Chips', 'Cookies', 'Soda', 'Juice', 'Chocolate'],
      datasets: [{
        label: 'Stock Quantity',
        data: [12, 19, 8, 15, 10], // replace with your actual stock numbers
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255, 206, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(153, 102, 255, 0.6)'
        ],
        borderColor: 'rgba(0,0,0,0.8)',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
</script>

        body {
            color: #000000; /* black text for readability */
        }
        .stApp {
            background: url("data:image/jpeg;base64,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.png");
            background-size: cover;
            background-repeat: repeat;
            background-attachment: fixed;
            color: #000000; /* ensure text inside remains black */
        }
        h1, h2, h3, h4 {
            font-family: 'Trebuchet MS', 'Comic Sans MS', sans-serif;
            color: #ff6600; /* bright orange headings */
        }
        .big-title {
            font-size: 48px !important;
            font-weight: bold;
            color: #ff6600;
            text-align: center;
            text-shadow: 1px 1px 2px #fff; /* subtle glow for contrast */
        }
        .block-container {
            background-color: rgba(255, 245, 235, 0.9); /* peachy semi-transparent tiles */
            border-radius: 15px;
            padding: 20px;
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


