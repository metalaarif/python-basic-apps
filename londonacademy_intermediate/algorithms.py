import time

list1 = [5, 12, 34, 67, 45, 89, 234]

# Linear search ==> It will match with each of them until it matches.

def search(n):
    for x in enumerate(list1):
        if n == x[1]:
            return x[0]
    return "Not Found"

t1 = time.clock()
print(search(67))
t2 = time.clock()
t3 = t2 - t1

# Binary Search, it will sort the value in accending order

list1.sort()
print(list1)

def search2(n):
    start = 0
    end = len(list1) - 1
    while start <= end:
        mid = (start + end)
        if n == list1[mid]:
            return mid
        elif n > list1[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return "Not found"

t4 = time.clock()
print(search2(67))
t5 = time.clock()
t6 = t5 - t4
print(t6 < t3)
