import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Drawing 3 points for each line
plotted_points = np.ones(4)
txt_style = dict(horizontalalignment='right',
                 verticalalignment='center',
                 fontsize=12,
                 fontdict={'family': 'monospace'})

style = dict(linestyle=':',
             color='0.5',
             markersize=10,
             mfc="C0",
             mec="C0")


# helper function for axes formating
def format_ax(ax):
    ax.margins(0.2)
    ax.set_axis_off()
    ax.invert_yaxis()


# helper function for splitting list
def split(a_list):
    i_half = len(a_list) // 2
    return (a_list[:i_half], a_list[i_half:])


figure, axes = plt.subplots(ncols=2)

for ax, markers in zip(axes, split(Line2D.filled_markers)):

    for y, marker in enumerate(markers):
        ax.text(-0.5, y, repr(marker), **txt_style)
        ax.plot(y * plotted_points, marker=marker,
                **style)

    format_ax(ax)

figure.suptitle('filled markers', fontsize=14)

plt.show()
