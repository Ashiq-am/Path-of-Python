from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection = '3d')

# Data for a three-dimensional line
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x, y, z, 'green')

ax.view_init(-140, 60)

plt.show()
