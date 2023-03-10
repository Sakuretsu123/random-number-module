#!python3
import random 

def strength() :
    x1 = random.randrange(1,7)
    x2 = random.randrange(1,7)
    x3 = random.randrange(1,7)
    return [x1, x2, x3]


def intelligence() :
    x1 = random.randrange(1,7)
    x2 = random.randrange(1,7)
    x3 = random.randrange(1,7)
    return [x1, x2, x3]


def wisdom() :
    x1 = random.randrange(1,7)
    x2 = random.randrange(1,7)
    x3 = random.randrange(1,7)
    return [x1, x2, x3]


def dexterity() :
    x1 = random.randrange(1,7)
    x2 = random.randrange(1,7)
    x3 = random.randrange(1,7)
    return [x1, x2, x3]


def constitution() :
    x1 = random.randrange(1,7)
    x2 = random.randrange(1,7)
    x3 = random.randrange(1,7)
    return [x1, x2, x3]


def charisma() :
    x1 = random.randrange(1,7)
    x2 = random.randrange(1,7)
    x3 = random.randrange(1,7)
    return [x1, x2, x3]

charisma1 = charisma()
strength1 = strength()
intelligence1 = intelligence()
wisdom1 = wisdom()
dexterity1 = dexterity()
constitution1 = constitution()

print("Here is your character caracteristics, hope you like it.")
print(f"{sum(charisma1)} charisma") 
print(f"{sum(strength1)} strength") 
print(f"{sum(intelligence1)} intelligence") 
print(f"{sum(wisdom1)} wisdom") 
print(f"{sum(dexterity1)} dexterity") 
print(f"{sum(constitution1)} constitution") 




