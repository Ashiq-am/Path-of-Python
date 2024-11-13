# import required library
import torch

# define a batch of two 3x3 square matrix
mat = torch.tensor([[[1.0, 2.0, 3.0], [4.0, 1.0, 6.0],
					[1.0, 1.0, 1.0]],
					[[2.0, 2.0, 3.0], [4.0, 5.0, 6.0],
					[2.0, 2.0, 2.0]]])
print("Input Matrix M: \n", mat)

# compute the inverse of matrix
Mat_inv = torch.linalg.inv(mat)

# display result
print("\nInverse Matrix: \n", Mat_inv)
