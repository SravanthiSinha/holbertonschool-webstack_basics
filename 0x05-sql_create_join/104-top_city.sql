-- displays the top 3 of cities temperature during July and August ordered by temperature 
SELECT city, SUM(value)/COUNT(city) AS avg_temp FROM temperatures
WHERE month IN (7, 8)
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
