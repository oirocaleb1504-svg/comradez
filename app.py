import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- Default Password (can be changed in session) ---
if "password" not in st.session_state:
    st.session_state["password"] = "comradez123"  # default password
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# --- Authentication Page ---
def login():
    st.title("🔐 Secure Login")
    pw_input = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        if pw_input == st.session_state["password"]:
            st.session_state["authenticated"] = True
            st.success("✅ Access Granted")
        else:
            st.error("❌ Wrong Password")

# --- Main App ---
def app():
    # Page Config
    st.set_page_config(page_title="Comradez Vending Report", page_icon="🥤", layout="wide")

    # Custom CSS
    st.markdown("""
        <style>
            .stApp {
                background-image: url("https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2F736x%2F62%2Fe6%2Faf%2F62e6afa541b8a7f36b56e748d01a2f6f.jpg&tbnid=7BpVA-JHw3OZLM&vet=10CAIQxiAoAGoXChMIgPjhhPDwjwMVAAAAAB0AAAAAEAc..i&imgrefurl=https%3A%2F%2Far.pinterest.com%2Fpin%2F573083121337237150%2F&docid=v-Kch5hifAPGBM&w=734&h=306&itg=1&q=dark%20images%20for%20websites&ved=0CAIQxiAoAGoXChMIgPjhhPDwjwMVAAAAAB0AAAAAEAc");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
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
            .tile {
                background-color: #FFDAB9;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.15);
                text-align: center;
                font-size: 20px;
                font-weight: bold;
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title & Slogan
    st.markdown('<div class="main-title">Comradez Vending Report</div>', unsafe_allow_html=True)
    st.markdown('<div class="slogan">*Where snacking meets innovation*</div>', unsafe_allow_html=True)

    # --- Inventory Management ---
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

    # Download Inventory
    if not st.session_state["inventory"].empty:
        csv_inventory = st.session_state["inventory"].to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Inventory Report (CSV)", csv_inventory, "inventory_report.csv", "text/csv")

    # --- Sales Report ---
    st.subheader("📊 Sales Report")
    data = pd.DataFrame({
        "Product": ["Soda", "Chips", "Candy", "Water", "Juice"],
        "Units Sold": np.random.randint(20, 100, 5),
        "Revenue (KSh)": np.random.randint(500, 3000, 5)
    })

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="tile">Total Sales<br>{data["Units Sold"].sum()}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="tile">Total Revenue<br>KSh {data["Revenue (KSh)"].sum()}</div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="tile">Top Product<br>{data.loc[data["Units Sold"].idxmax(), "Product"]}</div>', unsafe_allow_html=True)

    st.table(data)

    # Download Sales Report
    csv_sales = data.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Sales Report (CSV)", csv_sales, "sales_report.csv", "text/csv")

    # --- Change Password Section ---
    st.subheader("🔑 Change Password")
    current_pw = st.text_input("Enter current password", type="password")
    new_pw = st.text_input("Enter new password", type="password")
    confirm_pw = st.text_input("Confirm new password", type="password")

    if st.button("Update Password"):
        if current_pw == st.session_state["password"]:
            if new_pw == confirm_pw and new_pw.strip() != "":
                st.session_state["password"] = new_pw
                st.success("✅ Password updated successfully!")
            else:
                st.error("❌ New passwords do not match or are empty.")
        else:
            st.error("❌ Current password is incorrect.")
            

# --- Gatekeeper ---
if not st.session_state["authenticated"]:
    login()
else:
    app()
