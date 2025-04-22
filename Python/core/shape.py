# Parent Class
class Shape:

    def __init__(self):
        self.name = "Shape"
        self._sides = 0
        self.__color = "White"

    def get_color(self):
        return self.__color


# Child Class
class Square(Shape):

    def __init__(self):
        super().__init__()
        self.name = "Square"
        self._sides = 4
        self.__color = "Red"


# Shape
# shape = Shape()
# shape_folder = dir(shape)
# print(shape_folder)
# print()

# Shape
square = Square()
square_folder = dir(square)
print(square_folder)
print()
print(f"__color:{square.__color}")
print(f"color:{square.get_color()}")
