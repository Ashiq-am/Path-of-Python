# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
from matplotlib.patches import Polygon
import numpy as np

ang = 3
radi = 8
radii = np.linspace(0.25, 0.95, radi)

res = np.linspace(0, 4 * np.pi, ang)
res = np.repeat(res[..., np.newaxis], radi, axis=1)
res[:, 1::2] += np.pi / ang

x = (radii * np.cos(2 * res)).flatten()
y = (radii * np.sin(2 * res)).flatten()

triang = Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < 0.25)

trifinder = triang.get_trifinder()

fig = plt.figure()
plt.triplot(triang, 'go-')
polygon = Polygon([[0, 0], [0, 0]], facecolor='r')


def update_polygon(tri):
    if tri == -1:
        points = [0, 0, 0]

    else:
        points = triang.triangles[tri]

    xs = triang.x[points]
    ys = triang.y[points]
    polygon.set_xy(np.column_stack([xs, ys]))


def motion_notify(event):
    if event.inaxes is None:
        tri = -1

    else:
        tri = trifinder(event.xdata, event.ydata)

    update_polygon(tri)

    fig.suptitle('matplotlib.figure.Figure.gca()\
    function Example\n\n Potion number : %i' % tri,
                 fontweight="bold")

    event.canvas.draw()


update_polygon(-1)
fig.gca().add_patch(polygon)
plt.gcf().canvas.mpl_connect('motion_notify_event',
                             motion_notify)

plt.show()
