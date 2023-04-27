class Cube:
    def area(self, side=None, length=None, width=None, height=None):
        if side is not None:
            return 6 * side ** 2
        elif length is not None and width is not None and height is not None:
            return 2 * (length * width + length * height + width * height)
        else:
            return "Invalid input"
c1 = Cube()
print(c1.area(side=4)) # Expected output: 96
print(c1.area(length=2, width=3, height=4)) # Expected output: 52
print(c1.area(side=3, length=2, width=3)) # Expected output: Invalid input
