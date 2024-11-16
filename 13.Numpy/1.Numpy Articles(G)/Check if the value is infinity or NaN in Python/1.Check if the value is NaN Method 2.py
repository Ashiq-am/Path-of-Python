import math


def isNan(number):
    # This function compares number to itself.
    # NaN != NaN and therfore it will return
    # true if the number is Nan
    return number != number


# Driver Code
x = math.nan
print(isNan(x))
