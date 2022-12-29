# Joining Data with SQL

## Inner join  
Looks for records in both tables which match on a given field.  

Inner join of presidents and prime_ministers, joining on country.  

SELECT prime_ministers.country, prime_ministers.continent, prime_minister, president -- fields we want returned  
FROM prime_ministers -- left table  
INNER JOIN presidents -- right table  
ON prime_ministers.country = presidents.country; -- field to match both table on  

SELECT p1.country, p1.continent, prime_minister, president  
FROM prime_ministers AS p1  
INNER JOIN presidents AS p2  
USING(country);  

-- Select fields with aliases  
SELECT c.code AS country_code, name, year, inflation_rate  
FROM countries AS c  
-- Join to economies (alias e)  
INNER JOIN economies AS e  
-- Match on code field using table aliases  
ON c.code = e.code;  

## Multiple joins  
SELECT *  
FROM left_table  
INNER JOIN right_table  
ON left_table.id = right_table.id  
INNER JOIN another_table  
ON left_table.id = another_table.id;  

SELECT p1.country, p1.continent, president, prime_minister, pm_start  
FROM prime_ministers AS p1  
INNER JOIN presidents AS p2  
USING(country)  
INNER JOIN prime_minister_terms AS p3  
USING(prime_minister);  

-- Joining on multiple fields  
SELECT *  
FROM left_table  
INNER JOIN right_table  
ON left_table.id = right_table.id  
AND left_table.date = right_table.date  
            
## Left and Right joins  

**Left join** will return all records in the left table, and those records in the right table that match on the joining field provided.  

SELECT p1.country, prime_minister, president  
FROM prime_ministers AS p1  --left table  
LEFT JOIN presidents AS p2  --right table  
USING(country);  

**Right join** will return all records in the right table, and those records in the left table that match on the joining field provided.  

SELECT p1.country, prime_minister, president  
FROM prime_ministers AS p1  --left table  
RIGHT JOIN presidents AS p2  --right table  
USING(country);  

## Full join  

Full join combines left join and right join.  

SELECT *  
FROM left_table  
FULL JOIN right_table  
USING(id);  

SELECT p1.country AS country, prime_minister, president  
FROM prime_ministers AS p1  
FULL JOIN presidents AS p2  
ON p1.country = p2.country  
LIMIT 10;  

## Cross join  

Cross join creates all possible combinations of two tables.  

SELECT id1, id2  
FROM table1  
CROSS JOIN table2;  

## Self joins  

A table is joined to itself. They can be used to compare parts of the same table.  

SELECT p1.country AS country1, p2.country AS country2, p1.continent  
FROM prime_ministers AS p1  
INNER JOIN prime_ministers AS p2  
ON p1.continent = p2.continent  
LIMIT 10;  

## Set theory for SQL joins  

UNION - Takes two tables as input, and returns all records from both tables, w/o repeats.    

SELECT *  
FROM left_table  
UNION  
SELECT *  
FROM right_table;  

UNION ALL - Takes two tables and returns all records from both tables, including duplicates.

SELECT *  
FROM left_table  
UNION ALL  
SELECT *  
FROM right_table;  

SELECT monarch AS leader, country  
FROM monarchs  
UNION ALL  
SELECT prime_minister, country  
FROM prime_ministers  
ORDER BY country, leader  
LIMIT 10;  

## INTERSECT  
Returns only the results that intersect between both tables.  
Requires all fields to match.

SELECT id, val  
FROM left_table  
INTERSECT  
SELECT id, val  
FROM right_table;  

SELECT country AS intersect_country  
FROM prime_ministers  
INTERSECT  
SELECT country  
FROM presidents;  
^ Returns the countries with both a prime minister and a president  

## EXCEPT  

Allows us to identify the records that are present in one table but not the other.  

SELECT monarch, country  
FROM monarchs  
EXCEPT  
SELECT prime_minister, country  
FROM prime_ministers;  
^ Monarchs that do not also hold the role of prime minister.  


## Semi joins  

A semi join chooses records in the first table where a condition is met in the second table.  

SELECT president, country, continent  
FROM presidents  
WHERE country IN  
(SELECT country  
FROM states  
WHERE indep_year < 1800):  

## Anti joins  

An anti join chooses records in the first table where column 1 does not find a match in column 2.  

SELECT country, president  
FROM presidents  
WHERE continent LIKE '%America'  
AND country NOT IN  
(SELECT country  
FROM states  
WHERE indep_year < 1800);  

## Subqueries  

SELECT *  
FROM some_table  
WHERE some_field IN  
(include subquery here);  

SELECT *  
FROM some_table  
WHERE some_field IN  
(SELECT some_numeric_field  
FROM another_table  
WHERE field2 = some_condition);  

SELECT DISTINCT continent,  
(SELECT COUNT(*)  
FROM monarchs  
WHERE states.continent = monarch.continent) AS monarch_count  
FROM states;  

SELECT *  
FROM populations  
-- Filter for only those populations where life expectancy is 1.15 times higher than average  
WHERE life_expectancy >   
  (SELECT AVG(life_expectancy * 1.15)  
   FROM populations  
   WHERE year = 2015)   
    AND year = 2015;  
    
-- Select relevant fields from cities table  
SELECT name, country_code, urbanarea_pop  
FROM cities  
-- Filter using a subquery on the countries table  
WHERE name IN  
    (SELECT capital  
     FROM countries)  
ORDER BY urbanarea_pop DESC;  

-- Find top nine countries with the most cities  
SELECT countries.name AS country, COUNT(*) AS cities_num  
FROM countries  
LEFT JOIN cities  
ON countries.code = cities.country_code  
GROUP BY country  
-- Order by count of cities as cities_num  
ORDER BY cities_num DESC, country  
LIMIT 9;  

## Subqueries inside a FRROM clause  

If we're interested in all the continents with monarchs as well as the most recent country to gain independence in that continent.  

SELECT continent, MAX(indep_year) AS most_recent  
FROM states  
GROUP BY continent;  

Now, ho do we filter for only continents with monarchs ?  

SELECT DISTINCT monarchs.continent, sub.most_recent  
FROM monarchs,  
(SELECT continent, MAX(indep_year) AS most_recent  
 FROM states  
 GROUP BY continent) AS sub  
WHERE monarchs.continent = sub.continent  
ORDER BY continent;  

-- Select local_name and lang_num from appropriate tables  
SELECT local_name, sub.lang_num  
FROM countries,  
  (SELECT code, COUNT(*) AS lang_num  
  FROM languages  
  GROUP BY code) AS sub  
-- Where codes match  
WHERE countries.code = sub.code  
ORDER BY lang_num DESC;  

-- Select fields from cities  
SELECT name, country_code, city_proper_pop, metroarea_pop, city_proper_pop / metroarea_pop * 100 AS city_perc  
FROM cities  
WHERE name IN  
-- Use subquery to filter city name  
    (SELECT capital  
     FROM countries  
     WHERE continent = 'Europe' OR continent LIKE '%America')  
-- Add filter condition such that metroarea_pop does not have null values  
AND metroarea_pop IS NOT NULL  
-- Sort and limit the result  
ORDER BY city_perc DESC  
LIMIT 10;  
