# Data Manipulation in SQL  
CASE statements  
Simple subqueries  
Correlated subqueries  
Window functions  

## Selecting from the European Soccer Database  

SELECT l.name AS league, COUNT(m.country_id) AS total_matches  
FROM soccer.league AS l  
LEFT JOIN soccer.match AS m  
ON l.country_id = m.country_id  
GROUP BY l.name;  

## This code is written using a CASE statement below  

SELECT date, id, home_goal, away_goal  
FROM soccer.match  
WHERE season = '2013/2014'  
    AND home_goal > away_goal;  
    
## CASE statements contains WHEN, THEN, ELSE and END.  
CASE WHEN x = 1 THEN 'a'  
WHEN x = 2 THEN 'b'  
ELSE 'c' END AS new_column  

SELECT id, home_goal, away_goal,  
    CASE WHEN home_goal > away_goal THEN 'Home Team Win'  
         WHEN home_goal < away_goal THEN 'Away Team Win'  
         ELSE 'Tie' END AS outcome  
FROM soccer.match  
WHERE season = '2013/2014';  

SELECT date, hometeam_id, awayteam_id,  
    CASE WHEN hometeam_id = 8455 AND home_goal > away_goal THEN 'Chelsea home win!'  
         WHEN awayteam_id = 8455 AND home_goal < away_goal THEN 'Chelsea away win!'  
         ELSE 'Loss or tie :(' END AS outcome  
FROM soccer.match  
WHERE hometeam_id = 8455 OR awayteam_id = 8455  

## CASE WHEN with COUNT  

SELECT season,  
    COUNT(CASE WHEN hometeam_id = 8650 AND home_goal > away_goal THEN id END) AS home_wins,  
    COUNT(CASE WHEN awayteam_id = 8650 AND away_goal > home_goal THEN id END) AS away_wins  
FROM soccer.match  
GROUP BY season;  

## CASE WHEN with SUM  

SELECT season,  
    SUM(CASE WHEN hometeam_id = 8650 THEN home_goal END) AS home_goals,  
    SUM(CASE WHEN awayteam_id = 8650 THEN away_goal END) AS away_goals  
FROM soccer.match  
GROUP BY season;  

## CASE WHEN with AVG  

SELECT season,  
    AVG(CASE WHEN hometeam_id = 8650 THEN home_goal END) AS avg_homegoals,  
    AVG(CASE WHEN awayteam_id = 8650 THEN away_goal END) AS avg_awaygoals  
FROM soccer.match  
GROUP BY season;  

## Using ROUND  

SELECT season,  
    ROUND(AVG(CASE WHEN hometeam_id = 8650 THEN home_goal END),2) AS avg_homegoals,  
    ROUND(AVG(CASE WHEN awayteam_id = 8650 THEN away_goal END),2) AS avg_awaygoals  
FROM soccer.match  
GROUP BY season;  

## Percentages with CASE and AVG  

SELECT season,  
    AVG(CASE WHEN hometeam_id = 8455 AND home_goal > away_goal THEN 1  
             WHEN hometeam_id = 8455 AND home_goal < away_goal THEN 0  
             END) AS pct_homewins,  
    AVG(CASE WHEN awayteam_id = 8455 AND away_goal > home_goal THEN 1  
             WHEN awayteam_id = 8455 AND away_goal < home_goal THEN 0  
             END) AS pct_awaywins,  
FROM soccer.match  
GROUP BY season;  

## Subquery  

A subquery is a query nested inside another query.  

SELECT home_goal  
FROM match  
WHERE home_goal > (SELECT AVG(home_goal) FROM match);  

## Query from FROM  

SELECT team, home_avg  
FROM (SELECT  
		t.team_long_name AS team,  
        AVG(m.home_goal) AS home_avg  
      FROM match as m  
      LEFT JOIN team as t  
      ON m.hometeam_id = t.team_api_id  
      WHERE season = '2011/2012'  
      GROUP BY team) AS subquery  
ORDER BY home_avg DESC  
LIMIT 3;  

## Queries from SELECT  

SELECT season, COUNT(id) AS matches,  
		(SELECT COUNT(id) FROM match) AS total_matches  
FROM match  
GROUP BY season;  

## Correlated queries, Nested queries, and Common Table Expressions  

Correlated subqueries use values from the outer query to generate a result.  

What is the avg number of goals scored in each country ?  

SELECT c.name AS country, AVG(m.home_goal + m.away_goal) AS avg_goals  
FROM country AS c  
LEFT JOIN match AS m  
ON c.id = m.country_id  
GROUP BY country;  

## Nested subquery  

A subquery inside another subquery  

**EXTRACT** - EXTRACT (MONTH FROM date) AS month  

## Common Table Expressions - CTEs  

WITH cte AS (  
SELECT col1, col2  
FROM table)  
SELECT AVG(col1) AS avg_col  
FROM cte;  

## Window functions  

Class of functions that perform calculations on a result set that has already been generated.  

Agregate calculations -  
- Similar to subqueries in SELECT  
- Running totals, rankings, moving averages  

How many goals were scored in each match in 2011/2012, and how did that compare to the average?  

SELECT date, (home_goal + away_goal) AS goals,  
(SELECT AVG(home_goal + away_goal)  
FROM match  
WHERE season = '2011/2012') AS overall_avg  
FROM match  
WHERE season = '2011/2012';  

OR  

**USE A WINDOW FUNCTION OVER()**  
SELECT date, (home_goal + away_goal) AS goals,  
AVG(home_goal + away_goal) OVER() AS overall_avg  
FROM match  
WHERE season = '2011/2012';  

## RANK  

What is the rank of matches based on number of goals?  
SELECT date, (home_goal + away_goal) AS goals,  
RANK() OVER(ORDER BY home_goal + away_goal DESC) AS goal_rank  
FROM match  
WHERE season = '2011/2012';  

## Window partitions  

Calculate separate values for different categories.  
Calculate different calculations in the same column.  

AVG(home_goal) OVER(PARTITION BY season)  

How many goals were scored in each match, and how did that compare to the overall average?  

SELECT date, (home_goal + away_goal) AS goals,  
AVG(home_goal + away_goal) OVER() AS overall_avg  
FROM match;  

OR  

SELECT date, (home_goal + away_goal) AS goals,  
AVG(home_goal + away_goal) OVER(PARTITION BY season) AS season_avg  
FROM match;  

## Sliding windows  

Perform calculations relative to the current row.  
Can be used to calculate running totals, sums, averages, etc...  

**ROWS BETWEEN <start> AND <finish>**  
**PROCEDING**
**FOLLOWING**  
**UNBOUNDED PRECEDING**  
**UNOUNDED FOLLOWING**  
**CURRENT ROW**  
    
SELECT date, home_goal, away_goal, SUM(home_goal)  
    OVER(ORDER BY date ROWS BETWEEN  
    UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total  
FROM match  
WHERE hometeam_id = 8456 AND season = '2011/2012';  
