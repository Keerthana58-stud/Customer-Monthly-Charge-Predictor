import streamlit as st
import requests

st.title("Customer Monthly Charge Predictor")

age = st.number_input("Enter Age", min_value=18, max_value=100, step=1)
tenure = st.number_input("Enter Tenure (in months)", min_value=0, step=1)
services = st.multiselect("Select Services", ["Phone", "Internet", "TV", "Streaming", "Cloud"])

if st.button("Predict Monthly Charge"):
    input_data = {
        "age": age,
        "tenure": tenure,
        "services": services
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict/", json=input_data)
        if response.status_code == 200:
            prediction = response.json()["predicted_monthly_charge"]
            st.success(f"Predicted Monthly Charge: ₹{prediction}")
        else:
            st.error(f"Error from server: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to FastAPI server: {e}")
