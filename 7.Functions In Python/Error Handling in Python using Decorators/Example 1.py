# defining decorator function
def decorator_example(func):
    print("Decorator called")

    # defining inner decorator function
    def inner_function():
        print("inner function")
        func()

    return inner_function


# defining outer decorator function
@decorator_example
def out_function():
    print("outter function")


out_function()
