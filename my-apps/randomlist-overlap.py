#!/bin/python3
# Exercise List Overlap
import random

x = random.sample(range(30), 10)
y = random.sample(range(30), 10)
z = []
print(x)
print(y)

for num in x:
	if num in y:
		z.append(num)
a = str(z)
print("Overlapping numbers are: " + a)
