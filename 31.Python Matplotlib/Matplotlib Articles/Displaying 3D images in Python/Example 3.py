#Import libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Change the Size of Graph using Figsize
fig = plt.figure(figsize=(10,10))

#Generating a 3D sine wave
ax = plt.axes(projection='3d')


# assigning coordinates
x = np.linspace(-1, 5, 10)
y = np.linspace(-1, 5, 10)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

# creating the visualiztion
ax.plot_wireframe(X, Y, Z, color ='green')

# trun off/on axis
plt.axis('off')
