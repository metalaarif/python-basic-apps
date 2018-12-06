#!/usr/bin/python3

class Calculator:
    '''
    Basic Calculator using Class
    '''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return a + b
    def sub(self):
        return a - b
    def mul(self):
        return a * b
    def div(self):
        return a / b

print("\t \tCalculator: \nSelect number to perform calculation.")
select = int(input("0 Exit\n1 Add\n2 Sub\n3 Mul\n4 Div "))
if select == 0:
    exit()
a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))
obj = Calculator(a, b)
if select == 1:
    print("%d + %d = " %(a, b), obj.add())
elif select == 2:
    print("%d - %d = " %(a, b), obj.sub())
elif select == 3:
    print("%d * %d = " %(a, b), obj.mul())
elif select == 4:
    print("%d / %d = " %(a, b), obj.div())
else:
    print("Invalid Input - Error Detected")

print("Thanks Now!")