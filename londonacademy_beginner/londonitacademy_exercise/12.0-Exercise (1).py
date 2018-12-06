#!/usr/bin/python3
# London Academy of IT
# Python Exercise 12
'''
Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year
'''
# m = int(input("Enter the Month from 1 - 12: "))
# month_data = {
#         1: "January",
#         2: "Febuary",
#         3: "March",
#         4: "April",
#         5: "May",
#         6: "June",
#         7: "July",
#         8: "August",
#         9: "September",
#         10: "October",
#         11: "November",
#         12: "December"
#         }
# if m in month_data:
#     print("Month %d, is %s" %(m, month_data[m]))
# else:
#     print("Opps {}, is not associated with any months".format(m))

listm = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

m = int(input("Enter the month: "))

print("Month of %d is %s" %(m, listm[m-1]))
