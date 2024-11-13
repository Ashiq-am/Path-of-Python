# Python program to demonstrate
# ipdate)wrapper() method


import functools


def divide(a, b):
    "Original Documentation of Divide"
    return a / b


half = functools.partial(divide,
                         b=2)

oneThird = functools.partial(divide,
                             b=3)

print("UPDATED WRAPPER DATA")
print(f'WRAPPER ASSIGNMENTS : {functools.WRAPPER_ASSIGNMENTS}')
print(f'UPDATES : {functools.WRAPPER_UPDATES}')

# Updating Metadata of wrapper
# using update_wrapper
ft.update_wrapper(half, divide)

try:
    print(half.__name__)

except AttributeError:
    print('No Name')

print(half.__doc__)

help(half)
help(oneThird)
