# Python code to demonstrait
# nonlocal keyword

# Nested function to demonstrait
# nonlocal keyword

# Declairing variable in global scope
geek_name = 'geekforgeeks'


def geek_func():
    # Defining inner function
    def geek_func2():
        # Declairing nonlocal variable
        nonlocal geek_name
        geek_name = 'GeekForGeeks'

        # Printing our variable
        print(geek_name)

    # Calling inner function
    geek_func2()


geek_func()
