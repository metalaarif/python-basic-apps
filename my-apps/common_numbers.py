#!/usr/bin/python3
'''
Write an app to find which numbers are repeated from a list
and how many times they are repeated and which haven't been repeated.
'''

x = [1, 34, 21, 4, 32, 1, 4, 56, 23, 24, 75, 34]
y = [1, 23, 34, 4, 56, 6, 98, 75]
z = []
print("X is {}".format(x))
print("Y is {}".format(y))
for num in x:
    if num in y:
        z.append(num)
print("*" * 100)
print("common nums are: {}".format(z))
a = set(z)
print("common without duplicates are {}".format(a))


