import csv

filename = "vehicle_sensor_data.csv"

# Load dataset using pure Python CSV reader
data = []
with open(filename, mode="r") as file:
  reader = csv.reader(file)
  next(reader)  # Skip header
  for row in reader:
    data.append(
        {
            "Engine_Temp": float(row[0]),
            "Vibration_Level": float(row[1]),
            "Fuel_Consumption": float(row[2]),
            "Speed": float(row[3]),
            "Failure_Risk": int(row[4]),
        }
    )

# Split data into train (80%) and test (20%)
split_idx = int(len(data) * 0.8)
test_data = data[split_idx:]

# Evaluate prediction logic on test set
correct = 0
for row in test_data:
  # Predictive maintenance rule evaluation
  predicted_risk = (
      1 if (row["Engine_Temp"] > 100 and row["Vibration_Level"] > 3.5) else 0
  )
  if predicted_risk == row["Failure_Risk"]:
    correct += 1

accuracy = (correct / len(test_data)) * 100
print("Predictive Maintenance Model Evaluated Successfully!")
print(f"Model Accuracy: {accuracy:.2f}%")