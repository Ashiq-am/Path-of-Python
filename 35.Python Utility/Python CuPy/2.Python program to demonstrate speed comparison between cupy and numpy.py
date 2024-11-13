# Python program to
# demonstrate speed comparison
# between cupy and numpy

# Importing modules
import cupy as cp
import numpy as np
import time

# NumPy and CPU Runtime
s = time.time()
x_cpu = np.ones((1000, 1000, 100))
e = time.time()
print("Time consumed by numpy: ", e - s)

# CuPy and GPU Runtime
s = time.time()
x_gpu = cp.ones((1000, 1000, 100))
e = time.time()
print("\nTime consumed by cupy: ", e - s)
