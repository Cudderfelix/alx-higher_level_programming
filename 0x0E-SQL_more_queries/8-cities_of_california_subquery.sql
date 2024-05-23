-- lists all cities of california that can be found in the database
-- where the states table contain only one record where name = california
-- results are sorted in ASC by cities.id
SELECT id, name FROM cities WHERE state_id = (
	select id
	FROM states
	WHERE name='California'
) ORDER By cities.id ASC;
