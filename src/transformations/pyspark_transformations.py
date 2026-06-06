from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

from src.utils.config import Config
from src.utils.logger import logger


class WeatherTransformer:

    def __init__(self):

        self.spark = SparkSession.builder.appName("FranceWeatherAnalysis").getOrCreate()

        self.jdbc_url = (
            f"jdbc:postgresql://{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
        )

        self.connection_properties = {
            "user": Config.DB_USER,
            "password": Config.DB_PASSWORD,
            "driver": "org.postgresql.Driver",
        }

    def read_raw_weather(self):

        return self.spark.read.jdbc(
            url=self.jdbc_url,
            table="weather_raw",
            properties=self.connection_properties,
        )

    def clean_weather_data(self, df):

        # Remove duplicates
        df = df.dropDuplicates()

        # Keep only realistic temperatures
        df = df.filter((col("temperature") > -50) & (col("temperature") < 60))

        # Temperature category
        df = df.withColumn(
            "temperature_category",
            when(col("temperature") < 10, "Cold")
            .when(col("temperature") < 22, "Moderate")
            .otherwise("Hot"),
        )

        return df

    def write_clean_weather(self, df):

        (
            df.write.mode("append").jdbc(
                url=self.jdbc_url,
                table="weather_clean",
                properties=self.connection_properties,
            )
        )

    def run(self):

        raw_df = self.read_raw_weather()

        clean_df = self.clean_weather_data(raw_df)

        self.write_clean_weather(clean_df)

        logger.info(
            f"Transformation completed. "
            f"{clean_df.count()} rows written to weather_clean."
        )
