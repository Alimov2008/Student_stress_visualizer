SELECT coping_strategy, ROUND(AVG(stress_index),3) AS avg_stress, COUNT(*) AS students
FROM stress_data
GROUP BY coping_strategy
ORDER BY avg_stress ASC;