#!/bin/python3
""" 
Writing a small app which will display list of numbers.
User input will decide to print higher numbers from the list.
"""
i = 0
while i == 0:
	num = [1, 4, 6, 8, 15, 25 ,26, 45, 52, 67, 78, 98]
	print(num)
	
	user_input = int(input("Please enter a number and to quit press 0: "))
	if user_input == 0:
		exit()
	
	new_num = []
	
	for x in num:
		if x > user_input:
			new_num.append(x)
	print(new_num)	
	print("")

