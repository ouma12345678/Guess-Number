import random

number=random.randint(1,100)
guess=0

while guess != number:
    guess= int(input("What is your guess?"))

    if (guess<number):
        print("Guess higher")
    elif (guess>5°number):
        print("Guess lower")
    else:
        print("You got it !")        
