import random

print("     Welcome to Guess the Number Game")

rnum = random.randint(0,50)
guess = -99
i = 0

while i < 5:
    guess = int(input("Guess the number: "))
    if guess > rnum:
        print("{}, is wrong, please go lower".format(guess))
    elif guess < rnum:
        print("{}, is wrong, please go higher".format(guess))
    else:
        print("{}, Congrats that's the right number".format(guess))
    i += 1
print("The End")
