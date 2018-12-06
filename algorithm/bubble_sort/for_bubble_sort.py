#!/usr/bin/python3
import random
rand = int(input("Enter Range: "))
 a = random.sample(range(-100, 100), rand)
a = [12, 45, 76, 9, 78, 65, -90, 98, 5432, 43, -32, -45, 65, 1, 23, 0, 65, -989, 49]
print("Unsorted Bubble =>", a)
length = len(a) - 1         # len(a) - 1 because it will compare list from indexes a[0] to a[length - 1]

for x in range(length):
    '''
    "a[0] to a[length - x]" because every time it compares it swaps the largest value to the end and after every 
    iteration x will increase "a[0] to a[length - 1]" and "a[length -2]" and soon on till it sorts all.  
    '''
    for y in range(length - x):
        if a[y] > a[y + 1]:
           a[y], a[y + 1] = a[y + 1], a[y]  # Swapping
print("Sorted Bubble ==>", a)
