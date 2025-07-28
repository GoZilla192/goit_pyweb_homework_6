SELECT 
	DISTINCT name
FROM 
	grades g
JOIN students s ON s.id = g.student_id
JOIN subjects sj ON sj.id = g.subject_id
WHERE s.id = 2