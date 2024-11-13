# Implementation of matplotlib function
from matplotlib.axis import Axis
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig, ax = plt.subplots()


def tellme(s):
    fig.canvas.draw()
    renderer = fig.canvas.renderer
    Axis.draw(ax, renderer)


ax.grid()

fig.suptitle("""matplotlib.axis.Axis.draw() 
function Example\n""", fontweight="bold")

plt.show()
