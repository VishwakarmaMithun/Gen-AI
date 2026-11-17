import streamlit as st

st.title("Price & Discount Calculator")

# 1. Takes product price (number input)
price = st.number_input("Enter Original Price:", min_value=0.0, value=1000.0, step=10.0)

# 2. Takes discount percentage (slider from 0 to 50%)
discount = st.slider("Select Discount Percentage (%):", min_value=0, max_value=50, value=10)

# 3. On button click, calculates discounted price
if st.button("Calculate Discount"):
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    # 4. Shows result using st.success()
    st.success(f"Final Price: {final_price:.2f} (You saved {discount_amount:.2f}!)")

    # Extra (optional): Show comparison in a small table using a list of lists
    comparison_data = [
        ["Before", "After"],
        [f"{price:.2f}", f"{final_price:.2f}"]
    ]
    st.table(comparison_data)