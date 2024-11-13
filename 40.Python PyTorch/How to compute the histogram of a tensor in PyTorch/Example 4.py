# example 1
import torch
import matplotlib.pyplot as plt

# Create a tensor
T = torch.Tensor([1, 5, 1, 4, 2, 4, 3,
				3, 1, 4, 2, 4])
print("Original Tensor T:\n", T)

# Calculate the histogram of the above
# created tensor
hist = torch.histc(T, bins=5, min=0, max=4)
print("Histogram of T:\n", hist)
