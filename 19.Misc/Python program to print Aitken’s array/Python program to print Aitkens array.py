# Python program to print
# Aitken's array


from queue import Queue
from functools import reduce, lru_cache


# for dynamic programming
# Recursive function to print the
# Aitken's array.
@lru_cache()
def rec(n):
    # Base case
    if n == 1:
        print([1])
        return [1]

    array = [rec(n - 1)[-1]]

    for k in range(n - 1):
        array.append(array[k] + rec(n - 1)[k])

    print(array)

    return array


# Driver's code
rec(7)
