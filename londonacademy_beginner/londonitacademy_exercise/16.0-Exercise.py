#!/usr/bin/python3
# London Academy of IT
# Python Exercise 16
'''
Write a program that helps a tourist choose theatere shows. The progam should know about a series
of question about what kind of show they prefer and then gives two suggestions fro each possibility
(from atleast COMEDY, MUSICAL and HORROR).
'''
i = 0
yes = "yes"
no = "no"
while i == 0:
    comedy = input("Would you like to see a comedy (yes / no): ")
    if comedy == yes:
        print("You might like either Yes Minister or SPAMalot")
        continue
    if comedy == no:
        musical = input("Would you like to see a musical (yes / no): ")
        if musical == yes:
            print("You might like either Les Miserables or Mamma Mia")
            break
        if musical == no:
            horror = input("Would you like to see a horror (yes / no): ")
            if horror == yes:
                print("You might like either The Woman in Black or Macbeth")
                break
            else:
                print("There is no Suggestions left")
                break
print("Done")

