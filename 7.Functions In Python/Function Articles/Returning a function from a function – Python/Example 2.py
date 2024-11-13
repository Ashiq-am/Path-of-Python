# define two methods

# second method that will be returned
# by first method
def B(st2):
    print("Good " + st2 + ".")


# first method that return second method
def A(st1, st2):
    print(st1 + " and ", end="")

    # return second method
    return B(st2)


# call first method that do two work:
# 1. execute the body of first method, and
# 2. execute the body of second method as
# first method return the second method
A("Hello", "Morning")
