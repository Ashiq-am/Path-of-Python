# Import the torch library
import torch

# define a tensor
tens = torch.Tensor([10, 20, 30, 40, 50, 60])
print("Original Tensor: ", tens)

# below is the different ways to resize
# tensor to 2x3 using view()

# Resize tensor to 2x3
tens_1 = tens.view(2, 3)
print(" Tensor After Resize: \n", tens_1)

# other way resize tensor to 2x3
tens_2 = tens.view(2, -1)
print(" Tensor after resize: \n", tens_2)

# Other way to resize tensor to 2x3
tens_3 = tens.view(-1, 3)
print(" Tensor after resize: \n", tens_3)
