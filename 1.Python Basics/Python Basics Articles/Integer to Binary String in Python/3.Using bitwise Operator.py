# Manual conversion with bitwise operations
binary_string = ''
number = 42

while number > 0:
    binary_string = str(number % 2) + binary_string
    number //= 2

# Handle the case when num is 0
binary_result = binary_string if binary_string else '0'

# Example usage
print(type(number))
print(f"The binary representation of {number} is: {binary_result}")
print(type(binary_result))