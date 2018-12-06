#!/bin/python3
# Print Random List
import random

value = int(input("Enter random list size 1-10: "))
new_list = []
y = 1
while y < value:
	x = random.randint(0, value)
	new_list.append(x)
	y += 1
print(new_list)
