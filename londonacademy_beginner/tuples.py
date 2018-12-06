t1 = (3, 45, 24, 34 , 45)
t2 = (3, 45, "london")

print(t1)
print(t2)

print(len(t1))
print(len(t2))

print(max(t1))
print(min(t1))

print(t1 * 3)
print(t1 + t2)

print(t1[2])
print(t1[:4])

# t1.sort() # doesn't work in tuple because it is not changeable.
print("*" * 100)
list1 = list(t1) # Tuple can't be sorted so, we convert tuple to list
list1.sort(reverse=True) # reverse it
t1 = tuple(list1) # convert list to tuple
print(t1) # print tuple
print("*" * 100)

for x in t1:
    print(x)

print(45 in t1)
print(3 not in t1)



