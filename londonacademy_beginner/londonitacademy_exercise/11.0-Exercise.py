#!/usr/bin/python3
# London Academy of IT
# Python Exercise 11
'''
Write a program that asks the user to enter his/her full name and the program process and manupulate the text of his/her name.
'''
f_name = input(("Enter your Firstname: "))
l_name = input(("Enter your Lastname: "))
print("Your fullname is %s %s." %(f_name.upper(), l_name.upper()))
print("Your initials are {} {}".format(f_name[0].upper(), l_name[0].upper()))
print("Your firstname length is %d letter" %(int(len(f_name))))
print("Your lastname length is %d letter" %(int(len(l_name))))
print("Your fullname length is %d letter" %(int(len(f_name) + int(len(l_name)))))
print("First name starts with %s" %(f_name[0].upper()))
print("First name ends with {}" .format(f_name[int(len(f_name)) -1].upper()))
print("Last name starts with %s" %(l_name[0].upper()))
print("Last name ends with %s" %(l_name[int(len(l_name)) - 1].upper()))
print("First name Indexes are 0 - %d" %(int(len(f_name) - 1)))
print("Last name indexes are 0 - %d" %(int(len(l_name) - 1)))
#print("First name trims 1
