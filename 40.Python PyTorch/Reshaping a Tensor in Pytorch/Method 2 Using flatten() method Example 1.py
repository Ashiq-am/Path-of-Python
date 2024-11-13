# import torch module
import torch

# create an 2 D tensor with 8 elements each
a = torch.tensor([[1,2,3,4,5,6,7,8],
				[1,2,3,4,5,6,7,8]])

# display actual tensor
print(a)

# flatten a tensor with flatten() function
print(torch.flatten(a))
