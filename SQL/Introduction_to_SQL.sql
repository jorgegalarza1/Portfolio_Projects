-- Rows = records
-- Rows are unlimited
-- Columns = fields
-- Columns are set when the dataset was created

-- Select all fields
SELECT *
-- From the 'books' table
FROM books

-- VARCHAR is a flexible and popular string data type in SQL
-- INT is a flexible and popular integer data type in SQL
-- NUMERIC is a flexible and popular float data type in SQL
-- DATE is a flexible and popular date data type in SQL
-- A schema (blueprints) what tables are stored in the database and any relationship between its table
    -- It also tells the user what type of data each field can hold.

-- SELECT: Select which fields should be selected
-- FROM: Indicates the table in which the fields are located
SELECT name
FROM patrons;

-- Select multiple fields (columns)
SELECT card_num, name
FROM patrons;

-- Select three fields
SELECT name, card_num, total_fine
FROM patrons;

-- Select all fields from the "patrons" table
SELECT *
FROM patrons;

-- Select name and year_hired from employees table, rename 'name' to 'first_name'
SELECT name AS first_name, year_hired
FROM employees;

-- Select distinct records from the field year_hired (no duplicates)
SELECT DISTINCT year_hired
FROM employees;

-- All unique, no duplicate entries
SELECT DISTINCT dept_id, year_hired
FROM employees;

-- Saving SQL resulting from the SELECT statement
-- Create a view called employees_hire_years
CREATE VIEW employees_hire_years AS
SELECT id, name, year_hired
FROM employees

SELECT id, name
FROM employees_hire_years

-- PostgreSQL (free and open source)
SELECT id, name
FROM employees
LIMIT 2;

-- SQL Server (Created by Microsoft, has both a free and a enterprise version, is queried using T-SQL)
SELECT id, name
FROM employees
TOP 2;
