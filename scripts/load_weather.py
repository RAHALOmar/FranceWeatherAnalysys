from src.utils.config import Config
from src.utils.logger import logger
from src.utils.constants import FRENCH_CITIES
from src.extraction.weather_api import WeatherAPI
from src.loading.postgres_loader import PostgresLoader

api = WeatherAPI(Config.OPENWEATHER_API_KEY)
loader = PostgresLoader()


def load_weather_data(locations: list[tuple[str, str]]) -> None:
    """Load weather data for specified locations into the database.
    Args:
        locations: A list of tuples containing country code and city names.

    Returns:
        None"""
    for country, city in locations:
        weather = api.get_limited_weather_data(country=country, city=city)
        loader.insert_weather(weather)
        logger.info(f"Inserted {country}, {city}")


if __name__ == "__main__":
    load_weather_data(FRENCH_CITIES)
