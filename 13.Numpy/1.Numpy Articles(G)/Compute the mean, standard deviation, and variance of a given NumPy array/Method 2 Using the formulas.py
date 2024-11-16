import numpy as np

# Original array
array = np.arange(10)
print(array)

r1 = np.average(array)
print("\nMean: ", r1)

r2 = np.sqrt(np.mean((array - np.mean(array)) ** 2))
print("\nstd: ", r2)

r3 = np.mean((array - np.mean(array)) ** 2)
print("\nvariance: ", r3)
