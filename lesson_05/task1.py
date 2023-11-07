import random

user_number = input("Guess number from 1 to 10:\n")
if random.randint(1, 10) == user_number:
    print("Congratulations, you guess!")
else:
    print("You lost, let`s try again")
