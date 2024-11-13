# import torch library
import torch

# define a tensor
tens = torch.Tensor([100, 200, 300, 400, 500])

# display tensors
print(tens)

# Subtract 50 from tensor
tens_result = torch.sub(tens, 50)

# display result after subtract sclar from tensor
print("After subtract sclar from tensor:", tens_result)
