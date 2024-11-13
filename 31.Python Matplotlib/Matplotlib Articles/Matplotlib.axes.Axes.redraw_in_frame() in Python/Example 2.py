# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
import time

fig, ax = plt.subplots()
line, = ax.plot(np.random.randn(100))

tstart = time.time()
num_plots = 0
fig.canvas.draw()
while time.time() - tstart < 5:
    line.set_ydata(np.random.randn(100))
    ax.redraw_in_frame()
    num_plots += 1

ax.set_title('matplotlib.axes.Axes.redraw_in_frame() \
function Example')

plt.show()
