import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- Page Config ---
st.set_page_config(
    page_title="Comradez Vending Report",
    page_icon="🥤",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
    <style>
        /* Background wallpaper */
        .stApp {
            background-image: url("data:image/jpeg;base64,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");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        /* Title style */
        .main-title {
            font-size: 48px;
            font-weight: bold;
            color: orange;
            text-align: center;
        }

        .slogan {
            font-size: 20px;
            font-style: italic;
            color: black;
            text-align: center;
            margin-bottom: 20px;
        }

        /* Tiles */
        .tile {
            background-color: #FFDAB9; /* peach */
            padding: 20px;
            border-radius: 20px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.15);
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: black; /* all text in tiles is black */
        }
    </style>
""", unsafe_allow_html=True)

# --- Title + Slogan ---
st.markdown('<div class="main-title">Comradez Vending Report</div>', unsafe_allow_html=True)
st.markdown('<div class="slogan">*Where snacking meets innovation*</div>', unsafe_allow_html=True)

# --- Editable Inventory Section ---
st.subheader("🛒 Inventory Management")
if "inventory" not in st.session_state:
    st.session_state["inventory"] = pd.DataFrame(columns=["Item", "Quantity", "Date Added"])

item = st.text_input("Enter snack name")
qty = st.number_input("Enter quantity", min_value=1, step=1)
if st.button("Add to Inventory"):
    if item.strip() != "":
        new_entry = pd.DataFrame({
            "Item": [item],
            "Quantity": [qty],
            "Date Added": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        })
        st.session_state["inventory"] = pd.concat([st.session_state["inventory"], new_entry], ignore_index=True)
        st.success(f"Added {qty} units of {item} to inventory.")
    else:
        st.warning("Please enter a snack name before adding.")

st.dataframe(st.session_state["inventory"])

# --- Download Inventory CSV ---
if not st.session_state["inventory"].empty:
    csv_inventory = st.session_state["inventory"].to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Inventory Report (CSV)",
        data=csv_inventory,
        file_name="inventory_report.csv",
        mime="text/csv"
    )

# --- Sales Data Simulation ---
st.subheader("📊 Sales Report")
data = pd.DataFrame({
    "Product": ["Soda", "Chips", "Candy", "Water", "Juice"],
    "Units Sold": np.random.randint(20, 100, 5),
    "Revenue (KSh)": np.random.randint(500, 3000, 5)
})

# Display in tiles
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<div class="tile">Total Sales<br>{data["Units Sold"].sum()}</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="tile">Total Revenue<br>KSh {data["Revenue (KSh)"].sum()}</div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="tile">Top Product<br>{data.loc[data["Units Sold"].idxmax(), "Product"]}</div>', unsafe_allow_html=True)

# Table
st.table(data)

# --- Download Sales CSV ---
csv_sales = data.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Download Sales Report (CSV)",
    data=csv_sales,
    file_name="sales_report.csv",
    mime="text/csv"
)

