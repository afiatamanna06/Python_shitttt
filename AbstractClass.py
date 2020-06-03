from abc import ABC, abstractclassmethod
class Shape(ABC):
    def __init__(self, dimension1, dimension2):
        self.dimension1 = dimension1
        self.dimension2 = dimension2

    def area(self):
        pass


class Triangle(Shape):
    def area(self):
        triangleArea = 0.5 * self.dimension1 * self.dimension2
        print(triangleArea)


triangle = Triangle(5,6)
triangle.area()
