import torch

# Create a 1D tensor
x = torch.tensor([1, 2, 3])

# Add a new dimension at position 0
x_unsqueezed = x.unsqueeze(0)

# Repeat the tensor 4 times along the new dimension
x_repeated = x_unsqueezed.repeat(4, 1)

print("Repeated tensor along new dimension:\n", x_repeated)
