# importing the library
import torch

# define a 2D torch tensor
tensor = torch.tensor([[43,31,-92],
					[3,-4.3,53],
					[-4.2,7,-6.2]])
print("Tensor:\n", tensor)

# sorting the tensor in ascending order
print("Sorting tensor in \
ascending order along the column:")
values, indices = torch.sort(tensor, dim = 0)

# printing values in sorted tensor
print("Sorted values:\n", values)

# print indices of values in sorted tensor
print("Indices:\n", indices)

# sorting the tensor in descending order
print("Sorting tensor in \
descending order along the column:")
values, indices = torch.sort(tensor, dim = 0,
							descending=True)

# printing values in sorted tensor
print("Sorted values:\n", values)

# print indices of values in sorted tensor
print("Indices:\n", indices)
