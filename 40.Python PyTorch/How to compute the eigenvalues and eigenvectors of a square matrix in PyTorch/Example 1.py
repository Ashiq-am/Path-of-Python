# import the required library
import torch

# define a 3x3 square matrix
mat = torch.tensor([[-0.3371, -0.2975, 1.8739],
					[1.4078, 1.6856, 0.3799],
					[1.9002, -0.4428, 1.5552]])

# print the above created matrix
print("\n Matrix: \n", mat)

# compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(mat)

# print output
print("\n Eigenvalues: \n", eigenvalues)
print("\n Eigenvectors: \n", eigenvectors)
