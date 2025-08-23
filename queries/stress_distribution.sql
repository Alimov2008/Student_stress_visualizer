SELECT stress_index, COUNT(*) AS student_count
FROM stress_data
GROUP BY stress_index
ORDER BY stress_index;