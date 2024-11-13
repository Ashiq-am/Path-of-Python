# Import required library
import torch

# creating a input tensor
tens = torch.tensor([2.1+3j, 2.+2.j, 4.+2.j, 2.4+2.j])

# print the input tensor
print(" Input Tensor - ", tens)

# compute the inverse hyperbolic sine
# of input tensor
tens_inv_hsin = torch.asinh(tens)

# print the above computed tensor
print(" Computed Inverse Hyperbolic Sine - ",
	tens_inv_hsin)
