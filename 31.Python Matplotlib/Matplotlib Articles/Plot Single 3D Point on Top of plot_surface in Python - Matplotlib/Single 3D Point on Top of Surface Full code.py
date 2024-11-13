import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data for the plot_surface plot
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# create a 3D figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 3D surface plot
ax.plot_surface(X, Y, Z, cmap='viridis')

# 3D point (x,y,z) coordinate
# X-coordinate of the point
point_x = X.mean()
# Y-coordinate of the point
point_y = Y.mean()
# Z-coordinate of the point
point_z = 1.5*Z.max()
# Print 3d point
print('3D point(x,y,z):',point_x,point_y,point_z)

# Plot the single 3d point on the same axis
ax.scatter(point_x, point_y, point_z, color='red', s=50)

# Set x,y & z label
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# Set Tile
ax.set_title('3D Point on 3D surface')

plt.show()
