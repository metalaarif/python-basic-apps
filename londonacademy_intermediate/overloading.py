class Employee:
    def __init__(self, salary):
        self.salary = salary

    def  __add__(self, other):              # This is called overloading
        return Employee(self.salary + other.salary)

    def __str__(self):
        return str(self.salary)

e1 = Employee(5000)
e2 = Employee(10000)
e3 = Employee(15000)
print(e1 + e2 + e3)

'''
__add__ addition
__sub__ subtract
__mul__ multiplication
__truediv__ true division
__floordiv__ floor division
__lt__ <
__le__ <=
__gt__ >
__ge__ >=
__eq__ =
__neq__ !=
__pow__ power
__mod__ modulus

'''