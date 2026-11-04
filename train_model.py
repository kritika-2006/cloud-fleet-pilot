import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generate realistic sensor dataset
n_samples = 1000
engine_temp = np.random.uniform(70, 115, n_samples)
vibration_level = np.random.uniform(0.2, 5.0, n_samples)
fuel_consumption = np.random.uniform(5.0, 20.0, n_samples)
speed = np.random.uniform(20, 100, n_samples)

# Define clear rules for failure risk (Engine temp > 96 or Vibration > 3.2 = High Risk)
failure_risk = []
for t, v in zip(engine_temp, vibration_level):
    if t > 96 or v > 3.2:
        risk = 1 if np.random.random() < 0.90 else 0  # 90% chance of failure under stress
    else:
        risk = 1 if np.random.random() < 0.03 else 0  # 3% random failure otherwise
    failure_risk.append(risk)

df = pd.DataFrame({
    'Engine_Temp': engine_temp,
    'Vibration_Level': vibration_level,
    'Fuel_Consumption': fuel_consumption,
    'Speed': speed,
    'Failure_Risk': failure_risk
})

# Save the dataset locally
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'vehicle_sensor_data.csv')
df.to_csv(csv_path, index=False)
print("Dataset generated and saved to:", csv_path)

# 2. Train the Random Forest Model
X = df[['Engine_Temp', 'Vibration_Level', 'Fuel_Consumption', 'Speed']]
y = df['Failure_Risk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 3. Save the trained model file (.pkl)
model_path = os.path.join(current_dir, 'fleet_model.pkl')
joblib.dump(model, model_path)
print("Model trained and saved to:", model_path)