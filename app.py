import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('churn_model.pkl', 'rb'))

st.title("💸 Customer Churn Prediction")

st.write("Enter customer details:")

# Inputs
tenure = st.number_input("Tenure", min_value=0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

contract = st.selectbox("Contract", [0, 1, 2])
payment_method = st.selectbox("Payment Method", [0, 1, 2, 3])
internet_service = st.selectbox("Internet Service", [0, 1, 2])
tech_support = st.selectbox("Tech Support", [0, 1])
online_security = st.selectbox("Online Security", [0, 1])

support_calls = st.number_input("Support Calls", min_value=0)

# Prediction
if st.button("Predict"):
    features = np.array([[tenure, monthly_charges, total_charges,
                          contract, payment_method, internet_service,
                          tech_support, online_security, support_calls]])

    prediction = model.predict(features)

    if prediction[0] == 0:
        st.success('Customer is NOT likely to leave 😊')
    else:
        st.error('Customer is likely to leave ⚠️')