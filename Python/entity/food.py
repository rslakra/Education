# Food Entity
class Food:

    # constructor
    def __init__(self, id, type, name, ppu) -> None:
        self.id = id
        self.type = type
        self.name = name
        self.ppu = ppu

    # String representation
    def __str__(self) -> str:
        """Returns string representation of this object."""
        return f'Food <id={self.id}, type={self.type}, name={self.name}, ppu={self.ppu}>'

    def __repr__(self):
        """Returns string representation of this object."""
        return str(self)

    def print(foods):
        pass


cake = Food("0001", "donut", "Cake", 0.55)
print(cake)
