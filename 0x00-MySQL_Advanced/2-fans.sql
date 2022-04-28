-- ranks country origins of bands, ordered by the number of (non-unique) fans
-- Make the query
SELECT * FROM (
	SELECT origin, SUM(fans) as nb_fans
	FROM metal_bands
	GROUP BY origin) as table1
	ORDER BY nb_fans DESC;

