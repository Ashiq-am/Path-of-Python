import numpy as np
array1 = np.array([0, 1, 2])
array2 = np.array([3, 4, 5])

# Original array1
print(array1)

# Original array2
print(array2)

# ross-correlation of the arrays
print("\nCross-correlation:\n", np.correlate(array1, array2))
