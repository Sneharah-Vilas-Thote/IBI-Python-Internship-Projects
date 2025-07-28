# Weather-Forecast-App.py

"""
Weather Forecast App
---------------------
This Python script fetches and displays the current weather for a given city
using the OpenWeatherMap API. Make sure to replace 'YOUR_API_KEY' with your actual API key.
"""

import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key from https://openweathermap.org/api
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Construct final URL
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"

    # Fetch data from OpenWeatherMap
    response = requests.get(complete_url)
    data = response.json()

    # Check for successful response
    if data["cod"] != "404":
        weather_data = data["main"]
        current_temp = weather_data["temp"]
        pressure = weather_data["pressure"]
        humidity = weather_data["humidity"]
        description = data["weather"][0]["description"]

        print(f"\n📍 Weather Forecast for: {city}")
        print(f"🌡 Temperature: {current_temp}°C")
        print(f"💨 Pressure: {pressure} hPa")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌥 Condition: {description.capitalize()}\n")
    else:
        print("\n❌ City Not Found! Please enter a valid city name.\n")

# -------- Main Program Starts Here --------

print("=== Weather Forecast App ===")
user_city = input("Enter city name: ")
get_weather(user_city)
