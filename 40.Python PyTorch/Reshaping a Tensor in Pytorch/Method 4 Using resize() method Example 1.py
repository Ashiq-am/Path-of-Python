# importing torch module
import torch

# create one dimensional tensor
a = torch.Tensor()

# resize the tensor to 4 tensors.
# each tensor with 4 rows and 5 columns
print(a.resize_(4, 4, 5))
