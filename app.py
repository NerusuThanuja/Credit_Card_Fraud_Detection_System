import streamlit as st
import pandas as pd
from fraud import predict_fraud

st.set_page_config(page_title="Credit Card Fraud Detection")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details below")

feauture_count=29

# Input field
input_text = st.text_area(
    "Enter values separated by commas",
    placeholder=f"Enter {feature_count} numeric values"
)

if st.button("Predict"):
    try:
        values = list(map(float, input_text.split(",")))

        if len(values) != feature_count:
            st.error(f"Please enter exactly {feature_count} values")
        else:
            result = predict_fraud(values)

            if result == 1:
                st.error("🚨 Fraudulent Transaction")
            else:
                st.success("✅ Legitimate Transaction")

    except Exception as e:
        st.error(f"Error: {e}")