# Use Google Colab to run these programs
import torch

GFG = torch.Tensor([1, 7, 1, 4, 1, 4, 3, 4, 1, 7, 2, 4])
hist = torch.histc(GFG, bins=5, min=0, max=4, out=None)

# Printing the histogram of tensor
print("GeeksforGeeks")
print("GFG tensor", hist)
