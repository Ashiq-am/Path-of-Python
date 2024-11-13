# Import required library
import torch

# define a 2D input tensor
tens = torch.tensor([[1., 2.3, 1.3],
					[2.1, 3., -2.3],
					[3.2, 5.2, 2.3]])

# print the input tensor
print("\n Input Tensor: \n", tens)

# compute the inverse hyperbolic sine of
# input tensor
tens_inv_hsin = torch.asinh(tens)

# print the above computed tensor
print("\n Computed Inverse Hyperbolic Sine: \n ",
	tens_inv_hsin)
