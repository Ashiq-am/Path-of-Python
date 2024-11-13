import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as patches
import numpy as np

mpl.rcParams['figure.dpi'] = 80
mpl.rcParams['savefig.dpi'] = 80


def redraw(event):
    if np.size(plt.get_figlabels()):
        ax.clear()
        drawRectangles(ax)
        fig.canvas.draw()
    else:
        pass


def drawRectangles(ax):
    td2dis = ax.transData
    coords = td2dis.transform([0.2, 0.5])
    tr = mpl.transforms.Affine2D().rotate_deg_around(coords[0],
                                                     coords[1], 10)
    t = td2dis + tr
    rec0 = patches.Rectangle((0.5, 0.5),
                             0.25, 0.2,
                             color='green',
                             alpha=0.4)
    ax.add_patch(rec0)
    rect1 = patches.Rectangle((0.5, 0.5),
                              0.25, 0.2,
                              color='green',
                              alpha=0.7,
                              transform=t)
    ax.add_patch(rect1)
    plt.title('matplotlib.pyplot.get_figlabels() function Example', fontweight="bold")
    plt.grid()


figSize = (8, 6)
fig = plt.figure("Patch rotate", figsize=figSize)

ax = fig.add_subplot(111)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

fig.canvas.mpl_connect('resize_event', redraw)
drawRectangles(ax)

plt.show()
