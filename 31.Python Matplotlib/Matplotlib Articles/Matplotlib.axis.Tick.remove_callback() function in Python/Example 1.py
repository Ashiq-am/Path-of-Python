# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np
import time


def update():
    global timer
    plt.get_current_fig_manager().canvas.figure.patch.set_facecolor(str(np.random.random()))
    plt.draw()


def start_animation():
    global it
    timer = fig.canvas.new_timer(interval=50)
    w = timer.add_callback(update)
    timer.start()
    timer.remove_callback(w)


it = 1
fig = plt.figure()
start_animation()

fig.suptitle('matplotlib.axis.Tick.remove_callback() \
function Example', fontweight="bold")

plt.show()
