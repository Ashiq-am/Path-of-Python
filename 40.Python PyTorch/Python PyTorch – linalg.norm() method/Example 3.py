# Python program to compute matrix norm
# importing libraries
import torch
import torch.linalg as la

# define input a 2D tensor (matrix)
a = torch.tensor([[1., 2., -3.],
				[-4., 5., 6.]])
print("Tensor:\n", a)

# compute and print the computed norm
# with different ord and dim
print("Norm with dim=0:",
	la.norm(a, dim=0))
print("Norm with dim=1:",
	la.norm(a, dim=1))
print("Norm with ord=1, dim=1:",
	la.norm(a, ord=1, dim=1))
print("Norm with ord=-1, dim=1:",
	la.norm(a, ord=-1, dim=1))
print("Norm with ord=1, dim=0:",
	la.norm(a, ord=1, dim=0))
print("Norm with ord=-1, dim=0:",
	la.norm(a, ord=1, dim=1))
print("Norm with dim=(0,1):",
	la.norm(a, dim=(0, 1)))
