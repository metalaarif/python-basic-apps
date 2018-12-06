import os

myfolder = os.getcwd()
file = open("radishsurvey.txt", "r")
content = file.readline()
dist = {}

for lines in content:
    print(lines)
    v1, v2 = lines.split("")
    if v2 not in dist:
        dist[v2] = 1
    else:
        dist[v2] += 1
    #lines = file.readline()

print(dist)
file.close()