import requests
from Private import API_KEY
import Components

def get_lat_and_long(city):
    try:
        Components.validate_input(city=city)
    except ValueError as e:
        return f"Input validation error: {e}"

    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1&aqi=no&alerts=no"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location_name = data['location']['name']
        lat = data['location']['lat']
        lon = data['location']['lon']
        return f"Data for {location_name}: Latitude: {lat}, Longitude: {lon}"
    else:
        return "Error: Unable to fetch data"


