# importing the modules
import numpy as np
import timeit
import math

# vectorized operation
print("Time taken by vectorized operation : ", end = "")
timeit(np.exp(np.arange(150)))

# non-vectorized operation
print("Time taken by non-vectorized operation : ", end = "")
timeit([math.exp(item) for item in range(150)])
