#!/usr/bin/python3
# coding selection sort using function.

def selection_sort(a):
    print("Unsorted >", a)
    for x in range(0, len(a) - 1):
        min_value = x
        for i in range(x + 1, len(a)):
            if a[i] < a[min_value]:
                min_value = i
        a[x], a[min_value] = a[min_value], a[x]
        print(a)
    return a

list = [3, 2, 1, 0]
selection_sort(list)
