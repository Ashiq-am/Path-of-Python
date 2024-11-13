import torch
import torch.nn as nn

# Calling the Softmax function with
# dimension = 0 as dimension starts
# from 0
sm = nn.Softmax(dim=0)

# Defining tensor
input = torch.Tensor([1,-2,3,-5])

# Applying function to the tensor
output = sm(input)
print(output)
