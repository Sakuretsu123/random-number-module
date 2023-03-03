#!python3 
import random 
 
 #toss toin and then ask to guess 



x = random.randrange(2)

guess = str(input("Heads or Tails ? \n"))
myList = ["Heads", "Tails"]


if guess not in myList: 
    print("invalid input, make sure to use cap or that you entered the right word")

if "Heads" in guess and x == 1: 
    print("Yay Heads ! you guessed correctly")
elif "Heads" in guess and x == 0: 
    print("Nay..Tails.. you guessed incorrectly")
elif "Tails" in guess and x == 1: 
    print("Nay...Heads.. you guessed incorrectly")
elif "Tails" in guess and x ==0: 
    print("Yay Tails ! you guessed correctly")
else:
    print()
