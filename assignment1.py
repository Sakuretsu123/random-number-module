#! python3

# SD Computing Studies Assignment

#computer generate number from 1 to 100
#player try to guess and computer say if too high or too low
#play continues till player guess the number 
#then the game end and computer says how many tries it took
import random



x = random.randrange(100) 

guess = int(input("What is your guess ?"))
countdown = 0

if guess > 100 and guess < 0 : 
    print("the guess cant be over 100 and under 0")


while guess != x :
    countdown = countdown + 1 
    if guess > x : 
            print("the number is smaller than your guess. Try again !")
            guess = int(input("what is your guess ??"))
    elif guess < x : 
        print("the number is greater than your guess. Try again !")
        guess = int(input("what is your second guess ??"))

if guess == x and countdown == 0: 
    print("WOOWWWWWW IMPRESSIVE ! FIRST TRY")
elif guess == x : 
        print(f"You guessed the correct number in {countdown} tries !!!")

    




