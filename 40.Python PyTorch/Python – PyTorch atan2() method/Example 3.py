# Python3 program to demonstrate torch.atan2() method
%matplotlib qt

# importing required libraries
import torch
import numpy as np
import matplotlib.pyplot as plt

# defining first tensor (y-coordinates)
b = np.arange(25,74, 1)
y = torch.tensor(b)

# defining second tensor (x-coordinates)
a = np.arange(1,50, 1)
x = torch.tensor(a)
print('Tensor y:\n', y)
print('Tensor x:\n', x)

# computing the 2-argument arc tangent
result = torch.atan2(y,x)
print('atan2 values:\n', result)

# converting the result tensor to numpy array
result = result.numpy()

# plot the result as 3D using matplotlib
fig = plt.figure()

# syntax for 3-D projection
ax = plt.axes(projection ='3d')
ax.plot3D(a, b, result, 'green')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('atan2')
ax.set_title('3D atan2() plot GFG')
plt.show()
