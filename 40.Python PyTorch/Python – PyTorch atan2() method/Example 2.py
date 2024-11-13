# Python3 program to demonstrate torch.atan2() method
%matplotlib qt

# importing required libraries
import torch
import numpy as np
import matplotlib.pyplot as plt

# defining first tensor (y-coordinates)
b = np.array([-8,-3,-2,-1,0,1,2,3,4])

# defining second tensor (x-coordinates)
a = np.array([1,1,1,1,1,1,1,1,1])
y = torch.tensor(b)
x = torch.tensor(a)
print('Tensor y:\n', y)
print('Tensor x:\n', x)

# computing the 2-argument arc tangent
result = torch.atan2(y,x)
print('atan2:\n', result)

# tensor to numpy array
result = result.numpy()

# plot the result using matplotlib
plt.plot(b/a, result, color='r', label='atan2')
plt.xlabel("y/x")
plt.ylabel("atan2")
plt.title("2D atan2 plot GFG")
plt.show()
