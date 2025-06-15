CREATE TABLE IF NOT EXISTS airports (
    airport_code VARCHAR PRIMARY KEY,
    airport_name VARCHAR,
    state VARCHAR
);

CREATE TABLE IF NOT EXISTS carriers (
    carrier_code VARCHAR PRIMARY KEY,
    carrier_name VARCHAR
);

CREATE TABLE IF NOT EXISTS delays (
    delay_id SERIAL PRIMARY KEY,
    airport_code VARCHAR REFERENCES airports(airport_code),
    carrier_code VARCHAR REFERENCES carriers(carrier_code),
    year INT,
    month INT,
    arr_delay FLOAT,
    weather_delay FLOAT,
    carrier_delay FLOAT,
    nas_delay FLOAT,
    security_delay FLOAT,
    late_aircraft_delay FLOAT
);