"""
Requirements:
if conditions
casting
string concatenation
inputs
outputs
"""

# Reference: https://www.w3schools.com/python/python_conditions.asp

# user input name

# user input age

# if greater or equal to 18
    # output username is an adult

# else 
    # output username is not an adult

name = input("Enter a your name: ")
print("Hello", name+ "!")
age = input("Enter your age: ")

if (int(age) >= 18):
    print(name,  "is an adult")
elif (int(age) < 18):
    print(name, "is not an adult")