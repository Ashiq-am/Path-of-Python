import numpy as np
array1 = np.array([1,2])
array2 = np.array([1,2])

# Original array1
print(array1)

# Original array2
print(array2)
# Cross-correlation of the arrays
print("\nCross-correlation:\n", np.correlate(array1, array2))
