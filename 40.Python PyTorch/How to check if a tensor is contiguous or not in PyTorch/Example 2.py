# import torch library
import torch

# define a torch tensor
tens = torch.tensor([[10., 20., 30.],
					[40., 50., 60.]])

# transpose of the above defined tensor
tens_transpose = tens.transpose(0, 1)

# display tensors
print("\n Original Tensor \n", tens)
print("\n Transpose of original Tensor \n",
	tens_transpose)

# check if a tensor and it's transpose are
# contiguous or not
Output_1 = tens.is_contiguous()
print("\n Original Tensor is contiguous - ", Output_1)

Output_2 = tens_transpose.is_contiguous()
print("\n Transpose of original Tensor is contiguous - ", Output_2)
