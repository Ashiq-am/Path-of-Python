# Code to implement the usage
# of decorators
def decorating(function):
    def item():
        print("The function was decorated.")
        function()

    return item


# using the "@" sign to signify
# that a decorator is used.
@decorating
def my_function():
    print("This is my function.")


# Driver's Code
my_function()
