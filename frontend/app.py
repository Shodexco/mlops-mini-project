import streamlit as st
import requests

st.set_page_config(page_title="Gym Churn Predictor", page_icon="🏋️‍♂️")

st.title("Gym Churn Prediction")

st.write(
    "Fill in the customer details below to predict whether they will churn."
)
# Inputs
Near_Location = st.sidebar.selectbox("Near Location", [0, 1])
Promo_friends = st.sidebar.selectbox("Promo Friends", [0, 1])
Contract_period = st.sidebar.slider("Contract Period (months)", 1, 24, 12)
Month_to_end_contract = st.sidebar.slider("Months to End Contract", 0, 23, 6)  # Updated
Lifetime = st.sidebar.slider("Customer Lifetime (months)", 1, 36, 12)           # Updated
Avg_class_frequency_total = st.sidebar.slider("Avg Class Frequency Total", 1.0, 7.0, 3.0)  # Updated
Partner = st.sidebar.selectbox("Partner", [0, 1])

# Predict button
if st.button("Predict Churn"):
    input_data = {
        "Near_Location": Near_Location,
        "Promo_friends": Promo_friends,
        "Contract_period": Contract_period,
        "Month_to_end_contract": Month_to_end_contract,
        "Lifetime": Lifetime,
        "Avg_class_frequency_total": Avg_class_frequency_total,
        "Partner": Partner,
    }

    # Call the FastAPI endpoint
    try:
        response = requests.post("http://fastapi:8000/predict", json=input_data)
        prediction = response.json().get("Churn_Prediction")
        
        if prediction == 1:
            st.error("⚠️ This customer is likely to churn!")
        else:
            st.success("✅ This customer is not likely to churn.")
    except:
        st.error("Failed to connect to the API. Make sure FastAPI server is running.")