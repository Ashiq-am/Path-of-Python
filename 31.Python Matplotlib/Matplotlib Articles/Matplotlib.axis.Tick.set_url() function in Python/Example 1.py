# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
s = ax.scatter([1, 10, 3], [4, 5, 6])

Tick.set_url(s, 'http://www.google.com')
fig.canvas.print_figure('geeks1.svg')

fig.suptitle('matplotlib.axis.Tick.set_url() \
function Example', fontweight="bold")

plt.show()
