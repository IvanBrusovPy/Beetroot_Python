import random

string = input("Write a word:\n")
for i in range(5):
    for l in string:
        print(string[random.randint(0, len(string)-1)], end="")
    print("\n")