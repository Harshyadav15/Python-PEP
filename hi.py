#REVERSE A LIST
#METHOD 1 -----------> USING INBUILT REVERSE FUNCTION
'''
lst = [1,2,3,4,5]
list.reverse()
print(list)
'''
#METHOD 2------> USING SLICING
'''
lst = [1 , 2,3,4,5,6]
print(lst[::-1])
'''

#REMOVE DUPLICATE FROM A LIST



#CREATE A TUPLE AND exchange 2 AND 3 elements
#METHOD 1-----> SWAPPING
'''
tup = (1,2,3,4,5)

temp = tup[1]               #SWAPPING OF TWO ELEMENT
tup[1] = tup[2]
tup[2] = temp

print(tup)
'''

#METHOD 2-------> CONVERTING TUPLE TO LIST
'''
tup = (1,2,3,4,5)
lst = list(tup)
lst[1] , lst[2] = lst[2] ,lst[1]
tup = tuple(lst)
print(tup)
'''

#CONVERTING TUPLE TO LIST, vice versa
'''
tup = (1,2,3,4,5)
print(type(tup))

lst = list(tup)                 #TUPLE TO LIST
print(type(lst))

tup2 = tuple(lst)               #LIST TO TUPLE
print(type(tup2))

'''

# CONVERTING LIST TO SET AND VICE VERSA--------------->>> We use this to remove  duplicate element
"""
lst = [1,2,3,4,5,22,2,2,5,1]

st = set(lst)                   #list TO set
print(st)
print(type(st))

lst = list(st)                  #set TO list
print(lst)
print(type(lst))

"""


#CONVERTING DICTIONARY TO SET and VICE VERSA

'''
dict = {"hardik":12 , "rohit":13 , "rahul":14}
print(dict)

st1 = set(dict)                         #DICT(KEYS) TO SET
print(st1)


st = set(dict.values())                 #DICT(VALUES) TO SET
print(st)


st2 = set(dict.items())                 #DICT(key,value) to SET
print(st2)

'''

# SET TO DICT
'''
s2 = {'a', 'b', 'c'}

d = dict.fromkeys(s2)
print(d)

s = {1, 2, 3}

d = dict.fromkeys(s,s2 )
print(d)
'''


#---------------------------------------------------------------------------------------------------------------------------#


#EXCEPTION HANDLING IN PYTHON:

'''

THERE ARE 3 TYPES OF MAIN ERROR
1  SYNTAX ERROR
2  RUNTIME ERROR
3  LOGICAL ERROR

1 SYNTAX ERROR:  error occurs due to wrong syntax

2 RUNTIME ERROR : error occurs while program is running
 TYPE : 

| Error             | Cause              |
| ----------------- | ------------------ |
| ZeroDivisionError | Divide by zero     |
| ValueError        | Invalid value      |
| TypeError         | Wrong data type    |
| IndexError        | Index out of range |
| KeyError          | Key not found      |
| FileNotFoundError | File missing       |

            
3 LOGICAL ERROR : error run without error but output is wrong   

'''

"""
try:
    risky code
except:
    runs if error occursi

"""

# TRY, ERROR WITH DIFFERENT TYPE OF ERRORS
"""
try:
    x = 1000
    y =10
    print(x/y)
except ZeroDivisionError:
    print("0 error occured")
except ValueError:
    print("wrong value")
except RuntimeError:
    print("runtime")
except TypeError:
    print("its type error")
except IndexError:
    print("Index error")
except FileNotFoundError:
    print("No file found")
except:
    print("error")

"""

#TRY, EXCEPT, ELSE :
"""
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("error 0")
else:                                       #ONLY RUNS IF NO ERROR
    print("good")
"""

#TRY, EXCEPT, FINALLY:
"""
try:
    print(10/0)
except ZeroDivisionError:
    print("0 error")
finally:
    print("Program completed")              #RUNS EVERYTIME NO MATTER THERE IS ERROR OR NOT

"""


#------------------------------------------------------------------------------------------------------------------------#


# CREATING OWN ERROR ---------------->>>> USING RAISE
"""
age = int(input("Enter the age = "))

if age<18:
    raise ValueError("kam umar wala dur rahe")
else:
    print("u are eligible")
"""


# bank balance eg:
"""
balance = 500
withdraw = int(input("enter withdraw = "))
if withdraw> balance:
    raise LowBalanceError("balance is low")
else:
    print("Withdraw completed ")
"""


try:
    print("Outer try block")

    try:
        print(int("abc"))  # error here
    except ValueError:
        print("Inner except: ValueError occurred")

except:
    print("Outer except executed")











