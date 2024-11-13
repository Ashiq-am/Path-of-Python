# Import required library
import torch

# define the tensor
tens = torch.tensor([-2., 1., -3., 4., 5.])
print(" Input tensor: ", tens)

# define a function
def fun(tens):
	return tens**2+5

# values of function
values = fun(tens)

# display values
print(" Function Values: ", values)

# estimate the gradients of fun
grad = torch.gradient(values)

# Display result
print(" Estimated Gradients of fun() - ", grad)
