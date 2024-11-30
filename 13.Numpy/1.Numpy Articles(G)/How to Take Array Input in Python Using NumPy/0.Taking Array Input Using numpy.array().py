import numpy as np

# Take input for the array as a space-separated string

val = input("Enter elements separated by space: ").split()

# Convert input elements to a NumPy array
# Convert to integer array, change dtype as needed

arr = np.array(val, dtype=int)

print(arr)
