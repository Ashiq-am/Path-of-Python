# Python code to illustrate
# Decorators with parameters in Python
from _ctypes_test import func


def decorator_fun(func):
    print("Inside decorator")


def inner(*args, **kwargs):
    print("Inside inner function")
    print("Decorated the function")

    func()
    return inner


def func_to():
    print("Inside actual function")


# another way of using decorators
decorator_fun(func_to)()
