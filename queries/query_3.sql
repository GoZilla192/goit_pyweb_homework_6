SELECT 
	sj.name,
	gr.name,
	s.first_name,
	s.last_name,
	AVG(gd.grade) as avg_grade
FROM 
	grades gd
JOIN students s ON s.id = gd.student_id
JOIN groups gr ON gr.id = s.group_id
JOIN subjects sj ON sj.id = gd.subject_id
WHERE sj.name = "Біологія"
GROUP BY gr.name