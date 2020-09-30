"""A number-guessing game."""
#import random function randint
from random import randint

print("Welcome to the Guessing Game!")
name = input("What is your name? ")
randnum = randint(1, 100)
game_active = True
num_guesses = 0

#repeat forever:
#create while loop
while game_active == True:
    #ask for guess
    try:
        playernum = int(input("Guess a number: "))
        if playernum < 1 or playernum > 100:
            print("How dare you select a num out of range! Try again!")
        else:
            #check if guess is correct
            if playernum != randnum:
                num_guesses += 1
                if playernum > randnum:
                    print("Your guess is too high.")
                else:
                    print("Your guess is too low.")
            #if guess is incorrect:
                #give hint and increment number of guesses
            #if guess is correct
            else:
                num_guesses += 1
                game_active = False
                print(f"Well done, {name}! You've found my number in {num_guesses} amount of valid and invalid tries!")
                #congratulate player
    except ValueError:
        num_guesses += 1
        print("That's not a valid number. Please put an integer.")
    
        