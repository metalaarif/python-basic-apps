#!/usr/bin/python3
import random
class BubbleAlgorithm:
    '''
    Optimised Bubble Sort Algorithm
    '''

    def __init__(self, a, rand):
        self.a = a
        self.rand = rand

    def sort_bubble(self, a):
        print("Unsorted => ", a)
        length = len(a) - 1  # len(a) - 1 because it will compare list from indexes a[0] to a[length - 1]
        swap = 1
        while swap > 0:
            swap = 0
            for i in range(length):
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    swap += 1
        return a

rand = int(input("Enter Range: "))
a = random.sample(range(-100, 100), rand)
obj = BubbleAlgorithm(a, rand)
print("Sorted ==>", obj.sort_bubble(a))