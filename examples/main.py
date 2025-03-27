from myweather import MyWeather
import json

if __name__ == '__main__':
    w = MyWeather()

    weather = w.get_current_location_weather('Chicago')

    print(weather)