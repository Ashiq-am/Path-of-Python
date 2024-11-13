# import Pytorch library
import torch

# error occur
input_var = torch.randn(3.0, 4.0, 5.0,
					requires_grad = True)
print(input_var)
