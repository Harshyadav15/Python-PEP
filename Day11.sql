/*

Primary Key : not null + unique
-> one primary key per table

not null : value should be there,allows duplicate

unique : no duplicate values allwed

default : provides predefined value if no value is provided

check : check if it mets provided condition 

foreign key = if we have 2 table ,table 1 and table 2 and table 1 refrencing table 2 using foreign key that foreign key will be primary key of table 1 

syntax : 

Table 2 (PARENT)           Table 1 (CHILD)
----------------           ----------------
dept_id (PRIMARY KEY) <-- dept_id (FOREIGN KEY)


FOREIGN KEY (student_id) refrences table1(student_id)

*/

create database db;
use db;
create table abc(id INT PRIMARY KEY, name varchar(50) NOT NULL , phone_no int UNIQUE);

alter table abc											-- TO UPDATE THE FEATURES OF TABLE
modify phone_no BIGINT;
insert into abc values(4,"devansh",7676823889);
select * from abc;

update abc												-- TO UPDATE THE VALUES OF TABLE
set name = "Pankaj",
phone_no = 8894939304
where id = 3;


/*
create a table
*/
create table student(student_id INT primary key,name VARCHAR(50) , age INT );
create table table2(name_id INT primary key,student_id INT , subject VARCHAR(50) , marks INT,foreign key (student_id) references student(student_id));

insert into student values(1,"Hardik",19);

insert into table2 values(119,4,"SQL",72);

select * from student;
select * from table2;

drop table student;

create table table1(emp_id INT primary key,emp_name VARCHAR(50) unique,emp_city VARCHAR(50) not null);

create table table3(department_id INT primary key,emp_id INT ,department varchar(50) not null,salary INT ,FOREIGN KEY (emp_id) references table1(emp_id),check (salary>50000 AND salary<60000));

insert into table1 values(4,"Akash","Patna");
select* from table1;
insert into table3 values(104,4,"IT",59000);
select *from table3;


-- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --


/* 

																					JOIN
inner join = gives common between two table (intersection).
left join = left table full + common from both
right join = common from both + right table full
full join = both table + common from both tables

*/

-- 																				JOINING OF TWO TABLES

select t1.emp_name,t3.salary from table1 t1 join table3 t3
on t1.emp_id = t3.emp_id;



CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50),
    amount INT
);

INSERT INTO customers VALUES
(1, 'Aman', 'Delhi'),
(2, 'Riya', 'Mumbai'),
(3, 'Kabir', 'Delhi'),
(4, 'Neha', 'Pune'),
(5, 'Arjun', 'Bangalore'),
(6, 'Simran', 'Mumbai'),
(7, 'Rahul', 'Delhi'),
(8, 'Pooja', 'Chennai'),
(9, 'Vikas', 'Pune'),
(10, 'Anita', 'Bangalore');

INSERT INTO orders VALUES
(101, 1, 'Laptop', 60000),
(102, 1, 'Mouse', 1500),
(103, 2, 'Mobile', 30000),
(104, 3, 'Keyboard', 2500),
(105, 3, 'Monitor', 12000),
(106, 5, 'Tablet', 20000),
(107, 6, 'Laptop', 65000),
(108, 7, 'Mobile', 28000),
(109, 7, 'Earphones', 2000),
(110, 11, 'Camera', 40000);

SELECT * FROM customers;
select * from orders;


-- show coustomer name,product ,amount from table1 and table 2

select t1.customer_name,t2.product,t2.amount from customers t1 join orders t2
on t1.customer_id = t2.customer_id;


-- show coustomer from delhi who placed order

select t1.customer_name,t2.product from customers t1 join orders t2
on t1.customer_id = t2.customer_id
where city ="Delhi";

-- 1 show all order even they have no customer

SELECT t2.order_id, t2.product, t2.amount, t1.customer_name
FROM customers t1
RIGHT JOIN orders t2
ON t1.customer_id = t2.customer_id;


-- 2 find order with no matching customer
SELECT t2.order_id, t2.product, t2.amount FROM customers t1 RIGHT JOIN orders t2
ON t1.customer_id = t2.customer_id
WHERE t1.customer_id IS NULL;


-- 3 show all coustomer and order?													

SELECT t1.customer_name, t2.product, t2.amount
FROM customers t1
LEFT JOIN orders t2
ON t1.customer_id = t2.customer_id
UNION
SELECT t1.customer_name, t2.product, t2.amount
FROM customers t1
RIGHT JOIN orders t2
ON t1.customer_id = t2.customer_id;


-- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
























