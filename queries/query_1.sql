SELECT 
	s.first_name,
	s.last_name,
	AVG(g.grade) as average_grade
FROM 
	students s
JOIN grades g ON s.id = g.student_id
GROUP BY student_id
ORDER BY average_grade DESC
LIMIT 5