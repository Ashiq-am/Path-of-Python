# import requuired libraries
import numpy as np
from numpy.linalg import norm

# define two arrays
A = np.array([[1,2,2],
			[3,2,2],
			[-2,1,-3]])
B = np.array([[4,2,4],
			[2,-2,5],
			[3,4,-4]])

print("A:\n", A)
print("B:\n", B)

# compute cosine similarity
cosine = np.sum(A*B, axis=1)/(norm(A, axis=1)*norm(B, axis=1))

print("Cosine Similarity:\n", cosine)
print("Cosine Similarity:\n", cosine)
