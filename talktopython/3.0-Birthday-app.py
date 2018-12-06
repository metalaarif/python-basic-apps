#!/bin/python3
# Creating a Birthday App
import datetime

y = int(input("Enter your DOB Year: "))
m = int(input("Enter your DOB Month: "))
d = int(input("Enter your DOM Day: "))

bday_date = datetime.date(y, m, d)
today_date = datetime.date.today()
modified_date = datetime.date(today_date.year, m, d)
total = modified_date - today_date
days = int(total.days)

if days > 0:
    print("{} days until your birthday".format(days))
elif days < 0:
    print("It has been {} days since your birthday".format(-days))
else:
    print("It is your Happy Birthday Today")
