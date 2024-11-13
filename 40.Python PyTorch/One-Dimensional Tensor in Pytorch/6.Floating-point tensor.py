# importing torch module
import torch

# create one dimensional Float Tensor with
# integer type elements
a = torch.FloatTensor([10, 20, 30, 40, 50])

# display data type
print(a.dtype)

# access elements from 0 to 3
print(a[0:3])

# access from 4
print(a[4:])
