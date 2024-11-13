# Import required library
import torch
import torch.nn as nn

# define a batch of tensor
tens = torch.tensor([[[11, 12], [13, 14]],
					[[21, 22], [23, 24]]])

print("\n Input Tensor: \n", tens)

# add unique padding sizes to all sides
# (left, right, top, bottom)
pad = nn.ConstantPad2d(1, 8)
output = pad(tens)

# display result
print("\n After Pad Input Ternsor:\n", output)
