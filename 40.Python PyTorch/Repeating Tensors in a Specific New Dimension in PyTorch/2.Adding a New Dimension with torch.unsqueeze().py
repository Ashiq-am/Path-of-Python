import torch

# Create a 1D tensor
x = torch.tensor([1, 2, 3])

# Add a new dimension at position 0
x_unsqueezed = x.unsqueeze(0)

print("Tensor with a new dimension:\n", x_unsqueezed)
