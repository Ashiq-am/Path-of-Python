import torch

# Creating a scalar tensor (0-dimensional)
scalar_tensor = torch.tensor(42.0)

# Extracting the value using .item()
value = scalar_tensor.item()

print(value)
print(type(value))
