SELECT home_academic_pressure, ROUND(AVG(stress_index),3) AS avg_stress
FROM stress_data
GROUP BY home_academic_pressure
ORDER BY home_academic_pressure;