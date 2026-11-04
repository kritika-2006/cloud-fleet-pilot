import csv
import random

# Set random seed for consistency
random.seed(42)

n_samples = 1500
filename = "vehicle_sensor_data.csv"

# Open CSV file to write simulated telemetry data
with open(filename, mode="w", newline="") as file:
  writer = csv.writer(file)
  # Write header
  writer.writerow(
      [
          "Engine_Temp",
          "Vibration_Level",
          "Fuel_Consumption",
          "Speed",
          "Failure_Risk",
      ]
  )

  for _ in range(n_samples):
    engine_temp = round(random.uniform(70.0, 115.0), 2)
    vibration = round(random.uniform(0.5, 5.5), 2)
    fuel = round(random.uniform(5.0, 20.0), 2)
    speed = round(random.uniform(20.0, 100.0), 2)

    # Rule-based logic for failure risk (1 = High Risk, 0 = Normal)
    if engine_temp > 100 and vibration > 3.5:
      failure_risk = 1
    else:
      failure_risk = 0

    writer.writerow([engine_temp, vibration, fuel, speed, failure_risk])

print(
    "Dataset generated successfully and saved as"
    f" '{filename}' with {n_samples} records using pure Python!"
)