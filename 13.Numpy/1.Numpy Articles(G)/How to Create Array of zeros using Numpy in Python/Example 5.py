import numpy as np

# Specifying array as a tuple, and
# Specify their data types.
arr = np.zeros((2, 2), dtype=[('x', 'int'),
							('y', 'float')])
print(arr)
print(arr.dtype)
