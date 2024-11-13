import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])

a, b = np.meshgrid(a, b)

# surface plot for a + b
fig = plt.figure()
axes = fig.gca(projection ='3d')
axes.plot_surface(a, b, a + b)

plt.show()
