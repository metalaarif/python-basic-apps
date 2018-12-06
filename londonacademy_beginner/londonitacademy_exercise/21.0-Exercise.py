#!/usr/bin/python3
# London Academy of IT
# Python Exercise 21
'''
Write a program that asks the use to enter his/her name and then partly encrypt and display it.
'''
i = 0
a = 1
while i == 0:
    name = input("{} try, Enter your name to encrypt: ". format(a))
    x = "*"
    len_name = len(name)
    encrypt = x * (len(name) - 2)
    print("Encrypted form is {}{}{}".format(name[0], encrypt, name[len_name - 1]))
    a += 1

# name = input("Enter your name to encrypt: ")
# x = "*"
# len_name = len(name)
# encrypt = x * (len(name) - 2)
# print("Encrypted form is {}{}{}".format(name[0], encrypt, name[len_name - 1]))