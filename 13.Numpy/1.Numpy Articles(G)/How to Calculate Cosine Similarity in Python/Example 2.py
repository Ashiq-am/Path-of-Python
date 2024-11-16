# import requuired libraries
import numpy as np
from numpy.linalg import norm

# define two lists or array
A = np.array([[2,1,2],[3,2,9], [-1,2,-3]])
B = np.array([3,4,2])
print("A:\n", A)
print("B:\n", B)

# compute cosine similarity
cosine = np.dot(A,B)/(norm(A, axis=1)*norm(B))
print("Cosine Similarity:\n", cosine)
