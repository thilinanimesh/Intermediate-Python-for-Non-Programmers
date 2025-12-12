class Pencil:

    def __init__(self, price):
        self.price_ = price

    colour = "RED"
    size = "Medium"
    sharpness = 10

    info = "This is a {0} Pencil with {1} size, and sharpness = {2},".format(colour,size,sharpness)

    def alterInfo(self):
        self.info = f"{self.info} and the price is : {self.price_}"
        print(self.info)


my_pencil = Pencil(100)
print(my_pencil.info)
my_pencil.alterInfo()

### we also can set a defualt value on the init method

class Squre:
    sides = 4

    def __init__(self):
        self.height = 0

    def area(self):
        return self.height * self.height
    
my_shape = Squre()
my_shape.height = 5
print(my_shape.area())

my_shape_1 = Squre()
print(my_shape_1.area())