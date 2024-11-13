# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()


def tellme(s):
    ax.set_title(s, fontsize=12, fontweight="bold")
    fig.canvas.draw()
    ax.redraw_in_frame()


tellme('matplotlib.axes.Axes.redraw_in_frame() function \
Example')

plt.show()
