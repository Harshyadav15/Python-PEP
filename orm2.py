from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
# step 1
engine=create_engine("sqlite:///company.db")

print("Database connected")


# step 2
Base=declarative_base()

# step 3
class Employee(Base):
    __tablename__="employees"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    department=Column(String)

# step 4
Base.metadata.create_all(engine)

# step 5
Session=sessionmaker(bind=engine)
session=Session()
e1=Employee(name="Harsh",age=21,department="HR")
e2=Employee(name="Nikki",age=20,department="IT")
session.add(e1)
session.add(e2)
session.commit()

# step 6
employees=session.query(Employee).all()

print("Employee added")
# for i in employees:
#     print(i.id,i.name,i.age,i.department)

employees=session.query(Employee).filter_by(id=1).first()
employees.name="Gian"
session.commit()
print('Employee updated')
employees=session.query(Employee).all()
for i in employees:
    print(i.id,i.name,i.age,i.department)
