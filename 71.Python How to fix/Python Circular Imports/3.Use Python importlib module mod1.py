# import importlib module
import importlib

def display1():
    print("I am display1 from module 1")

# import mod2 using importlib.import_module()
module = importlib.import_module("mod2")
module.display2()
