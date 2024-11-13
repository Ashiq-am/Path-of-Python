import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Creating array points using numpy
x = np.arange(0, 20, 0.1)
y = np.sin(x)
z = y*np.sin(x)
c = x + y

#Change the Size of Graph using Figsize
fig = plt.figure(figsize = (10, 10))

#Generating a 3D sine wave
ax = plt.axes(projection = '3d')

# To create a scatter graph
ax.scatter(x, y, z, c = c)

# show the graph
plt.show()
