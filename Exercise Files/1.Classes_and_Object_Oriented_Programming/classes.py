# An example of a class in Python
class Dog:
    info = "They're carnivores, part of the Canidae family (with foxes, coyotes, wolves), have fur, paws with pads and claws, and communicate with barks and tail wags. "

print(Dog.info)

# Create a class for something around you in the room.
# Create a class variable inside the class

class Pencil:
    colour = "RED"
    size = "Medium"
    sharpness = 10
    info = "This is a {0} Pencil with {1} size, and sharpness = {2}.".format(colour,size,sharpness)

print(Pencil.info)