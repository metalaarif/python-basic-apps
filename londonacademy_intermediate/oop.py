class Employee:     # Pascal case, for each word, 1st letter should be capital
    '''This class processes employee data'''    # documentation string, can't use hash inside class
    __noOfEmployees = 0   # generic variable, in python generic variable first then specific and doubtle underscore makes variable private and it is accesible withint the class only

    def __init__(self, id, name, email): # initalisation or constructor method which is triggered when the object is created, it is also known as magic methods

        self.id = id    # internally self becomes e1.id
        self.name = name    # self becomes e1.name
        self.email = email
        Employee.__noOfEmployees += 1 # generic or class variable

    def printData(self):    # self means current object or holds
        print("Id is %d and Name is %s and email is %s" %(self.id, self.name, self.email))

    @classmethod    # decorator
    def printNoOfEmployees(cls):    # remove self and make it cls
        print("number of employee %d" % (Employee.__noOfEmployees))

    def __del__(self):  #destructor, called implicitly when object is removed from the stack
        Employee.__noOfEmployees -= 1


if __name__ == "__main__":  # will execute only codes in this program
    # x = 5           # datatype int which means object of class int
    # print(type(x))
    e1 = Employee(1000, "Aarif", "aarif@gmail.com") # e1  is an object of employee class # datatype is empployee
    e1.printData()
    # print(type(e1))    # <class '__main__.Employee'>
    e2 = Employee(1001, "Dragon", "dragon@gmail.com")
    e2.printData()
    Employee.printNoOfEmployees()
    del e2
    Employee.printNoOfEmployees()
    #
    # print("*" * 100)
    # print(Employee.__module__)
    # print(Employee.__name__)
    # print(Employee.__bases__)   # parent class
    # print(Employee.__dict__)
    # print(Employee.__doc__ )