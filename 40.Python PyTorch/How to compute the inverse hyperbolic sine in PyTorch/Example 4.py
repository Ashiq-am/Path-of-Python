# Import required library
import torch

# define a 2D input tensor
tens = torch.tensor([[2.1+3j, 2.+3.j, 3.1-3.5j],
					[1.3+2j, 2.3-2.3j, 4.+3.j],
					[3.2+5j, 6.+3.j, 4.2-3.2j]])

# print the input tensor
print("\n Input Tensor: \n", tens)

# compute the inverse hyperbolic sine
# of input tensor
tens_inv_hsin = torch.asinh(tens)

# print the above computed tensor
print("\n Computed Inverse Hyperbolic Sine: \n ",
	tens_inv_hsin)
