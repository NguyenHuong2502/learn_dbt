
import requests

api_url = "https://api.weatherstack.com/current"

params = {
    "access_key": "9cf765c13244c95c012bbf5c44e80cf9",
    "query": "New York"
}

'''def fetch_data():
    print("fetching weather data from weatherstack API...")
    try:
        response = requests.get(api_url, params=params, timeout=15)
        response.raise_for_status()
        print("API respone received successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'an error occurred:{e}')
fetch_data()'''
def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-10-24 03:49', 'localtime_epoch': 1792813740, 'utc_offset': '-4.0'}, 'current': {'observation_time': '07:49 AM', 'temperature': 11, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '07:17 AM', 'sunset': '06:03 PM', 'moonrise': '04:59 PM', 'moonset': '05:28 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 94}, 'air_quality': {'co': '237', 'no2': '45.7', 'o3': '8', 'so2': '1.5', 'pm2_5': '12.8', 'pm10': '13.3', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 8, 'wind_degree': 10, 'wind_dir': 'N', 'pressure': 1033, 'precip': 0, 'humidity': 49,'cloudcover': 5, 'feelslike': 9, 'uv_index': 0, 'visibility': 10, 'is_day': 'no'}}

