import requests
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
        else:
            logger.info("API request successful.")
            logger.info(f"Response text: {response.text}")

    def get_weather_data(self, city):

        params = {"q": city, "appid": self.api_key, "units": "metric"}

        response = requests.get(url=self._url, params=params)
        self.check_response_status(response)

        return response.json()
