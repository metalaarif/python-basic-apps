#!/bin/python3
i = 0
while i == 0:
	user_value = int(input("please enter a number or press 0 to exit: "))
	if user_value == 0:
		exit()

	number = list(range(1, user_value +1))
	
	new = []

	for x in number:
		if user_value % x == 0:
			new.append(x)
	print(new)
