import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Set the correct absolute path for cloud and local environments
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, 'vehicle_sensor_data.csv')
model_path = os.path.join(current_dir, 'fleet_model.pkl')

print('Loading dataset from:', csv_path)

# Load the vehicle sensor dataset safely
df = pd.read_csv(csv_path)

# Define features and target variable (adjust column names based on your dataset schema)
# Assuming 'failure_risk' is the target column
if 'failure_risk' in df.columns:
    X = df.drop(columns=['failure_risk'])
    y = df['failure_risk']
else:
    # Fallback to standard split if columns differ
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize and train the predictive model
print('Training the predictive fleet maintenance model...')
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model to disk using the secure path
joblib.dump(model, model_path)
print(f'Model successfully trained and saved to: {model_path}')