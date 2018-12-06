#!/usr/bin/python3
# Birthday App
'''
Write a program to find your current age and if you have upcoming birthday or if it has past in this year.
'''
import datetime
print("Please enter your Birthday.")
d = int(input("Day [DD]: "))
m = int(input("Month [MM]: "))
y = int(input("Year [YYYY]: "))

current_date = datetime.datetime.now().date()

bday = datetime.date(y, m, d)

modified_date = datetime.date(current_date.year, m, d)

days = ((modified_date - current_date)).days


if days > 0:
    print("Your birthday is on {} and its {} days until your bday".format(bday, days))
elif days < 0:
    print("Your birthday is on {} and its {} past your bday".format(bday, - days))
else:
    print("Today is your Happy Birthday")