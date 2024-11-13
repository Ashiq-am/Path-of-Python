# ImpleIn Reviewtation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

n_angles = 36
n_radii = 10
min_radius = 2
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles,
                     endpoint=False)
angles = np.repeat(angles[..., np.newaxis],
                   n_radii, axis=1)
angles[:, 1::2] += 2 * np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()

triang = tri.Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
fig, ax = plt.subplots()

ax.triplot(triang, 'bo-', lw=1, color="green")

w = ax.has_data()

print("Value Return by has_data() :", w)

fig.suptitle('matplotlib.axes.Axes.has_data() function\
Example\n\n', fontweight="bold")

fig.canvas.draw()

plt.show()
