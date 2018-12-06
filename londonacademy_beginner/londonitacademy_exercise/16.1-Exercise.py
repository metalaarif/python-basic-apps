#!/usr/bin/python3
# London Academy of IT
# Python Exercise 16
'''
Write a program that helps a tourist choose theatere shows. The progam should know about a series
of question about what kind of show they prefer and then gives two suggestions fro each possibility
(from atleast COMEDY, MUSICAL and HORROR).
'''


comdey = input("Would you like to see a comedy (yes / no): ")
if comdey == "yes":
    print("You  might like either Yes Minister or SPAMalot")
else:
    musical = input("Would you like to see a musical (yes / no): ")
    if musical == "no":
        print("You might like either The woman in black or macbeth")
    else:
        print("You might like either Les miserables or mama mia")

