#!/bin/python3

# Here I'll be performing 2nd task from talktopython video tutorial, without looking at it.
import random

print("-----------------------------------------------")
print("          Welcome to Random Number Game        ")
print("-----------------------------------------------")

x = random.randint(0,100)
guess = -9
name = input(" Hey Man!, what's your name? ")

while guess != x:
    guess = int(input("{} man!, Guess a number between 0 and 100: ".format(name)))

    if guess > x:
        print("{0} man, the number {1}, is not the right number, please go lower".format(name, guess))
    elif guess < x:
        print("{0} man, the number {1}, is not the right number, please go higher".format(name, guess))
    else:
        print("Perfect! {} man, you said the right number".format(name))

print("Done")
