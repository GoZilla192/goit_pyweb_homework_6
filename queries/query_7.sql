SELECT 
	*
FROM
	students s
JOIN groups g ON g.id = s.group_id
JOIN grades gd ON gd.student_id = s.id
WHERE g.id = 2 AND gd.subject_id = 2