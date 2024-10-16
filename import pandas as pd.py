import pandas as pd
import random

# List of cities in Malaysia
cities = ['Kuala Lumpur', 'Penang', 'Kedah', 'Perak', 'Selangor', 'Sabah', 'Sarawak', 'Kelantan', 'Terengganu', 'Pahang', 'Perlis', 'Melaka', 'Negeri Sembilan', 'Putrajaya', 'Johor', 'Labuan']

# Function to generate random AQI and pollutant levels
def generate_aqi_data(cities):
    data = []
    for city in cities:
        aqi = random.randint(50, 200)  # AQI between 50 (Good) to 200 (Unhealthy)
        pm25 = random.uniform(10, 35)  # PM2.5 in micrograms per cubic meter
        pm10 = random.uniform(20, 50)  # PM10 in micrograms per cubic meter
        ozone = random.uniform(15, 40)  # Ozone levels in ppb
        data.append([city, aqi, pm25, pm10, ozone])
    return data

# Generate AQI data for Malaysia cities
aqi_data = generate_aqi_data(cities)

# Create DataFrame
columns = ['City', 'AQI', 'PM2.5', 'PM10', 'Ozone']
df_aqi = pd.DataFrame(aqi_data, columns=columns)

# Save to CSV
df_aqi.to_csv('malaysia_aqi_data_no_dates.csv', index=False)
print("CSV file saved successfully without dates!")
