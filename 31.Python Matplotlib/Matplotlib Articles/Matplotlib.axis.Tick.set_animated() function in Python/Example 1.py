# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = np.array([[1, 2, 3, 4, 5],
                 [7, 4, 9, 2, 3]])

fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(0, 20))

line, = ax.plot([], [], 'r-')
annotation = ax.annotate('',
                         xy=(data[0][0],
                             data[1][0]))

Tick.set_animated(annotation, True)


def init():
    return line, annotation


def update(num):
    newData = np.array([[1 + num,
                         2 + num / 2,
                         3,
                         4 - num / 4,
                         5 + num],
                        [7, 4,
                         9 + num / 3,
                         2, 3]])

    line.set_data(newData)
    return line, annotation


anim = animation.FuncAnimation(fig,
                               update,
                               frames=59,
                               init_func=init,
                               interval=60,
                               blit=True)

fig.suptitle('matplotlib.axis.Tick.set_animated() \
function Example', fontweight="bold")

plt.show()
