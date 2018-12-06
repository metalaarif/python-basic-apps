#!/usr/bin/python3

a = "*"
for x in range(5):
    print(" " * (5 - x - 1), end='')
    print(a * (x + 1))