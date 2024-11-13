from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


# angle and radius
theta = 2 * np.pi * np.random.random(100)
r = 6 * np.random.random(100)

# all three axes
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f(x, y)

ax = plt.axes(projection ='3d')
ax.scatter(x, y, z, c = z, cmap ='viridis', linewidth = 0.25);

ax = plt.axes(projection ='3d')
ax.plot_trisurf(x, y, z, cmap ='viridis', edgecolor ='green');
