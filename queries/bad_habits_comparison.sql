SELECT bad_habits, ROUND(AVG(stress_index),3) AS avg_stress
FROM stress_data
GROUP BY bad_habits;