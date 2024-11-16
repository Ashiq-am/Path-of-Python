import numpy as np


# vector v1 of dimension (2, 2)
v1 = np.array([[1, 2], [1, 2]])

# vector v2 of dimension (2, 2)
v2 = np.array([[1, 2], [1, 2]])

print("vector multiplication")
print(np.dot(v1, v2))

print("\nElementwise multiplication of two vector")
print(v1 * v2)
