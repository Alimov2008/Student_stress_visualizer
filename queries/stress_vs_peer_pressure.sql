SELECT peer_pressure, ROUND(AVG(stress_index),3) AS avg_stress
FROM stress_data
GROUP BY peer_pressure
ORDER BY peer_pressure;