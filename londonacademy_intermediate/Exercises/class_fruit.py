#!/usr/bin/python3

class Fruit:
    '''
    Fruit
    '''
    def __init__(self, name, colour, flavour, poisonous):
        self.name = name
        self.colour = colour
        self.flavour = flavour
        self.poisonous = poisonous

    def printInfo(self):
        print("I am a %s and I taste %s" %(self.name, self.flavour))

    def is_edible(self):
        if self.poisonous == "poisonous":
            print("Don't Eat me! I am super %s" %(self.poisonous))
        else:
            print("I am Edible")


obj = Fruit("Dragonfruit", "Pink", "Sweet", "non-poi")
obj.printInfo()
obj.is_edible()

obj1 = Fruit("Apple", "red", "Sweet", "non-poi")
obj1.printInfo()
obj1.is_edible()

obj2 = Fruit("Nettle", "Green", "Bitter", "poisonous")
obj2.printInfo()
obj2.is_edible()