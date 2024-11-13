def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

calculator = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

# Using the calculator
print(calculator['add'](10, 5))
print(calculator['subtract'](10, 5))
print(calculator['multiply'](10, 5))
print(calculator['divide'](10, 5))
