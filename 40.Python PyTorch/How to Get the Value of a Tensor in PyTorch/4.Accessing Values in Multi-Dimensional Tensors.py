import torch

# Creating a 3D tensor
tensor = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Accessing a value in a 3D tensor
value = tensor[1, 0, 2]
print(value)
