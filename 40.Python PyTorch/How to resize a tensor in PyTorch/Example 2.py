# Import the torch library
import torch

# define a tensor
tens = torch.Tensor([[1, 2, 3], [4, 5, 6],
					[7, 8, 9], [10, 11, 12]])
print("Original Tensor: \n", tens)

# below is the different ways to use view()

# Resize tensor to 3x4
tens_1 = tens.view(2, -1)
print("\n Tensor After Resize: \n", tens_1)

# other way resize tensor to 3x4
tens_2 = tens.view(-1, 4)
print("\n Tensor after resize: \n", tens_2)

# Other way to resize tensor to 3x4
tens_3 = tens.view(3, -1)
print("\n Tensor after resize: \n", tens_3)
