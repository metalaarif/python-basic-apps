#!/usr/bin/python3
# London Academy of IT
# Python Exercise 3

''' 
Write Python code that displays the number from 1 to 5 as steps.
for example:
1
    2
        3
            4
                5
'''
for x in range(1, 6):
    print("\t" * (x - 1), x)

