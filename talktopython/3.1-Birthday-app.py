#!/bin/python3
# Creating a Birthday App
import datetime

def get_bday():
	y = int(input("Enter your DOB Year: "))
	m = int(input("Enter your DOB Month: "))
	d = int(input("Enter your DOM Day: "))
	bday_date = datetime.date(y, m, d)
	return bday_date

def compute_dates(a, b):
	modified_date = datetime.date(b.year, a.month, a.day)
	remaining_days = modified_date - b
	return remaining_days.days

def condition_dates(days):
	if days > 0:
		print("{} days until your birthday".format(days))
	elif days < 0:
		print("It has been {} days since your birthday".format(-days))
	else:
		print("It is your Happy Birthday Today")

def main():
	birth_date = get_bday()
	today_date = datetime.date.today()
	answer = compute_dates(birth_date, today_date)
	condition_dates(answer)


main()
