#!/usr/bin/python3
import random

def rand():
    rand = int(input("Enter Range: "))
    list = random.sample(range(-100, 100), rand)
    return list

def bubble_sort(a):
    print("Unsorted => ", a)
    length = len(a) - 1  # len(a) - 1 because it will compare list from indexes a[0] to a[length - 1]

    for x in range(length):
        for y in range(length - x):
            if a[y] > a[y + 1]:
                a[y], a[y + 1] = a[y + 1], a[y]  # Swapping
                print(a)
    return a

def main():
    print("Sorted ==>", bubble_sort(rand()))

main()
