list1 = [5, 34, 23, 12, 23]
list2 = [5, 23, "london"]
print(list1)
print(list2)
print(len(list1)) # count of the values, values are called as elements
print(len(list2))
print("*" * 100)
print(max(list1)) # max and min works only homogeneous, either int or str
print(min(list1))
#print(max(list2))
print(list1 * 2) # no matter what it will replicates not multiply
list3 = [x*2 for x in list1]
print(list3)
print(list1 + list2) # no matter what it will combine not add
# Slicing: nit is called slicing, taking part of the list.
print(list1[0])
print(list1[0:3]) # it will exclude last value, so it will print 0 1 2 only, it will exlude printing 3
print(list1[-1]) # if we do -1 it will start from end or from last or it starts print from right not left
print(list1[-3:-1]) # it will print only -1 and -2, it will exclude -3
print(list1[2:])   # starting from 2nd element it will print all
print(list1[:3]) # print from start upto 2nd element
print(list1)
# Slicing

for x in list1: # this is how you can retrieve elements from list
    print(x)

for x in enumerate(list1): # gives you value as well as position.
    print(x)

print("*" * 100)

list1.append(100) # it will add a value at the end., you can add only single value or element
print(list1)

list1.insert(2, 555) # it will add at specific position and adds only 1 value at a time.
print(list1)

list1.extend([333, 444, 555]) #to add multiple value or elements you use extend.
print(list1)

list1.append([222, 666, 999]) # entire list is added as a single element within a list.
print(list1)

list1[-1] = 44 # replaced the entire list of last value
print(list1)

list1.pop() # pop removes the element at the end. appends adds, pop removes
print(list1)

x = list1.pop() # removed variable is assigned to x
print(x)

list1.pop(4) # if position is specified it will removed that element.
print(list1)

list1.remove(444) # it removes the element specified. unlike pop removes the position.
print(list1)

del list1[0] # it deleted the first element.
print(list1)

del list1[0:4] # can be used to delete range of values
print(list1)

list1.reverse() # it reverses the elements or you can say flips the order
print(list1)

list1.sort() # it will sort and default order is ascending.
print(list1)

list1.sort(reverse=True) # it will descend now, by default reverse is False.
print(list1)

# How to find a element or value in list

print(40 not in list1)