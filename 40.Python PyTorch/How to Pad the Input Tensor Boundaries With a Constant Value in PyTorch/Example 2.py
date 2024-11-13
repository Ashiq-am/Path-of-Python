# Import required library
import torch
import torch.nn as nn

# define a tensor
tens = torch.tensor([[[11, 12], [13, 14]]])
print("\n Input Tensor: \n", tens)

# add unique padding sizes to all sides
# (left, right, top, bottom)
pad = nn.ConstantPad2d((1, 2, 3, 4), 8)
output = pad(tens)

# display result
print("\n After Pad Input Ternsor:\n", output)
