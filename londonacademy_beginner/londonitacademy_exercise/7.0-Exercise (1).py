#!/usr/bin/python3
# London Academy of IT
# Python Exercise 7
'''
Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)
'''
pounds = float(input("Please enter amount in pounds £"))
dollar = float(pounds * 1.30)
print("£%.2f equals $%.2f" %(pounds, dollar))
