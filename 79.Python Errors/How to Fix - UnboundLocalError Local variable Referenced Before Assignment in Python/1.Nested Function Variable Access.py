def outer_function():
    x = 10

    def inner_function():
        print(x)  # Trying to access 'x' from the outer function

        x = 20    # Inner function's local variable
        print(x)

    inner_function()

outer_function()
