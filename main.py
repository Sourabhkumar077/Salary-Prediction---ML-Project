import streamlit as st
import pickle
import numpy as np

# Page configuration
st.set_page_config(page_title="Salary Prediction App", page_icon="💼")

# Title
st.title("💼 Salary Prediction App")
st.write("Enter your years of experience to predict your salary.")

# Load the model
try:
    with open("salary_model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("❌ Model file 'salary_model.pkl' not found. Please make sure it's in the same folder as this app.")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading the model: {e}")
    st.stop()

# User input
exp = st.number_input("Enter your years of experience:", min_value=0.0, max_value=25.0, step=0.5)

# Predict button
if st.button("Predict Salary"):
    try:
        prediction = model.predict(np.array([[exp]]))
        predicted_salary = prediction[0]
        st.success(f"💰 Predicted Salary: ₹ {predicted_salary:,.2f}")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")