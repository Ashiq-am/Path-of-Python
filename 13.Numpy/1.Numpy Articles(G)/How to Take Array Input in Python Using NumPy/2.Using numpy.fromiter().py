import numpy as np

# Take input as space-separated values

val = input("Enter elements separated by space: ").split()

# Use fromiter() to create a NumPy array

arr = np.fromiter((int(x) for x in val), dtype=int)

print(arr)