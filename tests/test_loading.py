from src.utils.config import Config
from src.extraction.weather_api import WeatherAPI
from src.loading.postgres_loader import PostgresLoader

api = WeatherAPI(api_key=Config.OPENWEATHER_API_KEY)
weather_data = api.get_limited_weather_data(country="FR", city="Brest")
loader = PostgresLoader()
loader.insert_weather(weather_data)
