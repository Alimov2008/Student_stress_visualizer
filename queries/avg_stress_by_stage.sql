SELECT academic_stage, ROUND(AVG(stress_index),3) AS avg_stress
FROM stress_data
GROUP BY academic_stage
ORDER BY avg_stress DESC;
