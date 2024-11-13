# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Change the Size of Graph using
# Figsize
fig = plt.figure(figsize=(10, 10))

# Generating a 3D sine wave
ax = plt.axes(projection='3d')

# Creating array points using
# numpy
x = np.arange(0, 20, 0.1)
y = np.sin(x)
z = y*np.sin(x)
c = x + y

# To create a scatter graph
ax.scatter(x, y, z, c=c)

# trun off/on axis
plt.axis('off')

# show the graph
plt.show()
