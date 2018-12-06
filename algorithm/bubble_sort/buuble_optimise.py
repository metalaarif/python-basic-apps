#!/usr/bin/python3
import random
rand = int(input("Enter Range: "))
list = random.sample(range(-100, 100), rand)
print("Unsorted Bubble =>", list)
length = len(list) - 1
swap = 1
while swap > 0:
    swap = 0
    for i in range(length):
        if list[i] > list[i+1]:
            list[i], list[i + 1] = list[i + 1], list[i]
            swap += 1
print("Random Sorted => ", list)

