SELECT academic_competition, ROUND(AVG(stress_index),3) AS avg_stress
FROM stress_data
GROUP BY academic_competition
ORDER BY academic_competition;