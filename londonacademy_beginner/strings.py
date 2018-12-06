s1 = '''london is capital of united kingdom'''
print(s1)

print(len(s1)) # it counts the spaces too

print(s1.count("i")) # it counted just "i" within the string

print(s1.find("i")) # it will find the first position of "i"

print(s1.find("i", 8)) # it will find the first position of "i" starting from 8th position.

print(s1.find("i", 8, 12)) # if "i" or element doesn't exist it will give -1

print(s1.find("i", 8, 14)) # now it will give the position of "i"

print(s1.replace("o", "x"))

print(s1) # string is not changeable as well just like tuples
print("*" * 100)

print(s1.upper())  # changes to whole content to uppercase

print(s1.lower())    # changes whole content to lowercase

print(s1.capitalize())  # change first alphabet of sentence only capital

print(s1.title())  # make first alphabet of each word capital.

print("*" * 100)

# Boolean Value, it will give True or False only.
print(s1.startswith("london"))
print(s1.startswith("London"))
print(s1.startswith("m"))
print(s1.endswith("kingdom"))
print(s1.endswith("Kingdom"))

print("*" * 100)
# Slicing in string
print(s1[5])
print(s1[6:15]) # from position 6 to 15 excluding 15, space is counted as a character that's why it print weird.

print("*" * 100)
''' Split we need to provide parameter or else by default it will spilt whitespace (space) and
note:- it will count space too
'''

print(s1.split()) # splits strings and creates a list and it will split from space by default

print(s1.split("i")) # it splits from i only and not from space.

s2 = "united,kingdom,london"
print(s2.split(","))  # splitting from coma

v1, v2, v3 = s2.split(",") # splitting variable to 2 variables.
print(v1) # first one was given to v1
print(v2) # second one was given to v2
print(v3) # third one was given to v3

print(s1.replace(" ", "-")) # it replaced space with "-" hyphen
print("-".join(s1)) # joining each word with hyphen "-", it doesn't even leave space.

# Word boundry, check this will work in regular expression. regex

s3 = "level"
print(s3.lstrip("l")) # it removes the left not in between
print(s3.rstrip("l")) # it removes the right not in between
print(s3.strip("l")) # it removes both sides not in between
print(s3.strip()) # defaults removes the "\n" line break,

# Boolean
print(s3.isalpha()) # checking if it is alphabet
print(s3.isdigit()) # checking if it is numeric
print(s3.isalnum()) # checking if there is alphanumeric, can use during password

'''
why did we do like this???
len(s1) # function is generic
max(s1) # function
s1.upper() # method is specific
s2.lower() # method
if we are using with . then it is method for ex: s1.upper()
but if we use len(s1) then it is function.
'''
