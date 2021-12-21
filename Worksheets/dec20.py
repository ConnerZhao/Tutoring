import random # import random mod 

playGame = 'y' # Sets playgame to yes - the program will run
dirn = 'N' # User guidance for the computer 
lowest = 1 # Variable for lowest possible value
highest = 100 # Variable for highest possible value

bottom = lowest # Holder value
upper = highest # Holder value

while playGame == 'y': # Checks if the user wants to play the game

    bottom = lowest # Only needed if the user wants to play again
    upper = highest # Only needed if the user wants to play again
    dirn = 'N' # Only needed if the user wants to play again

    print("Guess a number (1 to 100)") # Prompt computer gives to the user that the game has bottomed
    try_num = random.randint(lowest,highest) # Generates a random number
    print(try_num) # Prints the random number
    counter = 0 # Number of attempts

    while dirn != 'C': # Continues to guess as long the computer does not guess it correctly
        dirn = input("Is it too large?(L) Too Small?(S) Correct?(C): ") # Prompts the user for a response to guide the computer

        if dirn == 'S' or dirn == 's': # if the generated number is too small 
            if try_num > bottom: 
                bottom = try_num + 1
            try_num = random.randint(bottom,upper)
            print(try_num)

        if dirn == 'L' or dirn == 'l': # if the generated number is too large 
            if try_num < upper:
                upper = try_num - 1
            try_num = random.randint(bottom,upper)
            print(try_num)
        counter += 1

    print("The computer guesses correctly")
    print("The computer took {} tries".format(counter))
    playGame = input("Repeat? (y or n): ")