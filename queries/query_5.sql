SELECT 
	s.name
FROM 
	subjects s
JOIN professors p ON p.id = s.professor_id
WHERE p.id = 1