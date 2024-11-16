import numpy as np

# Create a numpy array
arr = np.array([[5, 11, -15], [12, 34, -51],
                [-24, -43, 92]], dtype=np.int32)

print(arr)

# Find the QR factor of array
q, r = np.linalg.qr(arr)
print('\nQ:\n', q)
print('\nR:\n', r)
