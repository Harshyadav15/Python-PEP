# Abstraction -> 1. define rules
#                2. show what to do
#                3. hides how to do 
#                4. uses in big problem

# eg:
'''
class Parent:
    def work(self):
        pass

class Child(Parent):
    def work(self):
        print("I am working")

c1=Child()
c1.work()
'''

# Abstract class -> Method name is present
#                -> Method body is absent
#                -> Child class will complete method body

# eg:
'''
class Payment:
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print("Paid using UPI:",amount)

obj=UPI()
obj.pay(12)
'''

# Interface -> It  passes only rule class. It does not pass ready class.

# eg:
'''
class Shape:
    def draw(self):
        pass   

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

c = Circle()
c.draw()
'''

#  Example of abstract method:
'''
class Shape:
    def draw(self):
        pass    

    def info(self):
        print("This is a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

c = Circle()
c.draw()
c.info()
'''

# create  a program where an abstract class name is 'course'. 
# it has two methods 'course info' and 'duration' then you have to create a interface named as 'exam'.
# it is a method exam type.we have to make a python course which is child class of both course and exam interface .
#  use two method duration and exam type. 
class Course:
    def course_info(self):
        print("It is course")

    def duration(self):
        pass

class Exam:
    def exam_type(self):
        pass

class PythonCourse(Course, Exam):
    def duration(self):
        print("Duration is in 4 months")

    def exam_type(self):
        print("Pass the exam")

p1=PythonCourse()
p1.course_info()
p1.duration()
p1.exam_type()

