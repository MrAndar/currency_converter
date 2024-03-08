import streamlit as st
from function import currency_converter

# Creating widgets for User interface
st.title("Currency Converter")
amount = st.text_input("Enter amount:")
currency = st.radio("Select currency:", ["GBP to USD", "USD to GBP", "GBP to JPY", "JPY to GBP"])


if amount:
    try:
        new_amount = currency_converter(float(amount), currency)

        # two columns - text and converted amount
        col1, col2 = st.columns([1, 1])

        # Adding content to each column
        with col1:
            st.text("Converted amount: ")
        with col2:
            st.text(new_amount)
    except ValueError:
        st.info("Amount must be a number.")

print("hello")