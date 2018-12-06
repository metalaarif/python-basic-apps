#!/bin/python3
i = 0

while i != 1:
	value = int(input("Please enter a number or enter 0 to exit: "))

	if value == 0:
		exit()
	elif value % 2 == 0:
		print("%d is Even number" %(value))
	else:
		print("%d is Odd number" %(value))
