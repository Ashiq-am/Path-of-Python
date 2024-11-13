# Implementation of matplotlib function
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig, ax = plt.subplots()


def tellme(s):
    ax.set_title(s, fontsize=16)
    fig.canvas.draw()
    renderer = fig.canvas.renderer
    fig.draw(renderer)


tellme('matplotlib.figure.Figure.draw() \
function Example')

plt.show()
