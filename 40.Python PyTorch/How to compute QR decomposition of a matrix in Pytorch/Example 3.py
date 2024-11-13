# Import the required libraries
import torch

# create a matrix of size 3x3
matrix = torch.tensor([[1., 2., -3.], [6., 5., 4.], [7., 8., -9.]])

# display input matrix
print("\n Input Matrix: \n ", matrix)

# compute the QR decomposition of input matrix
Q, R = torch.linalg.qr(matrix, mode='r')

# display result
print("\n Q \n ", Q)
print("\n R \n ", R)
