# importing reduce() from functools
from functools import reduce


# composite_function accepts N
# number of function as an
# argument and then compose them
def composite_function(*func):
    def compose(f, g):
        return lambda x: f(g(x))

    return reduce(compose, func, lambda x: x)


# Function to add 2
def add(x):
    return x + 2


# Function to multiply 2
def multiply(x):
    return x * 2


# Function to subtract 2
def subtract(x):
    return x - 1


# Here add_subtract_multiply will
# store lambda x : multiply(subtract(add(x)))
add_subtract_multiply = composite_function(multiply,
                                           subtract,
                                           add)

print("Adding 2 to 5, then subtracting 1 and multiplying the result with 2: ",
      add_subtract_multiply(5))
