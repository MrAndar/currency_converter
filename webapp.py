import streamlit as st

# Creating widgets for User interface
st.title("Currency Converter")
st.text_input("Enter amount:")
st.radio("Select currency:", ["GBP to USD", "USD to GBP", "GBP to JPY", "JPY to GBP"])

# two columns - text and converted amount
col1, col2 = st.columns([1, 1])

# Adding content to each column
with col1:
    st.text("Converted amount: ")
with col2:
    st.text("900")

