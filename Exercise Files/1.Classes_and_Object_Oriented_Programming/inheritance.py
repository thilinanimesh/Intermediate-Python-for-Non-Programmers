# In this module will explain what is inhertitance on Python
# to explain we will get the Partent class as "Animal" and the child class as a "Dog"

import random

class Animal:
    info =  "Animal is a living organism that feeds on organic matter"


class Dog(Animal): #this means that the Dog inherits from the Dog class
    
    def __init__(self,name):
    #    super().__init__() 
    # # you have the chance to override the suuper class constructor, but in this case we will use our own one to simplycity purpose
        print("I am alive  !!!")
        self.lucky_number = random.randint(1,10)
        self.name = name


    def bark(self):
        print(f"woof!, My name is {self.name} and my number is {self.lucky_number}")

dog1 = Dog("Shiba")

print(dog1.info) # this case via accessing the parent variable using the child class...


