SELECT
	AVG(g.grade) as avg_grade
FROM
	grades g
JOIN subjects s ON g.subject_id = s.id
WHERE s.professor_id = 1
GROUP BY s.id