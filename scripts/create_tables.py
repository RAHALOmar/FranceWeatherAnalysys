"""
script to create the tables in the PostgreSQL database
using the schema defined in weather_schema.sql

P.S: database creation is not handled in this script,
it should be created manually before running this script.
"""

import psycopg2

from src.utils.config import Config
from src.utils.logger import logger


def create_tables(path="database/schemas/weather_schema.sql"):
    """
    Creates tables in the PostgreSQL database using the schema defined in the provided SQL file.
    Args:
        path (str): The file path to the SQL schema file. Default is "database/schemas/weather_schema.sql".

    """
    with psycopg2.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
    ) as conn:
        with conn.cursor() as cur:

            with open(path, "r", encoding="utf-8") as f:

                schema = f.read()

            cur.execute(schema)

        conn.commit()

    logger.info("Tables created successfully.")


if __name__ == "__main__":
    create_tables(path="database/schemas/weather_schema.sql")
    create_tables(path="database/schemas/weather_clean.sql")
