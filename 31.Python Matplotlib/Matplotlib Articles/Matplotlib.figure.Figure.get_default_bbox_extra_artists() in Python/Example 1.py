# ImpleIn Reviewtation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

n_angles = 36
n_radii = 10
min_radius = 2
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi,
                     n_angles,
                     endpoint=False)
angles = np.repeat(angles[..., np.newaxis],
                   n_radii,
                   axis=1)
angles[:, 1::2] += 2 * np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()

triang = tri.Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
fig, ax = plt.subplots()

ax.triplot(triang, 'bo-', lw=1, color="green")

w = fig.get_default_bbox_extra_artists()

print("Value Return by get_default_bbox_extra_artists() :")
for i in w:
    print(i)

fig.canvas.draw()
fig.suptitle('matplotlib.figure.Figure.get_default_bbox_extra_artists()\
function Example', fontweight="bold")

plt.show()
