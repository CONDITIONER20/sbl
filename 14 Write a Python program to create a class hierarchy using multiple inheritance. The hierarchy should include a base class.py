class Shape:
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def perimeter(self):
        return 4 * self.side
circle = Circle(5)
print("Area of circle:", circle.area())

square = Square(4)
print("Perimeter of square:", square.perimeter())
