import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")  
CITY = "Mumbai"

URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code == 200 and "main" in data:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    df = pd.DataFrame({
        "Metric": ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"],
        "Value": [temperature, humidity, pressure]
    })

    sns.set(style="whitegrid")
    sns.barplot(x="Metric", y="Value", data=df, palette="coolwarm")
    plt.title(f"Weather Data for {CITY}")
    plt.tight_layout()
    plt.show()

else:
    print("❌ Failed to fetch weather data.")
    print(f"Status Code: {response.status_code}")
    print(f"Message: {data.get('message')}") 
