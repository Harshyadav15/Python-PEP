'''
1. Generate random numbers
2. Check which number are even or odd
3. Round numbers using math
4. Count how many times numbers appear
5. Save result in the file
'''

'''
# MODULES USED
# random    -> to generate random numbers
# math      -> for rounding numbers
# collections -> to count occurrences
# os        -> to work with file system

import random
import math
from collections import Counter
import os

# 1. Generate random numbers
numbers = [random.uniform(1, 100) for _ in range(20)]  # 20 random numbers between 1 and 100
print("Random numbers:", numbers)

# 2. Check which numbers are even or odd
even_numbers = [num for num in numbers if int(num) % 2 == 0]
odd_numbers = [num for num in numbers if int(num) % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# 3. Round numbers using math
rounded_numbers = [math.ceil(num) for num in numbers]  # ceil rounds up
print("Rounded numbers (ceil):", rounded_numbers)

# 4. Count how many times numbers appear
# Rounding first for simplicity
counted = Counter(rounded_numbers)
print("Count of each rounded number:", counted)

# 5. Save result in the file
folder_name = "results"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)  # create folder if not exists

file_path = os.path.join(folder_name, "numbers_result.txt")
with open(file_path, "w") as f:
    f.write("Random numbers:\n" + str(numbers) + "\n")
    f.write("Even numbers:\n" + str(even_numbers) + "\n")
    f.write("Odd numbers:\n" + str(odd_numbers) + "\n")
    f.write("Rounded numbers:\n" + str(rounded_numbers) + "\n")
    f.write("Count of each rounded number:\n" + str(counted) + "\n")

print(f"Results saved in {file_path}")
'''

n1="Harsh"
n2="Yadav"
print(" ".join([n1,n2]))