# import torch library
import torch

# define a tensors
tens_1 = torch.Tensor([100, 200, 300, 400, 500])

# display tensor
print(" First Tensor: ", tens_1)

# multiply a scalar tensors
tens = torch.mul(tens_1, 2)

# display result after perform element wise multiplication
print(" After multiply 2 in tensor: ", tens)
