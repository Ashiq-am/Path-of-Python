import numpy as np

np.random.seed(42)

A = np.random.randint(0, 10, size=(3, 3, 2))
B = np.random.randint(0, 10, size=(3, 2, 4))

print("A:\n{}, shape={}\nB:\n{}, shape={}".format(
A, A.shape, B, B.shape))
