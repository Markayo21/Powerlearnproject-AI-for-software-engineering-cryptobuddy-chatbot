# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load your data
inventory = pd.read_csv("inventory.csv")
suppliers = pd.read_csv("suppliers.csv")
price_history = pd.read_csv("price_history.csv")

# Normalize column names: lowercase, strip spaces, replace spaces with underscores
inventory.columns = inventory.columns.str.strip().str.lower().str.replace(" ", "_")
suppliers.columns = suppliers.columns.str.strip().str.lower().str.replace(" ", "_")
price_history.columns = price_history.columns.str.strip().str.lower().str.replace(" ", "_")

# Show original columns (optional debugging help)
st.write("Inventory columns:", inventory.columns.tolist())
st.write("Suppliers columns:", suppliers.columns.tolist())

# Merge inventory with supplier cost data
if "item" in inventory.columns and "item" in suppliers.columns:
    merged_data = pd.merge(inventory, suppliers, on="item")
else:
    st.error("❌ 'item' column missing in one of the datasets!")
    st.stop()

# Check necessary columns before calculating profit margin
if "selling_price" in merged_data.columns and "cost_price" in merged_data.columns:
    merged_data["profit_margin"] = merged_data["selling_price"] - merged_data["cost_price"]
else:
    st.error("❌ 'selling_price' or 'cost_price' column missing in merged data!")
    st.stop()

# Show merged columns
st.write("Merged Columns:", merged_data.columns.tolist())

# Sidebar Filters
st.sidebar.title("Filter Items")
category_filter = st.sidebar.selectbox("Select Category", ["All"] + list(merged_data["category"].unique()))
min_margin = st.sidebar.slider("Minimum Profit Margin", 0, int(merged_data["profit_margin"].max()), 0)

# Apply filters
filtered_data = merged_data.copy()
if category_filter != "All":
    filtered_data = filtered_data[filtered_data["category"] == category_filter]
filtered_data = filtered_data[filtered_data["profit_margin"] >= min_margin]

# Page Title
st.title("📊 Retail Price Analysis Dashboard")

# Section 1: Profit Margin Chart (Plotly)
st.subheader("📊 Profit Margin per Item")
bar_chart = px.bar(
    filtered_data,
    x="item",
    y="profit_margin",
    color="category",
    title="Profit Margin by Item",
    labels={"profit_margin": "Profit Margin", "item": "Item"},
    height=400
)
st.plotly_chart(bar_chart)

# Section 2: Pie Chart (Category Distribution)
st.subheader("🥧 Stock Distribution by Category")
category_summary = merged_data.groupby("category")["stock"].sum().reset_index()
pie_chart = px.pie(
    category_summary,
    names="category",
    values="stock",
    title="Total Stock by Category"
)
st.plotly_chart(pie_chart)

# Section 3: Inventory Overview
st.subheader("📋 Inventory Overview")
st.dataframe(filtered_data[["item", "category", "stock", "selling_price", "cost_price", "profit_margin"]])

# Section 4: Price Trend Chart
st.subheader("📈 Price Trends Over Time")
if "item" in price_history.columns and "price" in price_history.columns:
    selected_item = st.selectbox("Select an item to view price trend", price_history["item"].unique())
    item_history = price_history[price_history["item"] == selected_item]
    plt.figure(figsize=(10, 4))
    plt.plot(item_history["month"], item_history["price"], marker="o", color="green")
    plt.title(f"Price Trend: {selected_item}")
    plt.xlabel("Month")
    plt.ylabel("Price")
    plt.grid(True)
    st.pyplot(plt)
else:
    st.warning("⚠️ Price history file is missing required columns ('item' and/or 'price').")

# Section 5: Recommendations
st.subheader("💡 Suggested Actions")

low_stock = merged_data[merged_data["stock"] < 10]
low_margin = merged_data[merged_data["profit_margin"] < 10]

st.markdown("🔴 **Low Stock Alerts (Stock < 10)**")
st.dataframe(low_stock[["item", "stock", "selling_price"]])

st.markdown("🟠 **Low Profit Margin Items (Margin < 10)**")
st.dataframe(low_margin[["item", "selling_price", "cost_price", "profit_margin"]])



