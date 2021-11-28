'''
using while loop
find all odd number from 1 to 100
find the sum of all odd number from 1 to 100
'''
# Reference:
currentNumber = 0
total = 0 # Init the var
while currentNumber != 100:
    currentNumber += 1
    total += currentNumber
    print("Current number: " + str(currentNumber))
    print("Sum: " + str(total))