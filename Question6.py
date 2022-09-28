#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
#   Keep the game going until the user types “exit”
#   Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
def myprog():
    a=random.randrange(1,10)
    b=0
    n=0
    while b != a and b != "exit":
        b=input("Guess a number, if you want to end the game, type exit ")
        if b=="exit":
            print(f"You guessed {n} times!")
            break
        n += 1
        if int(b) > int(a):
            print("Your guess was too high, try again ")
        elif int(b) < int(a):
            print("Your guess was too low, try again ")

myprog()
