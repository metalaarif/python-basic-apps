#!/usr/bin/python3
# London Academy of IT
# Python Exercise 14
'''
Cinema Tickets is £6 but it you're less than 16 years old 50% discount if you're over 60 years old then 75% discount.
'''

age = int(input("Enter your Age: "))
cinema_ticket = 6
if age <= 16:
    print("Your Cinema Ticket price is £%d" %(cinema_ticket * 0.5 ))
elif age >= 60:
    print("Your Cinema Ticket price is £%d" %(cinema_ticket * (1 / 3)))
else:
    print("Your Cinema Ticket price is £%d" %(cinema_ticket))