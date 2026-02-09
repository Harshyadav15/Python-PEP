# import create_engine to connect the database
'''
from sqlalchemy import create_engine
engine=create_engine("sqlite:///school.db")

# sql llite database
# file name is school.db
# will be created if not exist

print("Database connected")
'''

# ORM    --> object relational mapping(connection)
# Table  --> class
# rows   -->  object
# column --> variable

# import declarative base


from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
# step 1
engine=create_engine("sqlite:///school.db")

print("Database connected")


# create base class
# step 2
Base=declarative_base()

# base will be parent of all model
# step 3
class Student(Base):
    __tablename__="Student"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    course=Column(String)

# create all tables defined using base
# step 4
Base.metadata.create_all(engine)

# step 5
Session=sessionmaker(bind=engine)
session=Session()
s1=Student(name="Harsh",age=21,course="Python")
s2=Student(name="Nikki",age=20,course="BPT")
session.add(s1)
session.add(s2)
session.commit()
student=session.query(Student).all()

print("Student added")
for i in student:
    print(i.id,i.name,i.age,i.course)
    
