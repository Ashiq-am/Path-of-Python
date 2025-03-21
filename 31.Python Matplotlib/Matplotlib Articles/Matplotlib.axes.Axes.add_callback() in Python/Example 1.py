# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
import time


def update():
    plt.get_current_fig_manager().canvas.figure.patch.set_facecolor(str(np.random.random()))
    plt.draw()
    print("Draw at time :", time.time())


def start_animation():
    timer = fig.canvas.new_timer(interval=50)
    timer.add_callback(update)
    timer.start()


fig, ax = plt.subplots()
start_animation()

ax.set_title('matplotlib.axes.Axes.add_callback() function\
Example', fontweight="bold")

plt.show()
