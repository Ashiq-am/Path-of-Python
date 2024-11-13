# Python program to demonstrate
# function annotations

# Setting the arguments type and
# return type to int
def sum(num1: int, num2: int) -> int:
    return num1 + num2


# will not throw an error
print(sum(2, 3))

# will raise a TypeError
print(sum(1, 'Geeks'))
