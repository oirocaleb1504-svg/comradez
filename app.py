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
            background-image: url("https://i.ibb.co/6X0bLgL/snacks-pattern.jpg");
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
