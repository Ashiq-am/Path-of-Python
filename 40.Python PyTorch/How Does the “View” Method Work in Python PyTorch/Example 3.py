# importing torch module
import torch

# create one dimensional tensor
# 12 elements
a = torch.range(10, 21)

# view tensor in 4 rows and 3 columns
print(a.view(4, 3))

# view tensor in 3 rows and 4 columns
print(a.view(3, 4))
