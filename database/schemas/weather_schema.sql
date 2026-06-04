CREATE TABLE weather_raw (
    id SERIAL PRIMARY KEY,

    city VARCHAR(100) NOT NULL,

    temperature FLOAT,

    humidity INTEGER,

    pressure INTEGER,

    weather_description VARCHAR(255),

    extraction_time TIMESTAMP NOT NULL
);