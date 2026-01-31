# file=open("data.txt","mode->r,w,a")
'''
file=open("students.txt","w")
file.write("Name : Rahul\n")
file.write("Course : Python \n")
file.close()

file=open("students.txt","r")
data=file.read()
print(data)
file.close()

with open("students.txt","r") as file:
    data=file.read()
    print(data)
'''
file=open("students.txt","a")
file.write("Marks : 90\n")
file.close()
