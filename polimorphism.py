# Poly -> Many
# morphy -> Form

# eg:
'''
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a1 = Dog()
a2 = Cat()

a1.sound()
a2.sound()
'''

#create a class person with a method roll, then create two class student  and teacher , student prints im student and teacher prints im teacher

class Person:
  def  role(self):
    print("person")
class Teacher(Person):
  def role(self):
    print("I am a teacher") 
class Student(Person):
  def role(self):
    print("I am a student")
class Assistant(Student,Teacher):
  pass
obj=Assistant()
obj.role()    
