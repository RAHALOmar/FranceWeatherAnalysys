CREATE TABLE weather_raw (
    id SERIAL PRIMARY KEY,

    country_code VARCHAR(2) NOT NULL,
    city VARCHAR(100) NOT NULL,

    temperature FLOAT NOT NULL,
    feels_like FLOAT,
    temperature_min FLOAT NOT NULL,
    temperature_max FLOAT NOT NULL,

    humidity INTEGER,
    pressure INTEGER,

    weather_main VARCHAR(100),
    weather_description VARCHAR(255),

    wind_speed FLOAT,

    cloudiness INTEGER,

    extraction_time TIMESTAMPTZ NOT NULL
);