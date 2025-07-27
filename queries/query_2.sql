SELECT 
	s.first_name,
	s.last_name,
	sj.name as subject_name,
	AVG(g.grade) as avg_grade
FROM 
	students s
JOIN grades g ON g.student_id = s.id
JOIN subjects sj ON g.subject_id = sj.id
WHERE sj.name = "Інформатика"
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 1