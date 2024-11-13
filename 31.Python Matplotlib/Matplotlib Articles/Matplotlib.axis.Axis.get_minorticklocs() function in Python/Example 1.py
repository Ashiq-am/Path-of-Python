# Implementation of matplotlib function
from matplotlib.axis import Axis
from matplotlib.artist import Artist
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib

fig, ax = plt.subplots()


def tellme(s):
    ax.set_title(s, fontsize=16)
    fig.canvas.draw()
    renderer = fig.canvas.renderer
    Artist.draw(ax, renderer)


tellme("Matplotlib.axis.Axis.get_minorticklocs()\n\
Function Example")
ax.grid()

print("Value of get_minorticklocs() :")
ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(1))
for i in ax.xaxis.get_minorticklocs():
    print(i)

plt.show()
