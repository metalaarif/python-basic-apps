#!/usr/bin/python3
'''
Selection Sort: Identify the smallest element and move it to front until the whole array is sorted
'''
import random
rand = int(input("Enter Range: "))
a = random.sample(range(0, 100), rand)
# a = [3, 2, 1]          # a = [8, 2, 7, 6, 5, 1]
length = len(a)
print("Unsorted >", a)

for x in range(0, length - 1):
    min_value = x
    for i in range(x + 1, length):
        if a[i] < a[min_value]:
            min_value = i
    a[x], a[min_value] = a[min_value], a[x]
    print(a)

print("Sorted  >", a)