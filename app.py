# app.py

import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained model
with open("loan_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Loan Approval Prediction System")
st.write("Enter applicant details to predict loan approval status.")

# User input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.selectbox("Loan Amount Term", [360, 180, 240, 120])
credit_history = st.selectbox("Credit History", [1, 0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encoding inputs manually (must match training encoding)
input_data = np.array([[
    1 if gender == "Male" else 0,
    1 if married == "Yes" else 0,
    3 if dependents == "3+" else int(dependents),
    1 if education == "Graduate" else 0,
    1 if self_employed == "Yes" else 0,
    applicant_income,
    coapplicant_income,
    loan_amount,
    loan_term,
    credit_history,
    2 if property_area == "Urban" else 1 if property_area == "Semiurban" else 0
]])

# Prediction
if st.button("Predict Loan Approval"):
    import pandas as pd

    columns = [
        "Gender", "Married", "Dependents", "Education", "Self_Employed",
        "ApplicantIncome", "CoapplicantIncome", "LoanAmount",
        "Loan_Amount_Term", "Credit_History", "Property_Area"
    ]

    input_df = pd.DataFrame(input_data, columns=columns)

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("Loan Approved ")
    else:
        st.error("Loan Not Approved ")
