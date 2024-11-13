import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])

a, b = np.meshgrid(a, b)

# surface plot for a**2 + b**2
a = np.arange(-1, 1, 0.02)
b = a
a, b = np.meshgrid(a, b)

fig = plt.figure()
axes = fig.gca(projection ='3d')
axes.contour(a, b, a**2 + b**2)

plt.show()
