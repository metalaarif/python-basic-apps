def addNumber():    # def - define and function name # follow convetion of lower case of camel case
    print(5 + 10)

def addNumbers2(a, b): # fucntion with required arguments or parameters
    print(a + b)

def addNumbers3(a, c, b = 20, x = 10, y = 20):     # function is having a as compulsory and b optional parameters  # can have any number of option paaramters
    print(a + b + c - x - y)

def addNumber4(a, b): # the first line is known as funtion signature.
    return a + b

def addNumbers5(*values):   # variable argument, can pass any number of arguments
    print(type(values))
    sum = 0
    for x in values:
        sum += x
    return sum

def addNumbers6(**values):  # keyword arguments
    print(type(values))
    sum = 0
    for k, v in values.items():
        sum += v
    return sum

MYVARIABLE = 10     # global variable and it will always be in uppercase, conventionwise

def changeValue():
   # global MYVARIABLE   # refer the global variable in a function, if we don't do that it will always print 10
    MYVARIABLE = 50
    print(locals())
    print(MYVARIABLE)

# addNumber()         # calling a function
# addNumbers2(35, 10)
# addNumbers3(15, 10, 22, 12)
# print(addNumber4(10, 20))
# x = addNumber4(10, 40)
# print(x)
# print("*" * 100)
# print(addNumbers5(2, 2, 2, 2))
# print("*" * 100)
# print(addNumbers6(a = 10, b = 20, c = 40))