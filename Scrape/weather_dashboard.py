import requests
import pandas as pd
import streamlit as st

API_KEY = "your_openweathermap_api_key"
cities = ["London", "New York", "Paris", "Tokyo"]

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return {
            "City": city,
            "Temperature": data["main"]["temp"],
            "Condition": data["weather"][0]["description"]
        }
    else:
        return {"City": city, "Temperature": None, "Condition": None}

# Fetch weather data for each city
weather_data = [fetch_weather(city) for city in cities]
weather_df = pd.DataFrame(weather_data)

# Display data with Streamlit
st.title("Weather Dashboard")
st.write(weather_df)
