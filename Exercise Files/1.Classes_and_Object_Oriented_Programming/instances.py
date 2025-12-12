# An example of a class in Python
class Dog:
    info = "They're carnivores, part of the Canidae family (with foxes, coyotes, wolves), have fur, paws with pads and claws, and communicate with barks and tail wags. "

    def __init__(self):

        print("I am alive !!!")


# below are the instances that will be created from the Dog class as above, when a Dog instance is instanciated the "init" function will run
# Basically we are creating four instaces of Dog class as below
Dog()
Dog()
Dog()
Dog()


# Whatever your previous class was,
# make an instance of it and iadd an instance variable/attribute to it

class Pencil:

    def __init__(self, price):
        self.price_ = price

    colour = "RED"
    size = "Medium"
    sharpness = 10

    info = "This is a {0} Pencil with {1} size, and sharpness = {2}.".format(colour,size,sharpness)

print(Pencil(50).info)
print(Pencil(100).price_)