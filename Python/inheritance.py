# Author: Rohtash Lakra
import inspect
import random


# Animal Class
class Animal:

    # static variable 
    info = "Animals are multicellular, eukaryotic organisms in the biological kingdom Animalia."

    # Constructor
    def __init__(self, name, color):
        print(f"{inspect.stack()[0][3]}{name, color}")
        self.name = name
        self.color = color
        self.weight = random.randint(1, 100)

# Dog Class
class Dog(Animal):

    # static variable 
    info = "The dog is a domesticated descendant of the wolf. Also called the domestic dog, it is derived from extinct gray wolves, and the gray wolf is the dog's closest living relative."

    # Constructor
    def __init__(self, name, color):
        print(f"{inspect.stack()[0][3]}{name, color}")
        super().__init__(name, color)
        self.pet = True
        self.fur = ""
        # self.weight = random.random()

    def bark(self):
        print(f"Woof! I'm {self.name} of {self.color} color. I'm {self.weight}lb.")




class BullDog(Dog):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.pet = False



# instance the class object
my_dog = Dog("Barnaby", "White")
sarah_dog = Dog("Benton", "Black")
print("\n")
print(my_dog.info)
print("\n")
# print(f"A {my_dog.name} is of {my_dog.color} color and has {my_dog.weight} weight.")
my_dog.bark()
print("\n")
# print(f"A {sarah_dog.name} is of {sarah_dog.color} color and has {sarah_dog.weight} weight.")
sarah_dog.bark()
print("\n")


# instance the class object
bullDog = BullDog("BullDog", "Grey")
bullDog.bark()
print("\n")



# Shape Class
class Shape:

    def __init__(self, title, type="Shape", sides=0):
        self.title = title
        self.type = type
        self.sides = sides
        self.width = 0.0
        self.height = 0.0

    def area(self):
        return self.width * self.height

# Square Class
class Square(Shape):

    def __init__(self, title):
        super().__init__(title, "Square", 4)


# Circle Class
class Circle(Shape):

    def __init__(self, title):
        super().__init__(title, "Circle", 0)


# instance the Shape class object
circle = Circle("Circle")

rectangle = Shape("Rectangle", "Rectangle", 4)
rectangle.width = 24.8
rectangle.height = 3.23

square = Square("Square")
square.height = 4.23

print("\n")
print(f"A {circle.title} is of {circle.area()}")
print("\n")
print(f"A {rectangle.title} is of {rectangle.area()}")
print("\n")
print(f"A {square.title} is of {square.area()}")
print("\n")