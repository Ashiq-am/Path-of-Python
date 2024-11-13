# Python 3 program to demonstrate torch.atan2() method
# importing torch
import torch

# defining first tensor (y-coordinates)
y = torch.tensor([0., 40., -137., -30.])

# defining second tensor (x-coordinates)
x = torch.tensor([120., -4., -70., 23.])

# printing the two tensors
print('Tensor y:', y)
print('Tensor x:', x)

# computing the 2-argument arc tangent
result = torch.atan2(y, x)
print('atan2(y,x):', result)
