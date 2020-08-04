import random

number = (random.randint(1, 10))

guess1 = int(input("Take a guess: "))

while guess1 != number:
    if guess1 == number:
        print("You guessed right!")
    else:
        print("Wrong!")
        if guess1 < number:
            print("Number is higher")
            guess1 = int(input("Take a guess: "))
        else:
            print("Number is lower")
            guess1 = int(input("Take a guess: "))

print("you're correct")

