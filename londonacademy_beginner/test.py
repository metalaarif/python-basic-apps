#!/usr/bin/python3
'''
Counting number if its repeated multiple times in a list and removing duplicates.
Without using count() method
'''

# Create a random list not using random module
a = [1, 45, 32, 56, 76, 43, 1, 45, 3, 67, 76, 98, 5, 1, 43, 76, 45, 98, 56]

# Convert list to set and back to list and declaring it to b
b = list(set(a))

# Calculating the length of list a and declaring the length to c
c = len(b)

# Creating a blank dictionary which can be used to count number and its repetition.
d = {}

# Creating a count variable which will count the repetition
count = 0

# Creating a i value for looping
i = 0

# First we will start with while loop where i value is less than c
while i < c:
    # creating a for loop of a which we will use x to compare
    for x in a:
        # we are comparing x with b
        if x == b[i]:
            # count +1 if the same number exist
            count += 1
            # update the x value and count to d
            d.update({x: count})
    # once it searches for repetition it will come out of if statement, come out of for loop and increase i +1
    i += 1
    # reseting the count value to 0 so that it will again count for next value which comparing
    count = 0

# once all loop is finish d has all the update value and .item() method can be used to extract key and value from dict
for k, v in d.items():
    print("%d is repeated %d times" %(k, v))

'''
This is using .count() method, its much more simpler and easier.
'''
# a = [1, 45, 32, 56, 76, 43, 1, 45, 3, 67, 76, 98, 5, 1, 43, 76, 45, 98, 56]
# b = list(set(a))
# c = {}
# for x in b:
#     i = a.count(x)
#     c.update({x: i})
#     # c[x]= a.count(x)
#
# for k, v in c.items():
#     print("%d is repeated %d times" %(k, v))