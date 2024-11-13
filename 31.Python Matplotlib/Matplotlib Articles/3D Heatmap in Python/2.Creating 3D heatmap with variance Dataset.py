# 3D Heatmap in Python using matplotlib

# to make plot interactive
import matplotlib as matplotlib
from pasta.augment import inline

matplotlib
inline

# importing required libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

# creating a dummy dataset
x = np.random.randint(low=10, high=1000, size=(1000,))
y = np.random.randint(low=20, high=1000, size=(1000,))
z = np.random.randint(low=1, high=1000, size=(1000,))
colo = np.random.randn(10, 1000)*1000

# creating 3d figures
fig = plt.figure(figsize=(10, 10))
ax = Axes3D(fig)

# configuring colorbar
color_map = cm.ScalarMappable(cmap=cm.gray)
color_map.set_array(colo)

# creating the heatmap
img = ax.scatter(x, y, z, marker='s',
				s=100, color='gray')
plt.colorbar(color_map)

# adding title and labels
ax.set_title("3D Heatmap")
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# displaying plot
plt.show()
