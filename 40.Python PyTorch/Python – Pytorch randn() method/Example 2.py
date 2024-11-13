# import Pytorch library
import torch

# create a 3-dimensionl tensor
# of 4 x 5
input_var = torch.randn(3, 4, 5,
					requires_grad = True)
print(input_var)
