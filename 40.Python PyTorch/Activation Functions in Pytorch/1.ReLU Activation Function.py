import torch
import torch.nn as nn

# defining relu
r = nn.ReLU()

# Creating a Tensor with an array
input = torch.Tensor([1, -2, 3, -5])

# Passing the array to relu function
output = r(input)

print(output)
