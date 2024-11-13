def outer_function():
    my_variable = 10

    def inner_function():
        nonlocal my_variable
        my_variable += 1

    inner_function()
    print(my_variable)

outer_function()
