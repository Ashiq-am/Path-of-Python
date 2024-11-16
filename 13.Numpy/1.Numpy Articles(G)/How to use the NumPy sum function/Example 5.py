# Import NumPy Library
import numpy as np

# Initialize our array
array = np.ones(250, dtype=np.int8)

# Call our sum() function with a specified
# accumulator type
print(np.sum(array, dtype=np.int8))

# Expected Output: 250
