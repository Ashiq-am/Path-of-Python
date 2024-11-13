# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
from matplotlib import collections, colors, transforms
import numpy as np

nverts = 50
npts = 100

r = np.arange(nverts)
theta = np.linspace(0, 2 * np.pi, nverts)

xx = r * np.sin(theta)
yy = r * np.cos(theta)

spiral = np.column_stack([xx, yy])

rs = np.random.RandomState(19680801)

xyo = rs.randn(npts, 2)

colors = [colors.to_rgba(c)
          for c in plt.rcParams['axes.prop_cycle'].by_key()['color']]

fig, ax1 = plt.subplots()

col = collections.RegularPolyCollection(
    7, sizes=np.abs(xx) * 10.0,
    offsets=xyo,
    transOffset=ax1.transData)

trans = transforms.Affine2D().scale(fig.dpi / 72.0)
Axis.set_transform(col, trans)

ax1.add_collection(col, autolim=True)
col.set_color(colors)

fig.suptitle('matplotlib.axis.Axis.set_transform() \
function Example\n', fontweight="bold")

plt.show()
