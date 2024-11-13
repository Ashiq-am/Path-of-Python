class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

# Using static methods without creating an instance
print(MathOperations.add(5, 3))        # Output: 8
print(MathOperations.subtract(10, 4))  # Output: 6