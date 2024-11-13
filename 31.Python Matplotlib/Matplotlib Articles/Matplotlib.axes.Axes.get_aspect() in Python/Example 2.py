# ImpleIn Reviewtation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

n_angles = 36
n_radii = 10
min_radius = 2
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles,
					endpoint = False)

angles = np.repeat(angles[..., np.newaxis],
				n_radii, axis = 1)

angles[:, 1::2] += 2 * np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()

triang = tri.Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis = 1),
						y[triang.triangles].mean(axis = 1))
				< min_radius)
fig, (ax, ax1) = plt.subplots(1, 2)

ax.triplot(triang, 'bo-', lw = 1, color = "green")

ax1.set_aspect('equal')
ax1.triplot(triang, 'bo-', lw = 1, color = "green")

w = ax.get_aspect()
w1 = ax1.get_aspect()

ax.set_title("Axes 1\n Ratio : " +str(w))
ax1.set_title("Axes 2\n Ratio : " +str(w1))

fig.suptitle('matplotlib.axes.Axes.get_aspect() function Example\n\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
