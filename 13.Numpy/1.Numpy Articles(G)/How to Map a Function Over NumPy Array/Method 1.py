import numpy as np

arr = np.array([1, 2, 3, 4, 5])


def addTwo(i):
    return i + 2


applyall = np.vectorize(addTwo)
res = applyall(arr)
print(res)
