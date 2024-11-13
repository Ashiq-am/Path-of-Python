# python code to demonstrate short circuiting
# using and and or

# helper function
def check():
    return "geeks"


# using an expression to demonstrate
# prints "geeks", and gets executed
# as both are required to check truth value
print(1 and check())

# using an expression to demonstrate
# prints 1
# as only if 1st value is true, or
# doesnt require call check() fun
print(1 or check())

# using an expression to demonstrate
# prints "geeks"
# the value returns true when check
# is encountered. 1 is not executed
print(0 or check() or 1)

# using an expression to demonstrate
# prints 1
# as last value is required to evaluate
# full expression because of "and"
print(0 or check() and 1)
