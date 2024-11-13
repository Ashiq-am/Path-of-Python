def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed", 400)
    return a / b
