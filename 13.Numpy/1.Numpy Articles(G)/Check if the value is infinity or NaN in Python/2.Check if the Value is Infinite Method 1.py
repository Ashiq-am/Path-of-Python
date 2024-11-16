import math


# Function checks if negative or
# positive infinite.
def check(x):
    if (math.isinf(x) and x > 0):
        print("x is Positive inf")

    elif (math.isinf(x) and x < 0):
        print("x is negative inf")

    else:
        print("x is not inf")

    # Creating inf using math module.


number = math.inf
check(number)

number = -math.inf
check(number)
