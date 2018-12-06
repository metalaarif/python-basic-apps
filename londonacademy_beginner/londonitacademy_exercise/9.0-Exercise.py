#!/usr/bin/python3
# London Academy of IT
# Python Exercise 9
'''
Write a program that asks the user to enter his/her born year and it prints the year you are born and your age in 2020
'''
b_year = int(input("Enter the dob year only [YYYY]: "))
c_year = int(input("Enter the current year in [YYYY]"))
print("You were born in %d and you are %d years old." %(b_year, c_year - b_year))
f_year = int(input("Enter the future year to check your age [YYYY]: "))
print("In the year %d, you will be %d years old." %(f_year, f_year - b_year))
