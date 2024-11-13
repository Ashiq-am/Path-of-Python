# Python program to compute norm
# importing libraries
import torch
import torch.linalg as la

# define input a 2D tensor (matrix)
a = torch.tensor([[1., 2., -3.],
				[-4., 5., 6.],
				[9., -7., 8.]])
print("Tensor:\n", a)

# compute and print the computed norm
print("\nNorm with different ord:\n")
print("Norm with ord= None:",
	la.norm(a, ord=None))
print("Norm ord= 'fro':",
	la.norm(a, ord='fro'))
print("Norm with ord= float('inf'):",
	la.norm(a, ord=float('inf')))
print("Norm with ord= -float('inf'):",
	la.norm(a, ord=-float('inf')))
print("Norm with ord= 'nuc'):",
	la.norm(a, ord='nuc'))

# print("Norm with ord= 0:", la.norm(a, ord= 0))
# ord=0 not supported for matrix norm
print("Norm with ord= 1:",
	la.norm(a, ord=1))
print("Norm with ord= -1:",
	la.norm(a, ord=-1))
print("Norm with ord= 2:",
	la.norm(a, ord=2))
print("Norm with ord= -2:",
	la.norm(a, ord=-1))
