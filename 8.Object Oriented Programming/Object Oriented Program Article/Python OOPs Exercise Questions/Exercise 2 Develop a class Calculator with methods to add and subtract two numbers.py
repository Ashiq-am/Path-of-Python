class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# Testing the calculator
calc = Calculator()
print("Sum:", calc.add(5, 3))
print("Difference:", calc.subtract(5, 3))
