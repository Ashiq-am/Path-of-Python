# Implementation of matplotlib function
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig, ax = plt.subplots()


def tellme(s):
    ax.set_title(s, fontsize=16)
    fig.canvas.draw()
    renderer = fig.canvas.renderer
    ax.draw(renderer)


tellme('matplotlib.axes.Axes.draw() function Example')
plt.show()
