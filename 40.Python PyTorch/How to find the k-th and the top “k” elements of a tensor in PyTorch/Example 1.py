# import torch library
import torch

# define a tensor
tens = torch.Tensor([4, 5, -3, 9, 7])
print("Original Tensor:\n", tens)

# find 3 largest element from the tensor
value, index = torch.kthvalue(tens, 3)

# print value along with index
print("\nIndex:", index, "Value:", value)
