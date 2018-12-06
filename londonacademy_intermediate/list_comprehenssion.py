# list1 = []
# for x in range(1, 101):
#     list1.append(x)
# print(list1)

# list2 = [x for x in range(1, 101)]
# print(list2)
#
# list3 = [x ** 2 for x in range(1, 21)]
# print(list3)

list4 = [x for x in range(1, 21) for y in range(2, x) if x % y == 0]
print(set(list4))   # finding prime numbers

list5 = list(set(list4))
list6 = [x for x in range(1, 21) if x not in list5]
print(list6)    # finding non-prime numbers

list7 = ["aarif", "dragon", "metal"]
list8 = [name[0].upper() for name in list7]
list9 = [{name:len(name)} for name in list7]
list10 = [("C#", 2000), ("Go", 2010), ("python", 1980), ("C", 1972)]
list11 = [ name for name, year in list10 if year >= 2000]

print(list7)
print(list8)
print(list9)
print(list11)

''' LIST acts as Stack
append
insert
extend
pop - list1.pop() list.pop(2)
remove  - list1.remove("abc")
'''

list12 = [5, 10, 15, 20, 30, 5]
#list12.remove(5)   # it will remove only the first occurance
list12= [x for x in list12 if x != 5]
print(list12)