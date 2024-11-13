# Python3 program to demonstrate torch.log2() method
%matplotlib qt

# importing required libraries
import torch
import numpy as np

# import matplotlib.pyplot as plt
# defining a torch tensor
x = np.arange(1,50, 1)
t = torch.tensor(x)
print('Tensor:', t)

# computing the logarithm base 2 of t
result = torch.log2(t)
print('Logarithm of Tensor:', result)

# tensor to numpy array
y = result.numpy()

# plot the result using matplotlib
plt.plot(x, y, color = 'red', marker = "o")
plt.xlabel("x")
plt.ylabel("log2(x)")
plt.show()
