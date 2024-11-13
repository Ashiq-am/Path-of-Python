from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection = '3d')

# Creating array points using numpy
z = np.linspace(0, 15, 1000)
x = np.sin(zline)
y = np.cos(zline)
ax.plot3D(x, y, z, 'gray')

plt.show()
