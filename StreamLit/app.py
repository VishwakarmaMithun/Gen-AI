import streamlit as st
st.write("Hello, this is a simple chat interface using Streamlit and streamlit_chat!")
st.title("Chat with AI")
st.header("This is a simple chat interface using Streamlit and streamlit_chat!")    
st.subheader("You can chat with the AI by typing your message in the input box below and pressing Enter.")
st.text("Note: This is a simple demo and may not reflect the full capabilities of the AI model.")
 
if st.button("Click me to see a message"):
    st.write("You clicked the button!")
if st.checkbox("Check me out!"):
    st.write("You checked the box!")