# import library
import torch

# create a real tensor
mat = torch.randn(3,3,2)

# display the real tensor
print("Real Tensor: \n",mat)

# convert the above real tensor
# into complex tensor
mat = torch.view_as_complex(mat)

# display the complex tensor (matrix)
print("Complex Tensor (Matrix): \n", mat)

# Compute the determinant of Matrix
# using torch.linalg.det()
det = torch.linalg.det(mat)
print("Determinant: \n", det)
