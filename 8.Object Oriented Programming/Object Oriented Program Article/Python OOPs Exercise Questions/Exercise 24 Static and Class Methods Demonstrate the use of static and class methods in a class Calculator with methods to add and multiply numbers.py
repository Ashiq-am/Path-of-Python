class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

# Example usage:
print("Addition:", Calculator.add(5, 3))
print("Multiplication:", Calculator.multiply(4, 5))
