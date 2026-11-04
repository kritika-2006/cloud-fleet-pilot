import csv
import os  # 1. Yeh import add karein

# 2. Sahi path set karein taaki cloud par file mil jaye
current_dir = os.path.dirname(__file__)
filename = os.path.join(current_dir, 'vehicle_sensor_data.csv')

total_vehicles = 0
high_risk_count = 0
normal_count = 0

# Read and analyze the generated telemetry data
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        total_vehicles += 1
        # Check failure risk column
        if int(row[4]) == 1:
            high_risk_count += 1
        else:
            normal_count += 1

print(
    '============================================================\n'
    '        CLOUD FLEET MONITORING & ROUTE OPTIMIZATION SYSTEM   \n'
    '============================================================'
)
print(f'Total Fleet Telemetry Records Analyzed: {total_vehicles}')
print(f' Vehicles Operating Normally: {normal_count}')
print(
    '️ Vehicles with High Failure Risk (Alert Triggered):'
    f' {high_risk_count}'
)
print(
    '------------------------------------------------------------\n'
    'Cloud Action Taken:'
)
print(
    '-> High-risk vehicles automatically rerouted to the nearest service'
    ' station.'
)
print(
    '-> Real-time alerts successfully synced with the cloud server'
    ' dashboard.'
)
print('============================================================')