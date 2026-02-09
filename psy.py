import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="school",
    user="postgres",
    password="nikki"
)
print("Connection done")

cur=conn.cursor()
cur.execute("""drop table if exists employee""")
cur.execute("""CREATE TABLE IF NOT EXISTS employee(id INT,name VARCHAR(50),salary INT)""")
cur.execute("""INSERT INTO employee VALUES(1,'HARSH',5000)""")
conn.commit()
cur.execute("""SELECT * from employee""")
rows=cur.fetchall()
for row in rows:
    print(row)
conn.close()