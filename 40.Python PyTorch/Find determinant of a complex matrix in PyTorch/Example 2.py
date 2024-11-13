# import library
import torch

# create real parts the complex numbers
real = torch.tensor([[1, 2],[5,6]], dtype=torch.float32)

# create imaginary parts of the complex numbers
imag = torch.tensor([[3, 4],[8,9]], dtype=torch.float32)

# create complex tensor (matrix)
z = torch.complex(real, imag)
print("Complex Matrix: \n", z)

# Compute the determinant of Matrix
# using torch.linalg.det()
det = torch.linalg.det(z)
print("Determinant: \n", det)
