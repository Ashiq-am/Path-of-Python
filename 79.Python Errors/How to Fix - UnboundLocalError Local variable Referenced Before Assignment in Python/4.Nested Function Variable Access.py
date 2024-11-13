def outer_function():
    x = 10

    def inner_function():
        nonlocal x  # Declare 'x' as nonlocal
        print(x)    # Access 'x' from the outer function

        x = 20      # Modify outer function's local variable 'x'
        print(x)

    inner_function()

outer_function()
