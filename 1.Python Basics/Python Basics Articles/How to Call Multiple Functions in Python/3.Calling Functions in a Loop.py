def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


functions = [add, multiply]

for func in functions:
    print(func(3, 5))