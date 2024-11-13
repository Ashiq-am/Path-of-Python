# Python program to demonstrate
# ipdate)wrapper() method


import functools as ft


# Defining the decorator
def hi(func):
    def wrapper():
        "Hi has taken over Hello Documentation"
        print("Hi geeks")
        func()

    # Note The following Steps Clearly
    print("UPDATED WRAPPER DATA")
    print(f'WRAPPER ASSIGNMENTS : {ft.WRAPPER_ASSIGNMENTS}')
    print(f'UPDATES : {ft.WRAPPER_UPDATES}')

    # Updating Metadata of wrapper
    # using update_wrapper
    ft.update_wrapper(wrapper, func)
    return wrapper


@hi
def hello():
    "this is the documentation of Hello Function"
    print("Hey Geeks")


print(hello.__name__)
print(hello.__doc__)
help(hello)
