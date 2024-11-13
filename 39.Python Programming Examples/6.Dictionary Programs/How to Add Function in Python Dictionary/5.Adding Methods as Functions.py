class MathOperations:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

# Create an instance of the class
math_ops = MathOperations()

# Add methods to the dictionary
my_dict = {
    'add': math_ops.add,
    'subtract': math_ops.subtract
}

# Using the methods
print(my_dict['add'](10, 5))
print(my_dict['subtract'](10, 5))
