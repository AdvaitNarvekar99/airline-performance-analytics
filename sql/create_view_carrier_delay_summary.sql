CREATE OR REPLACE VIEW vw_carrier_delay_summary AS
SELECT
    carrier_name,
    COUNT(*) AS total_flights,
    ROUND(AVG(arr_delay), 2) AS avg_arrival_delay,
    ROUND(SUM(carrier_delay), 2) AS total_carrier_delay,
    ROUND(SUM(weather_delay), 2) AS total_weather_delay,
    ROUND(SUM(nas_delay), 2) AS total_nas_delay
FROM delays
GROUP BY carrier_name
ORDER BY avg_arrival_delay DESC;