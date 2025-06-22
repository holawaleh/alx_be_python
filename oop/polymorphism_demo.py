# polymorphism_demo.py

import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method.")


# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Optional test/demo code
if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is {shape.area():.2f}")

