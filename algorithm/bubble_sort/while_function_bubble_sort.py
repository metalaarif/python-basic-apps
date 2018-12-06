#!/usr/bin/python3
import random
def bubble_sort(a):
    print("Unsorted => ", a)
    length = len(a) - 1  # len(a) - 1 because it will compare list from indexes a[0] to a[length - 1]

    while length >= 0:
        for i in range(length):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]  # Swapping
                print(a)
        length -= 1
    return a

rand = int(input("Enter Range: "))
list = random.sample(range(-100, 100), rand)
# list = [3, 2, 1]
print("sorted ==> ", bubble_sort(list))