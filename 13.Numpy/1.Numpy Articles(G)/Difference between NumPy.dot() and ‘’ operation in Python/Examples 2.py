import numpy as np


v1 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

v2 = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]]])

print("vector multiplication")
print(np.dot(v1, v2))

print("\nElementwise multiplication of two vector")
print(v1 * v2)
