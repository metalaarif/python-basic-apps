#!/usr/bin/python3
# London Academy of IT
# Python Exercise 7
'''
Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)
'''
pounds = float(input("Please enter amount in pounds £"))
dollar = round(pounds * 1.30, 2)
print("£{} equals ${}".format(pounds, dollar))
