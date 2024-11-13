import torch
import torch.nn as nn

# Calling the sigmoid function
sig = nn.Sigmoid()

# Defining tensor
input = torch.Tensor([1,-2,3,-5])

# Applying sigmoid to the tensor
output = sig(input)

print(output)
