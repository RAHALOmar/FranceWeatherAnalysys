from src.utils.config import Config
from src.extraction.weather_api import WeatherAPI

api = WeatherAPI(api_key=Config.OPENWEATHER_API_KEY)
data = api.get_weather_data(country="FR", city="Brest")
print(data)

weather_data = api.get_limited_weather_data(country="FR", city="Brest")
print(weather_data)
