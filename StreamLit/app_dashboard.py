import streamlit as st

# 1. Title + Description
st.title("Simple Sales Dashboard")
st.write("Select a month below to view its sales performance and compare across Q1–Q2.")

# 2. Months list & 3. Static dictionary of monthly sales
months = ["January", "February", "March", "April"]
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

# Selectbox for month selection
selected_month = st.selectbox("Select a Month", months)

# 4. Display selected month's sales
st.metric(label=f"{selected_month} Sales", value=f"${sales[selected_month]:,}")

# 5. Display a bar chart
st.subheader("Monthly Sales Overview")
st.bar_chart(list(sales.values()))