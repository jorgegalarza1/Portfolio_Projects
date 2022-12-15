-- COUNT() Counts the number of records with a value in a field.
-- Counts the number of records in a field
SELECT COUNT(field_1) AS count_field_1
FROM table_1;

-- Counts the number of records in two field
SELECT COUNT(field_1) AS count_field_1, COUNT(field_2) AS count_field_2
FROM table_1;

-- Below, counts values in a field
COUNT(field_1)

-- (*), counts the number of records in a table
COUNT(*)

-- To count the number of records in table_1
SELECT COUNT(*) AS total_records
FROM table_1;

-- DISTINCT() Removes all duplicates in a field
SELECT field_name
FROM table_1;

-- Only show the distinct records in a field from table_1
SELECT DISTINCT field_name
FROM table_1;

-- Combining COUNT() and DISTINCT
SELECT COUNT(DISTINCT field_1) AS count_disting_variablea
FROM table_1;

-- COUNT() counts everything, regardless of the duplicates.
-- COUNT(DISTINCT) counts only the distinct (non-duplicate) values

-- SQL is not processed in its written order
1-FROM
2-SELECT
3-LIMIT

-- WHERE to filter a clause
WHERE field = 'condition'

-- Example:
 SELECT title -- Select the field "title"
 FROM films -- From the "films" table
 WHERE release_year >= 1940; -- Where the field "release_year" is greater or equal to 1940
 --  = equal to
 --  > greater than
 --  < less than
 -- <= less than or equal to
 -- >= greater than or equal to
 -- <> exclude


