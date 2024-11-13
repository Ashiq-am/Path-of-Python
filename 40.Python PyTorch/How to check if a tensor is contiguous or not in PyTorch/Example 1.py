# import torch library
import torch

# create torch tensors
tens_1 = torch.tensor([1., 2., 3., 4., 5.])

# display tensors
print("\n First Tensor - ", tens_1)

# check this tensor is contiguous or not
output_1 = tens_1.is_contiguous()

# display output
print("\n This tensor is contiguous - ", output_1)
