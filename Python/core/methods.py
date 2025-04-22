# Author: Rohtash Lakra
import inspect
import random

class Dog:

    def __init__(self, name, color):
        print(f"{inspect.stack()[0][3]}{name, color}")
        self.name = name
        self.color = color
        self.weight = random.randint(1, 100)
        # self.weight = random.random()

    def bark(self):
        print(f"Woof! I'm {self.name} of {self.color} color. I'm {self.weight}lb.")


# instance the class object
my_dog = Dog("Barnaby", "White")
sarah_dog = Dog("Benton", "Black")
print("\n")
# print(f"A {my_dog.name} is of {my_dog.color} color and has {my_dog.weight} weight.")
my_dog.bark()
print("\n")
# print(f"A {sarah_dog.name} is of {sarah_dog.color} color and has {sarah_dog.weight} weight.")
sarah_dog.bark()
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



# instance the Shape class object
circle = Shape("Circle")
rectangle = Shape("Rectangle", type="Rectangle", sides=4)
rectangle.width = 24.8
rectangle.height = 3.23
square = Shape("Square", type="Square", sides=4)
print("\n")
print(f"A {circle.title} is of {circle.area()}")
print("\n")
print(f"A {rectangle.title} is of {rectangle.area()}")
print("\n")
print(f"A {square.title} is of {square.area()}")
print("\n")