from string import Formatter

def custom_formatter(number):
    return f"The number is: {number:.2f}"

print(custom_formatter(123.456))
