SELECT
	DISTINCT sj.name
FROM 
	professors p
JOIN subjects sj ON sj.professor_id = p.id
JOIN grades g ON g.subject_id = sj.id
WHERE p.id = 5 AND g.student_id = 5
