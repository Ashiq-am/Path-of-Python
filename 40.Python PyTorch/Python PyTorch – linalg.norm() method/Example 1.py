# Python program to compute vector norm
# importing libraries
import torch
import torch.linalg as la

# define input a 1D tensor
a = torch.tensor([-3., -4., 1., 0., 3., 2., -1., -7.])
print("1D Tensor:\n", a)

# computing the norm
norm = la.norm(a)

# print the computed norm
print("Norm:", norm)

# reshape the tensor to 2D tensor
a = a.reshape(2, 4)
print("2D Tensor:\n", a)

# again compute the norm
norm = la.norm(a)

# print the norm
print("Norm:", norm)
