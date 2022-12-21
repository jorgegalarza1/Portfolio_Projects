# Introduction to SQL

Chapter 1 - Understand databases and their structures  
Chapter 2 - Extract data from databases using SQL  

**Relational database** - Defines relationships between tables of data inside the database  

Database advantages:  
	* More storage than spreadsheet applications  
    * Storage is more secure  
    * Many users can write queries to gather insights from the data at the same time  
    
SQL - Structured Query Language (most widely used programming language for databases) 

**Records** == Rows  
**Fields** == Columns  

Fields are set when the database was created.  
Records have no limit  

Table names should be lowercase and should not include spaces (_), and can refer to a collective group or can be plural.  

Field names should be lowercase and should not include spaces (_), and should be singular, rather than plural, fields cannot be repeated in a table, nor use the table's name.  

Unique identifiers are used to identify records in a table, they are unique and are often numbers

# SQL data types & keywords

**VARCHAR** - STRING - Letters or punctuation  
**INT** - INTEGER - Whole numbers  
**NUMERIC** - FLOAT - Numbers that include a decimal point  

**SELECT** - Select which fields should be selected  
**FROM** - Table in which these fields are located  

Select name fields from patrons table  
**SELECT** name  
**FROM** patrons;  

Select card_num and name from patrons table  
**SELECT** card_num, name  
**FROM** patrons;

To select all fields in the patrons table  
**SELECT** *  
**FROM** patrons;

Aliasing to rename columns  (replace name, for first name, and select year_hired as well)  
**SELECT** name **AS** first_name, year_hired  
**FROM** employees;  

Selecting distinct records, with no repeat values  
**SELECT DISTINCT** year_hired  
**FROM** employees;  

**SELECT DISTINCT** dept_id, year_hired  
**FROM** employees;  

Saving SQL result sets as employee_hire_years  
**CREATE VIEW** employee_hire_years **AS**  
**SELECT** id, name, year_hired  
**FROM** employees;  

Selecting the top 10 results from the below query  
**SELECT** genre  
**FROM** books  
**LIMIT** 10;  

OR  

**SELECT** genre  
**FROM** books  
**TOP** 10; 
