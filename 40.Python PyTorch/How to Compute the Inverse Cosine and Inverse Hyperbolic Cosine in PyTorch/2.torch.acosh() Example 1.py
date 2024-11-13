# importing torch
import torch

# create tensor
t1 = torch.tensor([[1, 2, 3],
				[5, 6, 7],
				[9, 10, 11]])

# printing the tensor
print(t1)

# get the inverse hyperbolic cosine values
print(torch.acosh(t1))
