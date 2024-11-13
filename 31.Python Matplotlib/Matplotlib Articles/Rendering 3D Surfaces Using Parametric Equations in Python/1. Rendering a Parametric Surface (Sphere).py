import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Define the parametric equations for the sphere
def sphere(R, u, v):
    x = R * np.cos(u) * np.sin(v)
    y = R * np.sin(u) * np.sin(v)
    z = R * np.cos(v)
    return x, y, z
# Create a grid of the u and v values
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
u, v = np.meshgrid(u, v)
# Calculate the coordinates of the sphere
R = 1
x, y, z = sphere(R, u, v)
# Plot the sphere
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='b', edgecolor='k', alpha=0.6)
# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Parametric Surface: Sphere')
# Show the plot
plt.show()
