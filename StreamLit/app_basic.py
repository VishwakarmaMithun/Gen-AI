import streamlit as st
st.title("welcome to the Streamlit app!")
name = st.text_input("Enter your name:")

if st.button("Greet me!"):
    st.write(f"Hello, {name}! Welcome to the Streamlit app!")
else:
    st.write("Please enter your name and click the button to be greeted.")

