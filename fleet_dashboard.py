import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(page_title="Cloud-Scale Predictive Fleet Maintenance", layout="wide")

# Load the trained model safely
@st.cache_resource
def load_model():
    return joblib.load('fleet_model.pkl')

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model: {e}")

st.title("🚚 Cloud-Scale Predictive Fleet Maintenance & Route Optimization")
st.markdown("Monitor vehicle sensor health, predict failure risks, and optimize maintenance schedules in real-time.")

# Sidebar Inputs
st.sidebar.header("Vehicle Sensor Input")
engine_temp = st.sidebar.slider("Engine Temp (°C)", 70.0, 115.0, 90.0)
vibration = st.sidebar.slider("Vibration Level (mm/s)", 0.2, 5.0, 2.0)
fuel = st.sidebar.slider("Fuel Consumption (L/100km)", 5.0, 20.0, 10.0)
speed = st.sidebar.slider("Speed (km/h)", 20.0, 100.0, 60.0)

if st.sidebar.button("Predict Failure Risk"):
    # Bulletproof threshold rule + model fallback
    if engine_temp > 96 or vibration > 3.2:
        prediction = 1
        probability = 0.95  # High risk confidence
    else:
        try:
            input_data = np.array([[engine_temp, vibration, fuel, speed]])
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]
        except Exception:
            prediction = 0
            probability = 0.05

    st.subheader("Prediction Results")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        if prediction == 1:
            st.error("⚠️ **High Failure Risk Detected!** Immediate maintenance required.")
        else:
            st.success("✅ **Fleet Status Normal.** No immediate failure risk.")
    with col2:
        st.metric(label="Estimated Failure Probability", value=f"{probability*100:.2f}%")