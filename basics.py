import re
'''
text="cat cot cut"
result=re.findall("c.t",text)
print(result)

text ="Hello hello"
print(bool(re.search("^Hello",text)))
print(bool(re.search("^World",text)))

text ="Hello hello"
print(bool(re.search("Hello$",text)))
print(bool(re.search("World$",text)))

text="helooooo"
result=re.findall("lo",text)
print(result)
'''

# 0 or 1 time(?)
'''
text="color colour"
result=re.findall("colou?r",text)
print(result)
'''

# character set([])
'''
text="apple ball cat"
result=re.findall("[abc]",text)
print(result)
'''

# Digits([0-9])
'''
text="My age is 20"
result=re.findall("[0-9]",text)
print(result)
'''

# Large Alphabets
'''
text="My age is 20"
result=re.findall("[A-Z]",text)
print(result)
'''

# Small Alphabet
'''
text="My age is 20"
result=re.findall("[a-z]",text)
print(result)
'''

# Alphabets([a-z])
'''
text="My age is 20"
result=re.findall("[A-za-a]",text)
print(result)
'''

# Non digit(\D)
'''
text="My age is 20"
result=re.findall("\D",text)
print(result)
'''

# Words(\)
'''
text="My age is 20"
result=re.findall("\w",text)
print(result)
'''

# not words(\W)
'''
text="My age is 20"
result=re.findall("\W",text)
print(result)
'''

# Space(\s)
'''
text="My age is 20"
result=re.findall("\s",text)
print(result)
'''

# not space(\S)
'''
text="My age is 20"
result=re.findall("\S",text)
print(result)
'''

# Grouping(())
'''
text="abab ab"
result=re.findall("(abc)+",text)
print(result)
'''

# eg 1:
'''
mobile="6367701597"
pattern="^[0-9]{10}$"
if re.match(pattern,mobile):
    print("Valid mobile number")
else:
    print("Invalid number")
'''

# eg 2: Extract all the emal id's from that string
'''
text = "Contact us at test@gmail.com or support@company.org. You can also reach out to admin@yahoo.in."
pattern = r"[\w.-]+@[\w.-]+\.\w+"
emails = re.findall(pattern, text)
print(emails)
'''

# eg 3: Extract number
'''
text="Order123 price45 quantity6"
result=re.findall("[0-9]",text)
print(result)
'''

# eg 4: Validate a strong password
'''
-> Atleast 8 digit character 
-> one uppercase = (?=.*[a-z])
-> one lowercase = (?=.*[A-Z])
-> one digit = (?=.*\d)
-> one special character = (?=.*[@$!*?&])
'''
'''
password="Harsh@12"
pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!*?&]).{8,}$"

if re.match(pattern,password):
    print("Valid pasword")
else:
    print("Invalid password")
'''

# eg 5:
'''
text=input("enter a pan number: ")
pattern=r"^[A-Z]{5}\d{4}[A-Z]$"
pan_number=re.match(pattern,text)
if pan_number:
    print("valid pan number")
else:
  print("Invalid pan number")
pan_number =re.findall(pattern,text)
for pan_number in pan_number:
  print(pan_number)
'''

# eg 6:

text=input("enter a IPV4 address: ")
pattern=r"^[0-9]{1,3}+\.[0-9]{1,3}+\.[0-9]{1,3}+\.[0-9]{1,3}$"
ipv4_address=re.match(pattern,text)
if ipv4_address:
    print("valid IPV4 address")
else:
  print("Invalid IPV4 address") 
ipv4_address=re.findall(pattern,text)
for ipv4_address in ipv4_address:
  print(ipv4_address)


