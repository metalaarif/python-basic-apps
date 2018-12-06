#!/usr/bin/python3
# London Academy of IT
# Python Exercise 8
'''
Write a program that asks the user to enter his/her name, student number and email address and display it as in the example run.
'''
name = input("Enter your name: ")
numb = input("Enter your number: ")
emai = input("Enter your email address: ")

print("Hello %s, thanks for entering your details. We will send you an email on %s with subject id: %s about further information." %(name, emai, numb))
