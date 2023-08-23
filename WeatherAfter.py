import requests


def get_weather_forecast(city, days, api_key, stop_hour=None):
    result = []

    if stop_hour is None:
        hour_range = 24
    else:
        hour_range = min(int(stop_hour), 24)

    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={days}&hour=0-23&aqi=no&alerts=no"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for day in range(days):
            for hour in range(hour_range):
                if hour > 12:
                    adjusted_hour = hour - 12
                    am_pm = "PM"
                elif hour == 0:
                    adjusted_hour = 12
                    am_pm = "AM"
                else:
                    adjusted_hour = hour
                    am_pm = "AM"

                temp = data['forecast']['forecastday'][day]['hour'][hour]['temp_c']
                result.append([f"Day {day + 1}", f"{adjusted_hour} {am_pm}", f"{temp}°C"])
    else:
        result.append(["Error: Unable to fetch data"])

    print("Data For : ", data['location']['name'])
    return result
