#!/usr/bin/python3
# London Academy of IT
# Python Exercise 13
'''
Write a program that reads an integer value from the user and prints output whether it is odd or even
'''

num = int(input("Enter a number to find if it is Even or Odd: "))
if num % 2 == 0:
    print("%d is Even" %(num))
else:
    print("%d  is Odd" %(num))
