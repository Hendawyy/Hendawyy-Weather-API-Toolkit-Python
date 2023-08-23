import requests
from Private import API_KEY
import Components

def get_current_temperature(city):
    try:
        Components.validate_input(city=city)
    except ValueError as e:
        return f"Input validation error: {e}"

    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1&aqi=no&alerts=no"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        current_temp = data['current']['temp_c']
        location_name = data['location']['name']
        return f"Current temperature in {location_name}: {current_temp}°C"
    else:
        return "Error: Unable to fetch data"



