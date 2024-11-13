# import importlib module
import importlib

def display2():
    print("I am display2 of module 2")

# import mod1 using importlib.import_module()
module = importlib.import_module("mod1")
module.display1()
