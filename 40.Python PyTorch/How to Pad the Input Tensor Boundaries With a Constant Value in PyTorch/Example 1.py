# Import required library
import torch
import torch.nn as nn

# define a tensor
tens = torch.tensor([[[21, 22], [23, 24]]])
print("\n Input Tensor: \n", tens)

# give padding size same for all sides
pad = nn.ConstantPad2d(2, 9)
output = pad(tens)

# display result
print("\n After Pad Input Ternsor: \n", output)
