import numpy as np

# Specifying array as a tuple, and
# Specify their data types.
arr3 = np.zeros((2, 2, 3), dtype=[('x', 'int'), ('y', 'float')])
print(arr3)
print(arr3.dtype)
