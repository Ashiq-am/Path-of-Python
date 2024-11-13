# Python3 program to Convert a
# list to dictionary
import numpy as np


def create(limit, diff):
    lst = np.arange(diff, limit, diff)
    if (lst[-1] != limit):
        lst = np.r_[lst, limit]

    return np.r_[-lst[::-1], 0, lst].tolist()


# Driver code
limit = 1
diff = 0.5
print(create(limit, diff))
