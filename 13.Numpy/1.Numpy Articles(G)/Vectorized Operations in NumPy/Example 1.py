# importing the modules
import numpy as np
import timeit

# vectorized sum
print(np.sum(np.arange(15000)))

print("Time taken by vectorized sum : ", end = "")
timeit(np.sum(np.arange(15000)))

# itersative sum
total = 0
for item in range(0, 15000):
	total += item
a = total
print("\n" + str(a))

print("Time taken by iterative sum : ", end = "")
timeit(a)
