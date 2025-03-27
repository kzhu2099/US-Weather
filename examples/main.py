'''
Author: Kevin Zhu
A basic example for the myweather library,
'''

from myweather import MyWeather

if __name__ == '__main__':
    w = MyWeather('your_email@example.com', 'your appp pass word')
    w.set_location_name('New York')

    '''
    1 week forecast (the max)
    '''

    forecast = w.get_forecast(days = 7, skip_nights = False)
    html = w.forecast_to_html(forecast)
    print(html)

    '''
    12 hour forecast
    '''

    forecast = w.get_hourly_forecast(hours = 12)
    html = w.forecast_to_html(forecast)
    print(html)

    w.send_email('your_email@gmail.com', timezone = 'US/Eastern')