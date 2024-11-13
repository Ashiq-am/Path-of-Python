# Implementation of matplotlib function
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)


def gfg1(event):
    # get the x and y pixel coords
    x, y = event.x, event.y
    if event.inaxes:
        # the axes instance
        ax = event.inaxes
        print('Coordinates : % f and\
              % f' % (event.xdata, event.ydata))


def gfg2(event):
    if event.button is MouseButton.LEFT:
        print('Successfully disconnected')
        plt.disconnect(binding_id)


binding_id = plt.connect('motion_notify_event',
                         gfg1)

plt.connect('button_press_event', gfg2)

plt.suptitle('matplotlib.pyplot.disconnect()\
function Example', fontweight="bold")
plt.show()
