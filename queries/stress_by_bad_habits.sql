SELECT bad_habits, ROUND(AVG(stress_index),3) AS avg_stress, COUNT(*) AS students
FROM stress_data
GROUP BY bad_habits
ORDER BY avg_stress DESC;