import random #make computer smarter
x = random.randint(0,10) # generates a random number between a, b (0, 10)
z = int(input("Guess the number(0 to 10): ")) # Initial input
# Checks if the user inputted a valid response
while not((z <= 10) and (z >= 0)): # Condition checking, if the user's input fits the parameter
    print("Overflow, try again")
    z = int(input("Guess the number(0 to 10): ")) # Try again
# Actual guessing part
while z != x:
    if x > z:
        print("Too low")
        z = int(input("Guess the number(0 to 10): ")) # Try again
    elif x < z:
        print("Too high")
        z = int(input("Guess the number(0 to 10): ")) # Try again


'''
Computer Guessing game
have the computer guess a number you are thinking
between 0 to 10
the computer will ask if its response is too high or too low
USE GOOGLE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''