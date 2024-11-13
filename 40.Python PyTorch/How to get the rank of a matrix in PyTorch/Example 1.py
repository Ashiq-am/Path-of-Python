# import torch module
import torch

# define a tensor
tens = torch.tensor([[0.5322, 0.9232, 0.232],
					[0.1112, 0.2323, 0.2611],
					[0.7556, 0.1217, 0.5435]])

# display tensor/matrix
print("\n Input Matrix: ")
print(tens)

# get the rank of input matrix
r = torch.linalg.matrix_rank(tens)

# display rank of matrix
print("\n Rank of input matrix: ", r)
