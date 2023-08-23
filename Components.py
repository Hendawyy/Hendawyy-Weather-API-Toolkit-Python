import requests
from Private import API_KEY
from tabulate import tabulate
import WeatherAfter as WA
import CurrentTemp as CT
import  LatLong as LL

def validate_input(city=None, days=None, stop_hour=None):
    if city is not None and not isinstance(city, str):
        raise ValueError("City must be a string.")

    if days is not None and not (isinstance(days, int) and 1 <= days <= 10):
        raise ValueError("Days must be an integer between 1 and 10.")

    if stop_hour is not None and not (isinstance(stop_hour, int) and 1 <= stop_hour <= 24):
        raise ValueError("Stop_hour must be an integer between 1 and 24.")

    return True

def get_weather_forecast_from_input():
    city = input("Enter the city: ")
    days = int(input("Enter the number of days (1-10): "))
    stop_hour = int(input("Enter the stop hour (1-24 (12-hour format), or leave blank for all hours): "))

    try:
        validate_input(city=city, days=days, stop_hour=stop_hour)
    except ValueError as e:
        print(f"Input validation error: {e}")
    else:
        forecast = WA.get_weather_forecast(city, days, API_KEY, stop_hour)

        if len(forecast) > 0:
            headers = ["Day", "Hour", "Temperature"]
            print(tabulate(forecast, headers=headers, tablefmt="pretty"))
        else:
            print("Error: Unable to fetch data")


def get_current_temperature_input():
    city = input("Enter the city: ")
    result = CT.get_current_temperature(city)
    print(f"Current Temprature is {result}")

def get_lat_long_input():
    city = input("Enter the city: ")
    result = LL.get_lat_and_long(city)
    print(result)

