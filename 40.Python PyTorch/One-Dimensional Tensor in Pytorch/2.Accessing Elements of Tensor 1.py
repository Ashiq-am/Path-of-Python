# importing torch module
import torch

# create one dimensional tensor with integer type elements
a = torch.tensor([10, 20, 30, 40, 50])

# access elements from 1 to 4
print(a[1:4])

# access from 4
print(a[4:])

# access from last
print(a[-1:])
