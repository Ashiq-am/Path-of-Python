# Import required library
import torch
import torch.nn as nn

# define a tensor
tens = torch.tensor([[[11, 12], [13, 14]]])
print("\n Input Tensor: \n", tens)

# give padding size same for all sides
pad = nn.ZeroPad2d(1)
output = pad(tens)

# display result
print("\n After Pad Input Ternsor: \n", output)
