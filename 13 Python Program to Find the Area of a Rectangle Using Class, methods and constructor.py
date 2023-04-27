class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


rectangle1 = Rectangle(4, 5)
print("Area of rectangle:", rectangle1.area())
