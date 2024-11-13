# import torch module
import torch

# Define a 2D tensor
tens = torch.tensor([[[1, 2, 3], [4, 5, 6]],
					[[7, 8, 9], [10, 11, 12]],
					[[13, 14, 15], [16, 17, 18]]])
# display original tensor
print("\n Original Tensor: \n", tens)

# find transpose of multi-dimension tensor
tens_transpose = torch.transpose(tens, 0, 1)

# display final result
print("\n Tensor After Transpose: \n", tens_transpose)
