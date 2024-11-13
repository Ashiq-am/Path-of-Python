# Import required library
import torch

# creating a input tensor
tens = torch.tensor([3., 1.3, 2., 2.3, -2.3])

# print the input tensor
print(" Input Tensor - ", tens)

# compute the inverse hyperbolic sine
# of input tensor
tens_inv_hsin = torch.asinh(tens)

# print the above computed tensor
print(" Computed Inverse Hyperbolic Sine Tensor - ",
	tens_inv_hsin)
