x = int(19)
y = int(578)
n = x + y # Answer
print("What is " + str(x) + " + " + str(y) + " = ?")
userInput = int(input("Enter answer here: "))
numberOfTrials = 1

while numberOfTrials != 3:
    if (userInput == n):
        print("Correct")
        break
    else:
        print("Incorrect")
        print("You have attempted " + str(numberOfTrials) + " times")
        numberOfTrials += 1
        userInput = int(input("Enter answer here: "))