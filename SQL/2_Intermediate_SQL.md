# Intermediate SQL

- Querying databases  
- Count and view specific records  
- Understand query execution and style  
- Filtering
- Aggregate functions  

**COUNT**() - Returning the number of record with a value in a field  

Count how many birthdates are in the birthdate field, and create a new table named count_birthdate  
**SELECT COUNT**(birthdate) **AS** count_birthdates  
**FROM** people;

Using COUNT() multiple times  
**SELECT COUNT**(name) AS count_names, **COUNT**(birthdate) **AS** count_birthdates  
**FROM** people;  

Count all recoeds in a table  
**COUNT**(*)  

Count the number of distinct values in a field  
**SELECT COUNT**(**DISTINCT** birthdate) **AS** count_distinct_birthdates  
**FROM** people;

To filter, you can use the **WHERE** clause  

**WHERE** color = 'green'  

Select movie titles from the films table, and include only the movies where the release is 1960  

**SELECT** title  
**FROM** films  
**WHERE** release_year = 1960;  

- '>' Greater than or after
- '<' Less than or before
- '=' Equal to
- '>=' Greater than or equal to
- '<=' Less than or equal to
- '<>' Not equal to

**SELECT** title  
**FROM** films  
**WHERE** country = 'Japan'  
**LIMIT** 5;  

Additional keywords:  
- **OR**  
- **AND**  
- **BETWEEN**  

**SELECT** *  
**FROM** coats  
**WHERE** color = 'yellow' **OR** length = 'short';  

**SELECT** *  
**FROM** coats  
**WHERE** color = 'yellow' **AND** length = 'short'; 

**SELECT** *  
**FROM** coats  
**WHERE** buttons **BETWEEN** 1 **AND** 5; 

Use **OR** when setting multiple criteria, and only need to satisfy only one condition  
Use **AND** when setting multiple criteria, and need to satisfy multiple conditions  

**SELECT** title  
**FROM** films  
**WHERE** release_year = 1994 **OR** release_year = 2000;  
    
**SELECT** title  
**FROM** films  
**WHERE** (release_year = 1994 **OR** release_year = 1995) **AND** (certification = 'PG' **OR** certification = 'R')  
    
**SELECT** title  
**FROM** films  
**WHERE** release_year **BETWEEN** 1994 **AND** 2000;  

**SELECT** title  
**FROM** films  
**WHERE** release_year  
**BETWEEN** 1994 **AND** 2000 **AND** country = 'UK'  

Filtering text with **LIKE**, **NOT LIKE** and **IN**  
**LIKE** - Used to search for a pattern in a field  
% match zero, one or many characters  
_ match a single character  

Code below will find names beginning with the letters Ade  
**SELECT** name  
**FROM** people  
**WHERE** name **LIKE** 'Ade%';  

Code below will find names beginning with the letters Ev_ and look for anything that is only missing one character  
**SELECT** name  
**FROM** people  
**WHERE** name **LIKE** 'Ev_';  

Looking for names that do not have "A." as part of their first name  
**SELECT** name  
**FROM** people  
**WHERE** name **NOT LIKE** 'A.%';  

This will find all people, whose name ends with the letter r  
**SELECT** name  
**FROM** people  
**WHERE** name **LIKE** '%r';

This will find people whose third letter in their name is a t
**SELECT** name  
**FROM** people  
**WHERE** name **LIKE** '__t%';  

Instead of using multiple ORs, you can use **IN**:    
**SELECT** title  
**FROM** films  
**WHERE** release_year **IN** (1920, 1930, 1940);  

**SELECT** title  
**FROM** films  
**WHERE** country **IN** ('Germany', 'France');  

null = A null or missing value  

To see which names do not have a recorded birthdate in our people table
**SELECT** name  
**FROM** people  
**WHERE** birthdate **IS NULL**;  

To count the missing values for birthdate  
**SELECT COUNT**(*) **AS** no_birthdates  
**FROM** people  
**WHERE** birthdate **IS NULL**;  

To count the non-missing values for birthdate  
**SELECT COUNT**(*) **AS** count_birthdates  
**FROM** people  
**WHERE** birthdate **IS NOT NULL**  

# New aggregate functions  

** AVG(), SUM(), MIN(), MAX(), COUNT(), ROUND()**  

Average of the budget field  
**SELECT AVG**(budget)  
**FROM** films;  

Returns the sum of the budget field  
**SELECT SUM**(budget)  
**FROM** films;  

**ROUND(number_to_round, decimal_places)**  

**SELECT ROUND**(**AVG**(budget), 2) **AS** avg_budget  
**FROM** films  
**WHERE** release_year >= 2010;  

# Arithmetic  
**+, -, *, and /**  

**SELECT**(4+3);  

**SELECT** (gross - budget) AS profit  
**FROM** films  

# Sorting  

Order the budget field in ascending order  
**SELECT** title, budget  
**FROM** films  
**ORDER BY**  budget **ASC**;  

Order the budget field in descending order  
**SELECT** title, budget  
**FROM** films  
**ORDER BY**  budget **DESC**;  

Order the duration field in descending order  
**SELECT** title, duration  
**FROM** films  
**WHERE** duration **IS NOT NULL**  
**ORDER BY** duration **DESC**;  

# GROUP BY

**SELECT** certification, **COUNT** (title) AS title_count  
**FROM** films  
**GROUP BY** certification;  

**SELECT** certification , language, **COUNT**(title) **AS** title_count  
**FROM** films  
**GROUP BY** certification, language;  

**SELECT** certification, **COUNT**(title) **AS** title_count  
**FROM** films  
**GROUP BY** certification  
**ORDER BY** title_count **DESC**;  

# Filtering  

**SELECT** release_year, **COUNT**(title) **AS** title_count  
**FROM** films  
**GROUP BY** release_year  
**HAVING COUNT**(title) > 10;  

**HAVING vs WHERE**  
**WHERE** filters individual recods, **HAVING** filters grouped records  

*In what years was the average film duration over two hours?*  
**SELECT** release_year  
**FROM** films  
**GROUP BY** release year  
**HAVING AVG**(duration) > 120;
