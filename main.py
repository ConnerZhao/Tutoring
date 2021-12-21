# Python Program to Swap Two Variables input by the user
a = input("Insert variable : ")
b = input("Insert another variable : ")

temp = a 
a = b 
b = temp 

print("The vaule of a after swapping: {}".format(a))
print("The vaule of b after swapping: {}".format(b))