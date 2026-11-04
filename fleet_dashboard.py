import os
import joblib
import pandas as pd
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Cloud-Scale Predictive Fleet Maintenance",
    page_icon="🚚",
    layout="wide"
)

# Safe pathing for cloud and local environments
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'fleet_model.pkl')
data_path = os.path.join(BASE_DIR, 'vehicle_sensor_data.csv')

# Load model and dataset safely with caching and error handling
@st.cache_resource
def load_fleet_assets():
    try:
        model = joblib.load(model_path)
        df = pd.read_csv(data_path)
        return model, df
    except Exception as e:
        st.error(f"Error loading model or data: {e}")
        return None, None

model, df = load_fleet_assets()

st.title("🚚 Cloud-Scale Predictive Fleet Maintenance & Route Optimization")
st.markdown("Monitor vehicle sensor health, predict failure risks, and optimize maintenance schedules in real-time.")

if model is not None and df is not None:
    # Sidebar for live sensor inputs
    st.sidebar.header("🔍 Vehicle Sensor Input")
    engine_temp = st.sidebar.slider("Engine Temp (°C)", float(df['Engine_Temp'].min()), float(df['Engine_Temp'].max()), float(df['Engine_Temp'].mean()))
    vibration = st.sidebar.slider("Vibration Level (mm/s)", float(df['Vibration_Level'].min()), float(df['Vibration_Level'].max()), float(df['Vibration_Level'].mean()))
    fuel = st.sidebar.slider("Fuel Consumption (L/100km)", float(df['Fuel_Consumption'].min()), float(df['Fuel_Consumption'].max()), float(df['Fuel_Consumption'].mean()))
    speed = st.sidebar.slider("Speed (km/h)", float(df['Speed'].min()), float(df['Speed'].max()), float(df['Speed'].mean()))

    # Prediction button & logic
    if st.sidebar.button("Predict Failure Risk"):
        input_data = pd.DataFrame([[engine_temp, vibration, fuel, speed]], columns=['Engine_Temp', 'Vibration_Level', 'Fuel_Consumption', 'Speed'])
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1] if hasattr(model, "predict_proba") else 0.0

        st.subheader("📊 Prediction Results")
        col1, col2 = st.columns(2)
        with col1:
            if prediction == 1:
                st.error("⚠️ **High Failure Risk Detected!** Immediate maintenance required.")
            else:
                st.success("✅ **Fleet Status Normal.** No immediate failure risk.")
        with col2:
            st.metric("Estimated Failure Probability", f"{probability * 100:.2f}%")

    # Main dataset preview and charts
    st.divider()
    st.subheader("📈 Fleet Sensor Dataset & Analytics")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Engine Temperature vs Vibration Analysis")
    st.scatter_chart(df, x='Engine_Temp', y='Vibration_Level', color='Failure_Risk' if 'Failure_Risk' in df.columns else None)
else:
    st.warning("Please ensure `fleet_model.pkl` and `vehicle_sensor_data.csv` are properly uploaded to your GitHub repository.")