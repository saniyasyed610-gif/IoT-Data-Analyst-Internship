# IoT Sensor Data Simulation

temperature = 28.5
humidity = 70
pressure = 1012

print("IoT Sensor Readings")
print("-------------------")
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Pressure:", pressure, "hPa")

if temperature > 30:
    print("Status: High Temperature Alert!")
else:
    print("Status: Temperature is Normal")