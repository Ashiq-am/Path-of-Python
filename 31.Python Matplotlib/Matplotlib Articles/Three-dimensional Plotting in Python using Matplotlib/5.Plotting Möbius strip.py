from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation


theta = np.linspace(0, 2 * np.pi, 10)
w = np.linspace(-1, 5, 8)
w, theta = np.meshgrid(w, theta)
phi = 0.5 * theta

# radius in x-y plane
r = 1 + w * np.cos(phi)

# all three axes
x = np.ravel(r * np.cos(theta))
y = np.ravel(r * np.sin(theta))
z = np.ravel(w * np.sin(phi))

# triangulate in the underlying
# parametrization
tri = Triangulation(np.ravel(w), np.ravel(theta))

ax = plt.axes(projection ='3d')
ax.plot_trisurf(x, y, z, triangles = tri.triangles,
				cmap ='viridis', linewidths = 0.2);
