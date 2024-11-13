# import the required library
import torch

# define a batch of matrices
mat = torch.tensor([[[-0.1345, -0.7437, 1.2377],
					[0.9337, 1.6473, 0.4346],
					[-1.6345, 0.9344, -0.2456]],
					[[1.3343, -1.3456, 0.7373],
					[1.4334, 0.2473, 1.1333],
					[-1.5341, 1.5348, -1.4567]]])

# print the above batch of matrices
print("\n Matrix: \n", mat)

# compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(mat)

# print output
print("\n Eigenvalues: \n", eigenvalues)
print("\n Eigenvectors: \n", eigenvectors)
