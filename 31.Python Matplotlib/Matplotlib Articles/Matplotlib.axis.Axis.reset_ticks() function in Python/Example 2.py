# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

delta = 0.5

x = y = np.arange(-2.0, 4.0, delta)
X, Y = np.meshgrid(x ** 2, y)

Z1 = np.exp(-X ** 2 - Y ** 2)
Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
Z = (Z1 - Z2)

transform = mtransforms.Affine2D().rotate_deg(30)
fig, ax = plt.subplots()

im = ax.imshow(Z, interpolation='none',
               origin='lower',
               extent=[-2, 4, -3, 2],
               clip_on=True)

trans_data = transform + ax.transData
Axis.set_transform(im, trans_data)

x1, x2, y1, y2 = im.get_extent()
ax.plot([x1, x2, x2, x1, x1],
        [y1, y1, y2, y2, y1],
        "ro-",
        transform=trans_data)

ax.set_xlim(-5, 5)
ax.set_ylim(-4, 4)

ax.yaxis.reset_ticks()

ax.grid()

fig.suptitle("""matplotlib.axis.Axis.reset_ticks() 
function Example\n""", fontweight="bold")

plt.show()
