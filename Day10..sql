/*
database : database is used to store data

2 type |------>RDBMS (relational database) ------->mysql
       |------>NRDBMS (Non relational database)---->MongoDB

relational database =  store data in form of tables

non relational database = store data in form of key and values for mongo db


1 : 
MySQL : MySQL is an open-source RDBMS.
-> It stores data in tables and uses SQL for data operations.


*/

-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

CREATE DATABASE school;													-- creates database
use school;																-- tell SQL to use this database	

-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

-- TABLE STUDENT :		
create TABLE students(													-- creates a table
id INT,
name VARCHAR(50),
roll_no INT);

INSERT INTO students VALUES(1,"Hardik",56);								-- insert values in table
SELECT * FROM students;													-- shows the table as output 

-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

-- TABLE CLASS : 
create table class(
id INT,
name VARCHAR(50),age INT,course VARCHAR(100),marks INT);

INSERT INTO class VALUES(1,"akash",19,"Python",95);
SELECT * FROM class;

-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

SELECT * from class order by marks desc;					-- arranges in ascending or descending order
select avg(marks) from class;								-- avg of all the marks
select min(marks) from class;								-- minimun of all the marks
select sum(marks) from class;								-- sum of all the marks
select max(marks) from class;								-- maximum of all the marks 				
select count(marks) from class;								-- counts the num of rows 

-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

-- Checking condition : 

 select * from class where marks>80;

--  and : 
select * from class where id = 1 and marks = 87;			-- check the condition	if both satify give result

-- or :
select * from class where id = 8 or name = "Hardik";		-- check the condition	if one satify give result		
 
 -- between :
select * from class where marks between 50 and 80;			-- return all values between two values
	
-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
-- deleting column in table

DELETE FROM class where marks = 78;														-- not working

delete from class;

-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

-- limit in sql 

select * from class where marks>80 limit 2 ;										-- give 2 element with marks greater than 80
	
select * from class order by marks desc limit 2;									-- gives last 2 element 

-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

-- updating marks in table :

update class set marks = 32 where id=1;												-- not working

-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

/*
Diffrence between delete , truncate and drop
-- DELETE                               | TRUNCATE                                 | DROP
--------------------------------------------------------------------------------------------------------------
delete selected rows                    | delete all the data                      | delete whole table		  |
WHERE clause allowed                    | no where           					   | no where 				  |
row by row deletion                     | deletes data at once                     | deletes data + structure |
table structure exists                  | table structure exists                   | table does not exist     |
rollback possible                       | rollback not possible                    | rollback not possible    |
slow                                    | fast                                     | fastest				  |
-------------------------------------------------------------------------------------------------------------

*/

select course,avg(marks) from class group by course;		 		-- group by course
 
insert into class VALUES(5,"Karan",12,"Java",87);				-- insert 1 more column

select course,age,avg(marks),max(marks) from class group by course ,age;	-- group by course,age


-- ------------------------------------------------------------------------------------------------------------------------------------ --
/*
Q Employee table 

select * from Employee;
+--------+----------+-------------+--------+-------------+--------+------------+
| emp_id | emp_name | department  | gender | city        | salary | Experience |
+--------+----------+-------------+--------+-------------+--------+------------+
|      1 | Hardik   | AI          | male   | haldwani    |  50000 |          1 |
|      2 | Rohit    | ML          | male   | khatima     |  80000 |          2 |
|      3 | Garima   | Datascience | female | pithoragarh | 100000 |          3 |
|      1 | Rahul    | IT          | Male   | Delhi       |  70000 |          5 |
|      2 | Anita    | HR          | Female | Mumbai      |  50000 |          4 |
|      3 | Aman     | IT          | Male   | Delhi       |  90000 |          8 |
|      4 | Neha     | Finance     | Female | Pune        |  60000 |          6 |
|      5 | Rohit    | IT          | Male   | Mumbai      |  75000 |          5 |
|      6 | Priya    | HR          | Female | Delhi       |  48000 |          3 |
|      7 | Vikas    | Finance     | Male   | Pune        |  65000 |          7 |
|      8 | Sneha    | IT          | Female | Bangalore   |  85000 |          6 |
|      9 | Arjun    | HR          | Male   | Mumbai      |  52000 |          4 |
|     10 | Kavya    | Finance     | Female | Delhi       |  72000 |          8 |
+--------+----------+-------------+--------+-------------+--------+------------+


Q department wise avg salary ?

mysql> select department,avg(salary) as avg from employee group by department;


+-------------+-------------+
| department  | avg         |
+-------------+-------------+
| AI          |  50000.0000 |
| ML          |  80000.0000 |
| Datascience | 100000.0000 |
| IT          |  80000.0000 |
| HR          |  50000.0000 |
| Finance     |  65666.6667 |
+-------------+-------------+


Q city wise total salary expense  ?

mysql> select department ,count(gender) as male_count from employee where gender="male" group by department;
+------------+------------+
| department | male_count |
+------------+------------+
| AI         |          1 |
| ML         |          1 |
| IT         |          3 |
| Finance    |          1 |
| HR         |          1 |
+------------+------------+


mysql> select city,sum(salary) as expense from Employee group by city;
+-------------+---------+
| city        | expense |
+-------------+---------+
| haldwani    |   50000 |
| khatima     |   80000 |
| pithoragarh |  100000 |
| Delhi       |  280000 |
| Mumbai      |  177000 |
| Pune        |  125000 |
| Bangalore   |   85000 |


mysql> select department,city,avg(salary) as avg from employee group by department,city;
+-------------+-------------+-------------+
| department  | city        | avg         |
+-------------+-------------+-------------+
| AI          | haldwani    |  50000.0000 |
| ML          | khatima     |  80000.0000 |
| Datascience | pithoragarh | 100000.0000 |
| IT          | Delhi       |  80000.0000 |
| HR          | Mumbai      |  51000.0000 |
| Finance     | Pune        |  62500.0000 |
| IT          | Mumbai      |  75000.0000 |
| HR          | Delhi       |  48000.0000 |
| IT          | Bangalore   |  85000.0000 |
| Finance     | Delhi       |  72000.0000 |
+-------------+-------------+-------------+


mysql> select department,avg(salary) as avg_salary from Employee where salary>60000 group by department;
+-------------+-------------+
| department  | avg_salary  |
+-------------+-------------+
| ML          |  80000.0000 |
| Datascience | 100000.0000 |
| IT          |  80000.0000 |
| Finance     |  68500.0000 |
+-------------+-------------+


mysql> select department,count(emp_id) as emp_count from Employee where salary>60000 group by department;
+-------------+-----------+
| department  | emp_count |
+-------------+-----------+
| ML          |         1 |
| Datascience |         1 |
| IT          |         4 |
| Finance     |         2 |
+-------------+-----------+
4 rows in set (0.00 sec)

*/


