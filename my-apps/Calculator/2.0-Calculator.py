#!/bin/python3
# I'm trying my best to create a calculator from scratch.

print("###############################################")
print("###############################################")
print("     Aarif Homemade Calculator Version 2.0     ")
print("-----------------------------------------------")
print("")

print("Press 1:Addition")
print("Press 2:Substract")
print("Press 3:Multiply")
print("Press 4:Division")
print("Press 5:Modulus")
print("Press 6:Exponentiation")
print("Press 7:Floor Division")
print("Press 8:Quit")

select = int(input("Please select what you want to do from above: "))

if select == 8:
	exit()

fnum = float(input("Please input 1st number: "))
snum = float(input("Please input 2nd number: "))

if select == 1:
	print("ADDITION")
	result = str(fnum + snum)
	print("The total of {} and {} is:  ".format(fnum, snum) + result)
elif select == 2:
	print("SUBTRACTION")
	result = str(fnum - snum)
	print("The total of {} and {} is: ".format(fnum, snum) + result)
elif select == 3:
	print("MULTIPLICATION")
	result = str(fnum * snum)
	print("The total of {} and {} is: ".format(fnum, snum) + result)
elif select == 4:
	print("DIVISION")
	result = str(fnum / snum)
	print("The total of {} and {} is: ".format(fnum, snum) + result)
elif select == 5:
	print("MODULUS")
	result  = str(fnum % snum)
	print("The total of {} and {} is: ".format(fnum, snum) + result)
elif select == 6:
	print("EXPONENTIATION")
	result = str(fnum ** snum)
	print("The total of {} and {} is: ".format(fnum, snum) + result)
elif select == 7:
	print("FLOOR DIVISION")
	result = str(fnum // snum)
	print("The total of {} and {} is: ".format(fnum, snum) + result)
else:
	print("ERROR")

print("")
print("Done")

