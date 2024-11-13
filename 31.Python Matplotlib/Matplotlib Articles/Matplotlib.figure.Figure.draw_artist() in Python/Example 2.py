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
    fig.draw_artist(ax.patch)
    fig.draw_artist(line)
    num_plots += 1

fig.suptitle('matplotlib.figure.Figure.draw_artist()\
function Example')

plt.show()
