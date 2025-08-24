SELECT coping_strategy, COUNT(*) AS count
FROM stress_data
GROUP BY coping_strategy
ORDER BY count DESC;