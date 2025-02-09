class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def set_dimensions(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage:
rect = Rectangle()
print("Default area:", rect.area())
rect.set_dimensions(4, 5)
print("Updated area:", rect.area())
