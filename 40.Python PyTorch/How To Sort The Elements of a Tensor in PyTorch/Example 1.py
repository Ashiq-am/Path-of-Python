# importing required library
import torch

# defining a PyTorch Tensor
tensor = torch.tensor([-12, -23, 0.0, 32,
					1.32, 201, 5.02])
print("Tensor:\n", tensor)

# sorting the tensor in ascending order
print("Sorting tensor in ascending order:")
values, indices = torch.sort(tensor)

# printing values of sorted tensor
print("Sorted values:\n", values)

# printing indices of sorted value
print("Indices:\n", indices)

# sorting the tensor in descending order
print("Sorting tensor in descending order:")
values, indices = torch.sort(tensor, descending=True)

# printing values of sorted tensor
print("Sorted values:\n", values)

# printing indices of sorted value
print("Indices:\n", indices)
