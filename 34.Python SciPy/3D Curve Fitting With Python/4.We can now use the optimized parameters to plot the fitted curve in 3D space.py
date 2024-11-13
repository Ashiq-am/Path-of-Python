import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create 3D plot of the data points and the fitted curve
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, color='blue')
x_range = np.linspace(0, 1, 50)
y_range = np.linspace(0, 1, 50)
X, Y = np.meshgrid(x_range, y_range)
Z = func(X, Y, *popt)
ax.plot_surface(X, Y, Z, color='red', alpha=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
