#!/usr/bin/python3
# Counting if a single number was repeated from a list.

a = [1, 34, 1, 4, 32, 1, 4, 56, 34, 34, 75, 34]
count = 0
for x in a:
    i = 34
    if x == i:
        count += 1
print("\n:wq%d repeated %d times" %(i, count))