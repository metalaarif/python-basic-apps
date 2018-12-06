import sys
a = 5
print(sys.getrefcount(5))
b = 5
print(sys.getrefcount(5))
list1 = [5, 10, 15, 5]
print(sys.getrefcount(5))

class Test:
    def __init__(self):
        self.x = 5

t1 = Test()
t2 = Test()

print(sys.getrefcount(5))
print(id(t1) == id(t2))
print(id(t1.x) == id(list1[-1]))

print(id(t1.x))
print(id(list1[-1]))

del t2
print(sys.getrefcount(5))