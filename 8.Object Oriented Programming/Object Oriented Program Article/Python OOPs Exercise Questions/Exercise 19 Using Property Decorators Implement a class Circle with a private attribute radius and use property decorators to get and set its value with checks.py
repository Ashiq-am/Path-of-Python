class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self.__radius = value
        else:
            print("Radius cannot be negative")

    def area(self):
        return 3.14159 * self.__radius ** 2

# Example usage:
circle = Circle(5)
print("Area:", circle.area())
circle.radius = -10
print("Radius:", circle.radius)
