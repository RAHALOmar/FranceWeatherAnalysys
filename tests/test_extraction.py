from src.utils.config import Config
from src.extraction.weather_api import WeatherAPI

api = WeatherAPI(api_key=Config.OPENWEATHER_API_KEY)
api.get_weather_data(city="Paris")
