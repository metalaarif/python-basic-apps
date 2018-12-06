#!/usr/bin/python3
# London Academy of IT
# Python Exercise 22
'''
Write a program tthat asks the user for two whole number Celsius calues, and then prints a Celsius/Fahrenheit conversion
chart for all whole number Celsius values between (and including( the two values entered. You can use C to F conversion.
The formula: F = C * 9/5 + 32
'''
c = [int(input("Enter 1st number: ")), int(input("Enter 2nd number: "))]
print ("Celsius  \t Fahrenheit")
for x in range(c[0], c[1] +1):
    print(" %d \t \t %.1f" %(x, (x * (9 / 5) + 32)))

