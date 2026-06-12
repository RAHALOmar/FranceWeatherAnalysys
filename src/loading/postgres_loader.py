import psycopg2

from ..utils.config import Config
from ..utils.constants import WEATHER_RAW_TABLE
from ..utils.logger import logger


class PostgresLoader:

    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
            )
            logger.info("Connected to PostgreSQL database.")
        except Exception as e:
            logger.error(f"Error connecting to PostgreSQL database: {e}")
            raise

    def insert_weather(self, weather_data: dict):
        if self.connection is None:
            self.connect()
        try:
            with self.connection.cursor() as cursor:
                insert_query = f"""
                    INSERT INTO {WEATHER_RAW_TABLE} (
                        country_code, city, 
                        temperature, feels_like, temperature_min, temperature_max,
                        humidity, pressure, 
                        weather_main, weather_description, 
                        wind_speed,
                        cloudiness, 
                        extraction_time
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(
                    insert_query,
                    (
                        weather_data["country_code"],
                        weather_data["city"],
                        weather_data["temperature"],
                        weather_data["feels_like"],
                        weather_data["temperature_min"],
                        weather_data["temperature_max"],
                        weather_data["humidity"],
                        weather_data["pressure"],
                        weather_data["weather_main"],
                        weather_data["weather_description"],
                        weather_data["wind_speed"],
                        weather_data["cloudiness"],
                        weather_data["extraction_time"],
                    ),
                )
            self.connection.commit()
            logger.info("Weather data inserted successfully.")
        except Exception as e:
            logger.error(f"Error inserting weather data: {e}")
            self.connection.rollback()
            raise
