SELECT 
	gd.student_id,
	gd.grade
FROM 
	grades gd
JOIN students s ON s.id = gd.student_id
WHERE s.group_id = 2 
AND gd.subject_id = 2 
AND gd.received_date in (
	SELECT 
		gd.received_date
	FROM grades gd
	JOIN students s ON s.id = gd.student_id
	WHERE gd.subject_id = 2 
	AND s.group_id = 2
	ORDER BY gd.received_date DESC
	LIMIT 1
)