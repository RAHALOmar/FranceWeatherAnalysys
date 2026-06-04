import requests
from datetime import datetime, UTC

from ..utils.logger import logger


class WeatherAPI:

    _url = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key):
        self.api_key = api_key

    def check_response_status(self, response):
        if response.status_code != 200:
            logger.error(
                f"API request failed with status code {response.status_code}: {response.text}"
            )
            raise Exception(f"API request failed: {response.status_code}")
        else:
            logger.info("API request successful.")
            # logger.info(f"Response text: {response.text}")

    def get_weather_data(self, country, city):

        params = {"q": f"{city},{country}", "appid": self.api_key, "units": "metric"}

        response = requests.get(url=self._url, params=params)
        self.check_response_status(response)

        return response.json()

    def get_limited_weather_data(self, country, city):
        data = self.get_weather_data(country, city)
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather_description": data["weather"][0]["description"],
            "extraction_time": datetime.now(UTC),
        }
