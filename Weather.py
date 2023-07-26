import requests
import os
import time

def current_temp():
    api_key = os.environ.get("api_key")
    weather_api_endpoint = f'https://api.openweathermap.org/data/2.5/onecall?lat=53.349804&lon=-6.260310&exclude=hourly&appid={api_key}'

    response = requests.get(weather_api_endpoint)
    if response.status_code == 200:
        weather_data = response.json()
        current_weather_json_data = weather_data.get('current')
        if current_weather_json_data:
            current_temp_k = int(current_weather_json_data.get('temp', 0))
            return kelvin_to_celsius(current_temp_k)
        else:
            print("Error: 'current' key not found in the API response.")
    else:
        print(f"Error: Failed to fetch weather data. Status code: {response.status_code}")

    return None

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

