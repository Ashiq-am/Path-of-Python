import torch
import matplotlib.pyplot as plt

GFG = torch.Tensor([1, 7, 1, 4, 1, 4, 3, 4, 1, 7, 2, 4])
hist = torch.histc(GFG, bins=5, min=0, max=4, out=None)

# Printing the histogram of tensor
print("GeeksforGeeks")
print("GFG tensor", hist)
bins = 5
x = range(bins)
plt.bar(x, hist, align='center', color=['forestgreen'])
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.show()
