# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig1, (ax1, ax11) = plt.subplots(1, 2)
fig2, (ax2, ax22) = plt.subplots(1, 2)
ax1.set(xlim=(-0.5, 1.5),
        ylim=(-0.5, 1.5),
        autoscale_on=False)

ax2.set(xlim=(0.5, 0.75),
        ylim=(0.5, 0.75),
        autoscale_on=False)

ax11.set(xlim=(-0.5, 1.5),
         ylim=(-0.5, 1.5),
         autoscale_on=False)

ax22.set(xlim=(0.5, 0.75),
         ylim=(0.5, 0.75),
         autoscale_on=False)

x, y, s, c = np.random.rand(4, 200)
s *= 200

ax1.scatter(x, y, s, c)
ax2.scatter(x, y, s, c)
ax11.scatter(x, y, s, c)
ax22.scatter(x, y, s, c)


def GFG(event):
    if event.button != 1:
        return
    x, y = event.xdata, event.ydata
    ax2.set_xlim(x - 0.1, x + 0.1)
    ax2.set_ylim(y - 0.1, y + 0.1)
    ax22.set_xlim(x - 0.1, x + 0.1)
    ax22.set_ylim(y - 0.1, y + 0.1)
    fig2.canvas.draw()


fig1.canvas.mpl_connect('button_press_event',
                        GFG)

xmin, xmax = ax1.get_ylim()
ax1.set_title('Original Window', fontsize=10,
              fontweight='bold')

ax11.set_ylim(xmin, 2 * xmax)
ax11.set_title('After Using get_ylim() function',
               fontsize=10, fontweight='bold')

xmin, xmax = ax2.get_ylim()
ax2.set_title('Zoomed Window', fontsize=10,
              fontweight='bold')

ax22.set_ylim(xmin, 2 * xmax)
ax22.set_title('After Using get_ylim() function',
               fontsize=10, fontweight='bold')

fig1.suptitle('matplotlib.axes.Axes.get_ylim()\
Example\n', fontsize=10, fontweight='bold')
plt.show()
