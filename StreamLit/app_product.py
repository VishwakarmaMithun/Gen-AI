import streamlit as st
st.title("Product Management App")
# Sidebar for product details
st.sidebar.header("Add new product")
product_name = st.sidebar.text_input("Product Name:")
product_category = st.sidebar.selectbox("Category:", ["Electronics", "Clothing", "Books", "Home & Kitchen"])    
price = st.sidebar.number_input("Price:", min_value=0.0, value=100.0, step=1.0)
add_click = st.sidebar.button("Add Product")

if add_click:
    if product_name.strip():
        st.success(f"Product '{product_name}' added successfully!")
        st.write(f"Category: {product_category}")
        st.write(f"Price: ${price:.2f}")
    else:
        st.error("Product name cannot be empty. Please enter a valid product name.")
else:
    st.write("Please enter product details in the sidebar and click 'Add Product' to add a new product.")
