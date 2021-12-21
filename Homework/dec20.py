'''
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
Computer Guessing game
have the computer guess a number you are thinking
between 0 to 10
the computer will ask if its response is too high or too low
USE GOOGLE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
import random # Imported Random 

guess = int(input("Enter a number 0-10: ")) # Gave directions to start the game - Asking for input
computerguess = random.randint(0,10) # Computer is generating a random number
counter = 0 # Init counter variable
while 10<=guess>=1: # Check if the number is between 1 and 10 Inclusive - Check if given value falls under parameter
    guess = int(input("Enter a number 0-10: ")) # If it does not fall under the parameter, another input is prompted

while computerguess != guess: # While computer's guess does not equal to given value, the program enters a guessing state

    print("The computer's guess is: {}".format(computerguess))

    if computerguess>guess: # Checks if the computer value is higher than the given
        print("Too high, try again")
        counter = counter + 1 #Changing variable to add 1 
        print("{} tries".format(counter))
        computerguess = random.randint(0, 10) 
    elif computerguess<guess: # Checks if the computer value is lower than the given
        print("Too low, try again.")
        counter = counter + 1 
        print("{} tries".format(counter))
        computerguess = random.randint(0, 10)

    if computerguess == guess:
        print("The computer guessed {} times".format(counter))
        print("The computer's guess is {} Correct! The number was {}".format(computerguess,computerguess))