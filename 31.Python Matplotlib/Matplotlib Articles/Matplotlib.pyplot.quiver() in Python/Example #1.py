#Python program to explain
# matplotlib.pyplot.quiver method


import matplotlib.pyplot as plt
import numpy as np

#defining necessary arrays
x = np.linspace(0,2,8)
y = np.linspace(2,0,8)
x_dir = y_dir = np.zeros((8,8))
y_dir[5,5] = 0.2

#plotting the 2D graph
plt.quiver(x, y, x_dir, y_dir, scale=1)
