# eg 1:
'''
from collections import Counter
fruit=['mango','orange','banana','apple']
count=Counter(fruit)
print(count)

text='Hello'
count=Counter(text)
print(count)

sentence='Python is easy and python is powerful'
sentence=sentence.split()
count=Counter(sentence)
print(count)

number=[1,2,2,3,1,3,4,1,3]
count=Counter(number)
print(count)
'''

# eg 2:

import os
current_path=os.getcwd()
print(current_path)
items=os.listdir()
print(items)


import os
foldername="my folder"
if not os.path.exists(foldername):
    os.mkdir(foldername)
    print("Folder created successfully")
else:
    print("Folder is already present there.")
