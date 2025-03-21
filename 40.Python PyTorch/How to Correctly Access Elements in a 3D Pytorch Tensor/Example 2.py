# import torch module
import torch

# create an 3 D tensor with 8 elements each
a = torch.tensor([[[1, 2, 3, 4, 5, 6, 7, 8],
				[10, 11, 12, 13, 14, 15, 16, 17]],
				[[71, 72, 73, 74, 75, 76, 77, 78],
				[81, 82, 83, 84, 85, 86, 87, 88]]])

# display actual tensor
print(a)

# access all the tensors of 1 dimension
# and get only 7 values in that dimension
print(a[0:1, 0:1, :7])
