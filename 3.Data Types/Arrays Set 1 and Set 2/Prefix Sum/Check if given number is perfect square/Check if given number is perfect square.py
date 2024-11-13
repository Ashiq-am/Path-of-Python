# Python program to find if x is a
# perfect square.

import math


def isPerfectSquare(x):
    # if x >= 0,
    if (x >= 0):
        sr = math.sqrt(x)

        # return boolean T/F
        return ((sr * sr) == x)
    return false


# Driver code


x = 2500
if (isPerfectSquare(x)):
    print("Yes")
else:
    print("No")


