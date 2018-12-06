#!/bin/python3
# I'm trying my best to create a calculator from scratch.
def header():
    print("###############################################")
    print("###############################################")
    print("     Aarif Homemade Calculator Version 5.0     ")
    print("-----------------------------------------------")
    print("")

def body():
    i = 0

    while i != 1:
        print(" \n \n Please press a number to Calculate or Press 8 to Quit: ")
        choice = ["1 Addition: ", "2 Subtraction: ", "3 Multiplication: ", "4 Division: ", "5 Modulus", "6 Exponentiation",
              "7 Floor Division"]
        for x in choice:
            print(x)

        select = int(input("Please select what you want to do from above: "))

        if select == 8:
            exit()

        fnum = float(input("1st number: \n"))
        snum = float(input("2nd number: \n"))

        if select == 1:
            result = str (fnum + snum)
            print("The total of {} and {} is: ".format (fnum, snum) + result)
        elif select == 2:
            result = str (fnum - snum)
            print("The total of {} and {} is: ".format (fnum, snum) + result)
        elif select == 3:
            result = str (fnum * snum)
            print("The total of {} and {} is: ".format (fnum, snum) + result)
        elif select == 4:
            result = str (fnum / snum)
            print("The total of {} and {} is: ".format (fnum, snum) + result)
        elif select == 5:
            result = str (fnum % snum)
            print("The total of {} and {} is: ".format (fnum, snum) + result)
        elif select == 6:
            result = str (fnum ** snum)
            print("The total of {} and {} is: ".format (fnum, snum) + result)
        elif select == 7:
            result = str (fnum // snum)
            print("The total of {} and {} is: ".format (fnum, snum) + result)
        else:
            print("ERROR")

    print("")
    print("Done")

def main():
    header()
    body()

main()