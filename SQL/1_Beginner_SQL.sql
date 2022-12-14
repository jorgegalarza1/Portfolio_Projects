-- Rows = records
-- Rows are unlimited
-- Columns = fields
-- Columns are set when the dataset was created

-- Select all fields (columns)
SELECT *
-- From the 'sample_table' table
FROM sample_table

-- VARCHAR is a flexible and popular string data type in SQL
-- INT is a flexible and popular integer data type in SQL
-- NUMERIC is a flexible and popular float data type in SQL
-- DATE is a flexible and popular date data type in SQL
-- A schema (blueprints) what tables are stored in the database and any relationship between its table
    -- It also tells the user what type of data each field can hold.

-- SELECT: Select which fields should be selected
-- FROM: Indicates the table in which the fields are located
SELECT column_1
FROM sample_table;

-- Select multiple fields (columns)
SELECT column_1, column_2
FROM sample_table;

-- Select three fields
SELECT column_1, column_2, column_3
FROM sample_table;

-- Select all fields from the "sample_table" table
SELECT *
FROM sample_table;

-- Select column_1 and column_2 from "sample_table" table, rename 'column_1' to 'first_mod'
SELECT column_1 AS first_mod, column_2
FROM sample_table;

-- Select distinct records from the field column_year (no duplicates)
SELECT DISTINCT column_year
FROM sample_table;

-- All unique, no duplicate entries
SELECT DISTINCT column_1, column_year
FROM sample_table;

-- Saving SQL resulting from the SELECT statement
-- Create a view (table) called new_table
CREATE VIEW new_table AS
SELECT column_1, column_2, column_3
FROM sample_table;

-- Now you can also work with your new table
SELECT column_1, column_2
FROM new_table;

-- PostgreSQL 
-- (free and open source)
-- From sample_table, get column_1 and column_2, and only retain the top 2 records (rows)
SELECT column_1, column_2
FROM sample_table
LIMIT 2;

-- SQL Server
-- (Created by Microsoft, has both a free and a enterprise version, is queried using T-SQL)
-- From sample_table, get column_1 and column_2, and only retain the top 2 records (rows)
SELECT column_1, column_2
FROM sample_table
TOP 2;
