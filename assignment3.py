#!python3
import random

x = random.randrange(3)

guess = str(input("Rock Paper Scissors ? \n"))
myList = ["Rock", "Paper", "Scissors"]


if guess not in myList: 
    print("invalid input, make sure to use a cap or that you entered the right word")

if "Rock" in guess and x == 0: 
    print("Scissors, win")
elif "Rock" in guess and x == 1: 
    print("Rock, tie")
elif "Rock" in guess and x == 2: 
    print("Paper, lose")
elif "Paper" in guess and x == 0: 
    print("Scissors, lose")
elif "Paper" in guess and x == 1: 
    print("Rock, win")
elif "Paper" in guess and x == 2: 
    print("Paper, tie")
elif "Scissors" in guess and x ==0: 
    print("Scissors, tie")
elif "Scissors" in guess and x == 1: 
    print("Rock, lose")
elif "Scissors" in guess and x == 2: 
    print("Paper, win")
else:
    print()

#0 is scissors 1 is rock 2 is paper