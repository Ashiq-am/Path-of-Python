# Import required library
import torch

# define the tensor
tens = torch.tensor([[-1., 3., -5.],
					[-4., 5., 2.],
					[-2., 3., 4.], ])

print("\n Input tensor: \n", tens)

# define a function
def fun(tens):
	return tens**3

# values of function
values = fun(tens)

# display values
print("\n Function Values: \n", values)

# estimate the gradients of fun in dim=0
grad_dim_0 = torch.gradient(values, dim=0)
print("\n Estimated Gradients of fun() in dim=0 - \n", grad_dim_0)

# estimate the gradients of fun in dim=1
grad_dim_1 = torch.gradient(values, dim=1)
print("\n Estimated Gradients of fun() in dim=1 - \n", grad_dim_1)
