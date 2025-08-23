SELECT study_environment, ROUND(AVG(Stress_Index),3) AS avg_stress, COUNT(*) AS students
FROM stress_data
GROUP BY study_environment
ORDER BY avg_stress DESC;
