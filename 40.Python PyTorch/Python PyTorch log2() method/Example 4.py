# Python3 program to demonstrate torch.log2() method
# importing libraries
import torch
import numpy as np

# defining a torch tensor
t = torch.tensor([-3., -5., 0, 0.5, 7., 3., np.inf])
print('Original Tensor:\n', t)

# computing the logarithm base 2 of t
result = torch.log2(t)
print('Logarithm of Tensor:\n', result)
