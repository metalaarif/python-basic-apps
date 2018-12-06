class Shape:
    def getSides(self, sides = 2):                  # it is called method overloading (falls under polymorphism)
        self.length = float(input("Enter Length: "))
        if sides  == 2:
            self.width = float(input("Enter Width: "))

class Rectangle(Shape):
    def calculateArea(self):
        return self.length * self.width

class Square(Shape):
    def calculateArea(self):
        return self.length ** 2

print("Rectangle")
r1 = Rectangle()
r1.getSides()
print("Area of Rectangle is %.2f" %(r1.calculateArea()))
print("Square")
r2 = Square()
r2.getSides(1)
print("Are of Square is %.2f" %(r2.calculateArea()))


