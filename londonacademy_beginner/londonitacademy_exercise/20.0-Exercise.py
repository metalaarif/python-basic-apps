#!/usr/bin/python3
# London Academy of IT
# Python Exercise 20
'''
Write a program that displays matrix of integer numbers
And example runs of program
1   2   3
4   5   6
7   8   9
'''
print("*" * 50)
print("Using For Loop")
print("*" * 50)
for x in range(1, 10):
    print(x, "\t", end='')
    if x % 3 == 0:
        print("\n")
print("*" * 50)
print("Using While Loop")
print("*" * 50)
i = 1
while i <= 9:
    print(i, "\t", end='')
    if i % 3 == 0:
        print("\n")
    i += 1