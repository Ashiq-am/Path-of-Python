# example 2
import torch
import matplotlib.pyplot as plt

# Create a tensor
T = torch.Tensor([1, 5, 1, 4, 2, 4, 3,
				3, 1, 4, 2, 4])
print("Original Tensor T:\n", T)

# Calculate the histogram of the above
# created tensor
hist = torch.histc(T, bins=5, min=0, max=4)

# Visualize above calculated histogram
# as bar diagram
bins = 5
x = range(bins)
plt.bar(x, hist, align='center', color=['forestgreen'])
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.show()
