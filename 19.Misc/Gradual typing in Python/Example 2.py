# Python program to demonstrate
# function annotations

# Setting the arguments type and
# return type to str
def say_hello(name: str) -> str:
    return 'Hello ' + name


# will not throw an error
print(say_hello("Geeks"))

# will raise a TypeError
print(say_hello(1))
