import torch

real = torch.rand(2, 2)
print(real)
imag = torch.rand(2, 2)
print(imag)
complex_tensor = torch.complex(real, imag)
print(complex_tensor)
