class Shape:
    def __init__(self, dimension1, dimension2):
        self.dimension1 = dimension1
        self.dimension2 = dimension2
        
    
class Triangle(Shape):
    def calculateArea(self):
        area = 0.5 * self.dimension1 * self.dimension2
        print("Triangle area:",area)
        
        
class Rectangle(Shape):
    def calculateArea(self):
        area = self.dimension1 * self.dimension2
        print("Rectangle area:",area)
        
             
ABC = Triangle(5, 6)
ABC.calculateArea()

ABCD = Rectangle(5, 6)
ABCD.calculateArea()