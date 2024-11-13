import torch

# Create a 2x3 tensor
x = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Repeat the tensor 2 times along the first dimension
x_repeated = x.repeat(2, 1)

print("Original tensor:\n", x)
print("Repeated tensor:\n", x_repeated)
