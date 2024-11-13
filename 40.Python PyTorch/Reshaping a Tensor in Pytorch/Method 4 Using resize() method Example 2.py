# importing torch module
import torch

# create one dimensional
a = torch.Tensor()

# resize the tensor to 2 tensors.
# each tensor with 4 rows and 2 columns
print(a.resize_(2, 4, 2))
