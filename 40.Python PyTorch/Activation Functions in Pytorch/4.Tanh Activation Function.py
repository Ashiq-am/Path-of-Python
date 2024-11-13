import torch
import torch.nn as nn

# Calling the Tanh function
t = nn.Tanh()

# Defining tensor
input = torch.Tensor([1,-2,3,-5])

# Applying Tanh to the tensor
output = t(input)
print(output)
