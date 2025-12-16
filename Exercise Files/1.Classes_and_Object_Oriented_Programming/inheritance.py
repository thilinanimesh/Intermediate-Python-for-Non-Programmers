# In this module will explain what is inhertitance on Python
# to explain we will get the Partent class as "Animal" and the child class as a "Dog"

import random

class Animal:
    info =  "Animal is a living organism that feeds on organic matter"

    def __init__(self):
        print("An Animal is created !!!")


class Dog(Animal): #this means that the Dog inherits from the Dog class
    
    def __init__(self,name):
    
    # # You can call the parent class init method from a child class init with the "super().__init__() "
    
        super().__init__()
    
        print("A Dog is created !!!")
        self.lucky_number = random.randint(1,10)
        self.name = name


    def bark(self):
        print(f"woof!, My name is {self.name} and my number is {self.lucky_number}")

dog1 = Dog("Shiba")

#print(dog1.info) # this case via accessing the parent variable using the child class...


# In your previous class, add a parent or a child class that then inherits from or to

class Shape:
    def __init__(self):
        print("A shape is created now !!!")
    pass


class Squre (Shape):
    sides = 4

    def __init__(self):
        self.height = 10
        super().__init__()
        print("A Squre is created !!!")

    def area(self):
        return (self.height * self.sides)
    

my_shape = Squre()
print(f"Area of my shape is {my_shape.area}")