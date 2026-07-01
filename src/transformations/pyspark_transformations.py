from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

from src.utils.config import Config
from src.utils.constants import WEATHER_CLEAN_TABLE, WEATHER_RAW_TABLE
from src.utils.logger import logger


class WeatherTransformer:

    def __init__(self):
        # Initialize Spark session with PostgreSQL JDBC driver
        self.spark = (
            SparkSession.builder.appName("FranceWeatherAnalysis")
            .master("local[*]")
            .config("spark.driver.extraClassPath", r"jars\postgresql-42.7.4.jar")
            .getOrCreate()
        )

        # JDBC connection properties
        self.jdbc_url = (
            f"jdbc:postgresql://{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
        )

        # Connection properties for JDBC
        self.connection_properties = {
            "user": Config.DB_USER,
            "password": Config.DB_PASSWORD,
            "driver": "org.postgresql.Driver",
        }

    def read_raw_weather(self):

        return self.spark.read.jdbc(
            url=self.jdbc_url,
            table=WEATHER_RAW_TABLE,
            properties=self.connection_properties,
        )

    def clean_weather_data(self, df):

        # Remove duplicates from the raw data
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
        # Humidity category
        df = df.withColumn(
            "humidity_category",
            when(col("humidity") < 40, "Dry")
            .when(col("humidity") < 70, "Normal")
            .otherwise("Humid"),
        )

        return df

    def write_clean_weather(self, df):

        (
            df.write.mode(
                "overwrite"
            ).jdbc(  # using 'overwrite' mode to replace the existing
                # data in the table instead of 'append' mode to it
                # this is because we want to keep the table clean and not have duplicates in it
                url=self.jdbc_url,
                table=WEATHER_CLEAN_TABLE,
                properties=self.connection_properties,
            )
        )

    def run(self):

        raw_df = self.read_raw_weather()

        clean_df = self.clean_weather_data(raw_df)
        clean_df = clean_df.drop("id")
        self.write_clean_weather(clean_df)

        logger.info(
            f"Transformation completed. "
            f"{clean_df.count()} rows written to weather_clean."
        )
