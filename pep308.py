# eg 1:
'''
import math
num=16
print(math.sqrt(num))
print(math.pow(2,3)) #2 to the power 3
num=9.8
print(math.floor(num))
print(math.ceil(num))    #rounding off

print(math.fabs(-5)) #give absolute value

import random
dice = random.randint(1,6) #gives random values between 1 to 6
print(dice)


student=["Rahul","Sneha","Aditya","Sumit","Prashant"]
selected=random.choice(student)
print("Congratulations!", selected)
'''

# eg 2:

import datetime
current=datetime.datetime.now() #date time both
print(current)
today=datetime.date.today() #only date
print(today)
print(current.month)
print(current.year)
d1=datetime.date(2026,1,1)
d2=datetime.date(2026,1,29)

print(d2-d1)