import re
s1 = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem 1988 Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''

print(s1)

'''
Identifier      # what you are looking for
\w ==> looking for letters
\d ==> looking for digits
\s ==> looking for whitespaces
\. ==> looking ofr fullstop
\b ==> looking for word boundry

modifier        # what pattern(occurence) you're looking for
+ ==> one or more
* ==> zero or more
? ==> zero or one
{m,n} ==> number of
[a-e] ==> between the range
^ ==> at the begining of the string ==> it is called caret ^
$ ==> at the end of the string
| ==> or
'''

list1 = re.findall(r'\bl\w+', s1, re.I)     # re.I ==> ignore the case
print(list1)

list2 = re.findall(r'\b\d{1,4}\b', s1)  # r'\b\d',, s1
print(list2)

list3 = re.findall(r'^L\w+', s1)    # ^ also means ==> starts at the begining
print(list3)

list4 = re.findall(r'Ipsum\.$', s1) # $ also means ==> at the end
print(list4)

list5 = re.findall(r'\b[a-e|p-s]\w+\b', s1) # | means or a to e or p to s
print(list5)
print("*" * 100)
# s2 = "Python is multi purpose programming language"
# #list6 = re.search(r'(\bp\w+\b)', s2)
# print(list6)
# if list6:
#     print("It exist")
#     print(list6.span())
#     print(list6.groups())
#     print(list6.group())
# else:
#     print("doesn't exit")

s2 = "Python is multi purpose programming language"
list6 = re.match(r'Python', s2)
print(list6)
if list6:
    print("It exist")
    print(list6.span())
    print(list6.group())
else:
    print("doesn't exit")


print(re.sub("Lorem", "LOREM", s1, count=1, flags=re.I))  # default counts is 0, replaces all, 1 replaces only 1 /  flags ==> it is casesensitive bydefauult, to chage that add flag




# print(r"\n")    # r before "" means raw string
#
# print("-".join("hello world"))  # word boundry is between hello and world