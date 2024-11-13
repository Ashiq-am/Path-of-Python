# Decorator to print function call
# details
def function_details(func):
    # Getting the argument names of the
    # called function
    argnames = func.__code__.co_varnames[:func.__code__.co_argcount]

    # Getting the Function name of the
    # called function
    fname = func.__name__

    def inner_func(*args, **kwargs):
        print(fname, "(", end="")

        # printing the function arguments
        print(', '.join('% s = % r' % entry
                        for entry in zip(argnames, args[:len(argnames)])), end=", ")

        # Printing the variable length Arguments
        print("args =", list(args[len(argnames):]), end=", ")

        # Printing the variable length keyword
        # arguments
        print("kwargs =", kwargs, end="")
        print(")")

    return inner_func


# Driver Code
@function_details
def GFG(a, b=1, *args, **kwargs):
    pass


GFG(1, 2, 3, 4, 5, d=6, g=12.9)
GFG(1, 2, 3)
GFG(1, 2, d='Geeks')
