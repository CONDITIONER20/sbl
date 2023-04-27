class Math:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c

math = Math()
print(math.add(2, 3))      # Output: 5
print(math.add(2, 3, 4))   # Output: 9
