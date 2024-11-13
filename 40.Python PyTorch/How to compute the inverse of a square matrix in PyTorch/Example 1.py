# import required library
import torch

# define a 4x4 square matrix
mat = torch.tensor([[ 1.00, -0.000, -0.00, 0.00],
		[ 4.00, 1.000, 2.00, 0.00],
		[ -9.00, -3.00, 1.00, 8.00],
		[ -2.00, -0.00, -0.00, 1.00]])
print("Input Matrix M: \n", mat)

# compute the inverse of matrix
Mat_inv = torch.linalg.inv(mat)

# display result
print("\nInverse Matrix: \n", Mat_inv)
