# Importing modules
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
from matplotlib.patches import Polygon
import numpy as np


def Trigolo1(tri):
    if tri == -1:
        points = [0, 0, 0]

    else:
        points = triang.triangles[tri]

    xs = triang.x[points]
    ys = triang.y[points]
    polygon.set_xy(np.column_stack([xs, ys]))


def Trigolo2(event):
    if event.inaxes is None:
        tri = -1

    else:
        tri = trifinder(event.xdata, event.ydata)

    Trigolo1(tri)
    plt.title('Example 2\nTriangle No : %i' % tri)
    event.canvas.draw()


# Create a Triangulation.
ang = 16
rad = 5
mrad = 0.25
radii = np.linspace(mrad, 0.95, rad)

angletri = np.linspace(0,
                       2 * np.pi, ang,
                       endpoint=False)

angletri = np.repeat(angletri[..., np.newaxis],
                     rad,
                     axis=1)

angletri[:, 1::2] += np.pi / ang

x = (radii * np.cos(angletri)).flatten()
y = (radii * np.sin(angletri)).flatten()

triang = Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < mrad)

# Use the triangulation's default TriFinder object.
trifinder = triang.get_trifinder()

# Setup plot and callbacks.
plt.subplot(111, aspect='equal')
plt.triplot(triang, 'o-')
polygon = Polygon([[0, 0], [0, 0]], facecolor='y')
Trigolo1(-1)
plt.gca().add_patch(polygon)
plt.gcf().canvas.mpl_connect('motion_notify_event', Trigolo2)

plt.show()
