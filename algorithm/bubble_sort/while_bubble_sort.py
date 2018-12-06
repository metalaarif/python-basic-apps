#!/usr/bin/python3
a = [3, 2, 1]
print("Unsorted Bubble =>", a)
length = len(a) - 1     # len(a) - 1 because it will compare list from indexes a[0] to a[length - 1]

while length >= 0:
    for i in range(length):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]     # Swapping
            print(a)

    length -= 1
print("Sorted Bubble ==>", a)