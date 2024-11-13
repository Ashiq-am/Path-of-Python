# code
import torch
import torch.nn as nn

# defining Lrelu and the the parameter 0.2 is passed to control the negative slope ; a=0.2
r = nn.LeakyReLU(0.2)

# Creating a Tensor with an array
input = torch.Tensor([1,-2,3,-5])

output = r(input)

print(output)
