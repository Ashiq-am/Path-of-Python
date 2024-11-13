# importing pytorch module
import torch

# create an vector A
A = torch.tensor([58, 59, 60, 61, 62])

# create an vector B
B = torch.tensor([8, 9, 6, 1, 2])

# dot product of the two vectors
print(torch.dot(A, B))
