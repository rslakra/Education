# Author: Rohtash Lakra
import inspect
import random

class Dog:
    # static variable 
    info = "The dog is a domesticated descendant of the wolf. Also called the domestic dog, it is derived from extinct gray wolves, and the gray wolf is the dog's closest living relative."

    def __init__(self, name, color, brand):
        print(f"{inspect.stack()[0][3]}{name, color, brand}")
        self.id = random.randint(1, 100)
        self.name = name
        self.color = color
        self.brand = brand
        # print("Initialzing the object ...")


class Shape:

    def __init__(self, name):
        self.name = name
        self.sides = 0

print("Creating instance ...")

dog = Dog("American Foxhound", "White", "Akita")
myDog = Dog("Foxhound", "Black", "kita")
# herDog = Dog("Foxhound")
# myDog.color = "Black"
# print("\n")
print(f"A {Dog.info}")
print(f"A {dog.color}, {dog.id}:{dog.name} dog is that I like")
print(f"A {myDog.color}, {myDog.id}:{myDog.name} dog is that I like")
# print(f"A {herDog.color}, {herDog.id}:{herDog.name} dog is that I like")

# Shape object
print("\n")
circle = Shape("Circle")
rectangle = Shape("Rectangle")
rectangle.sides = 4
print(f"A {circle.name} has {circle.sides}")
print(f"A {rectangle.name} has {rectangle.sides}")

print("\n")