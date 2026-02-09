
import sqlite3
'''
connection1=sqlite3.connect("School.db")
print("Database connected")
connection1.close()
'''

'''
connection1=sqlite3.connect("School.db")
cur=connection1.cursor()
print("Cursor created")
connection1.close()
'''

'''
connection1=sqlite3.connect("School.db")
cur=connection1.cursor()
cur.execute("""CREATE TABLE students (id INTEGER, name TEXT, marks INTEGER)""")
connection1.commit()
connection1.close()
'''

'''
connection1 = sqlite3.connect("School.db")
cur = connection1.cursor()
cur.execute("""INSERT INTO students values(1,"Harsh",78)""")            
cur.execute("""INSERT INTO students values(2,"Raman",87)""")
cur.execute("""INSERT INTO students values(3,"Rahul",97)""")
connection1.commit()
connection1.close()
'''

'''
connection1=sqlite3.connect("School.db")
cur=connection1.cursor()
cur.execute("""select * from students""")
rows=cur.fetchall()
for rows in rows:
    print(rows)
connection1.close()
'''

'''
connection1 = sqlite3.connect("Bank.db")
print("DataBase Created")
cur = connection1.cursor()
print("Cursor created")
cur.execute("""drop table if exists employee""")
cur.execute("""CREATE TABLE employee(id INTEGER ,name TEXT ,salary INTEGER)""")
cur.execute("""INSERT INTO employee VALUES(1,"Harsh",12)""")
cur.execute("""INSERT INTO employee VALUES(2,"Roman",13)""")
cur.execute("""INSERT INTO employee VALUES(3,"Rahul",14)""")
cur.execute("""SELECT * FROM employee""")
rows = cur.fetchall()
for i in rows:
    print(i)
connection1.commit()
connection1.close()
'''


connection1 = sqlite3.connect("school.db")
cur = connection1.cursor()

# Drop key
cur.execute("""drop table if exists employee""")

# Create and insert key
cur.executescript("""
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    emp_id INTEGER,
    emp_name TEXT,
    emp_salary INTEGER
);

INSERT INTO EMPLOYEE VALUES
(101,'HARSH',8000),
(102,'AMIT',6000);
""")


# Update, Alter, Delete Key
cur.execute("""UPDATE EMPLOYEE SET emp_salary = emp_salary + 5000 WHERE emp_id = 102""")
cur.execute("""ALTER TABLE EMPLOYEE add column emp_dept TEXT""")
cur.execute("""DELETE FROM EMPLOYEE WHERE emp_id=102""")

# Select Key
cur.execute("SELECT * FROM EMPLOYEE")
rows = cur.fetchall()
for row in rows:
    print(row)

connection1.commit()
connection1.close()



