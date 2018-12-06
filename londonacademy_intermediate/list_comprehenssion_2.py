import functools

def square(n):
    return n ** 2

def even(n):
    return n % 2 == 0

def sum(x, y):
    return x + y

def compare(x, y):
    return x if x > y else y


list1 = list(map(square, range(1, 21))) # map ==> transform the value using the provided function
print(list1)

list2 = list(filter(even, range(1, 21))) # filters the value using the provided funtion and inserts in a list if the function returns true
print(list2)
#
# list2 = list(map(even, range(1, 21))) # check what map does
# print(list2)

x = functools.reduce(sum, range(1, 11), 20) # reduce added all the number from 1 to 10
                        # range (1, 11), 20 is the start value
print(x)

list3 = [4, 34, 4, 82, 23, 33, 34, 92, 3, 5]
y = functools.reduce(compare, list3)    # comparing and reducing to single value
print(y)

list4 = list(map(lambda x: x ** 2, range(1, 21)))   # lambda can be only used in list comprehension
print(list4)

z = functools.reduce(lambda x, y : x if x > y else y, list3)
print(z)
# OR, we can do it below way,
# we can use lambda instead of functions
expr = lambda x, y : x if x > y else y
z = functools.reduce(expr, list3)
print(z)