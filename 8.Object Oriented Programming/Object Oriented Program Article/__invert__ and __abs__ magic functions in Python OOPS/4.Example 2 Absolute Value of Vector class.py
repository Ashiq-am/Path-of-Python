class Vector:
    def __init__(self, components):
        self.components = components

    def __abs__(self):
        # Custom implementation for absolute value computation
        return sum(component**2 for component in self.components)**0.5

# Example usage:
vector = Vector([1, 2, 3])
magnitude = abs(vector)
print(magnitude)
