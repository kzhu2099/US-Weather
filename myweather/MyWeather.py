'''
Author: Kevin Zhu
'''

import requests

class MyWeather:
    def __init__(self):
        self.weather_api = 'https://api.open-meteo.com/v1/forecast'
        self.location_api = 'https://nominatim.openstreetmap.org/search'

    def get_location(self, location_name):
        params = {
            'q': location_name,
            'format': 'json',
            'limit': 1
        }

        response = requests.get(self.location_api, params = params, headers = {'User-Agent': 'myweather/1.0'})

        if response.status_code == 200:
            data = response.json()
            return data[0]

        else:
            print(f'Error: {response.status_code}')
            return {}

    def forecast(self, params):
        response = requests.get(self.weather_api, params = params)

        if response.status_code == 200:
            data = response.json()
            return data['current']

        else:
            print(f'Error: {response.status_code}')
            return {}

    def get_current_location_weather(self, location_name):
        location = self.get_location(location_name)
        params = {
            'latitude': location['lat'],
            'longitude': location['lon'],
            'current': 'temperature_2m,wind_speed_10m',
        }

        forecast = self.forecast(params)

        result = \
f'''
🌍 Weather for {location_name.capitalize()} 🌍'
------------------------------
⏰ Time: {forecast['time']}
📍 Location: ({float(location['lat']):.2f}, {float(location['lon']):.2f})
🌡️  Temperature: {forecast['temperature_2m']}°C
💨 Wind Speed: {forecast['wind_speed_10m']} m/s
------------------------------
'''
        return result