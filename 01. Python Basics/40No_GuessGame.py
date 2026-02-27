import numpy as np
from numpy import random
print("Welcome to the No. Guessing Game:-")
lb = int(input("Enter Lower Bound of the Game:- "))
ub = int(input("Enter Upper Bound of the Game:- "))

num = random.randint(lb,ub)


#ch = 7
turn = 0


while turn <= 7:
    if yn != num:
        yn = int(input("Guess the Number:- "))
    elif turn == 7:
        print("Sorry all chances exhausted, The number was: ", num)
    elif yn == num:
        print("Congo!, Your Guess was right")
        pass
    elif yn < num:
        print("OOPS! You Guessed a lower Number. Try Again")
    elif yn > num:
        print("OOPS! You Guessed a Bigger Number. Try Again")
    turn += 1




# Was working wrong
'''
while turn < 7:
    yn = int(input("Guess the Number:- "))
    if yn == num:
        print("Congo!, Your Guess was right")
    elif yn < num:
        print("OOPS! You Guessed a lower Number. Try Again")
    elif yn > num:
        print("OOPS1 You Guessed a Bigger Number. Try Again")
    turn += 1
print("Sorry all chances exhausted, The number was: ", num)
'''
