import os

from pyspark.sql import SparkSession


def get_spark(app_name: str = "FranceWeatherAnalysis") -> SparkSession:
    """
    Create (or retrieve) a SparkSession configured for this project.
    """

    jar_path = os.path.join("jars", "postgresql-42.7.4.jar")

    spark = (
        SparkSession.builder.appName(app_name)
        .master("local[*]")
        .config("spark.driver.extraClassPath", jar_path)
        .getOrCreate()
    )

    return spark


get_spark()
