# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
s = ax.scatter([1, 2, 3], [4, 5, 6])
Axis.set_url(s, 'http://www.google.com')
fig.canvas.print_figure('geeks1.svg')

fig.suptitle('matplotlib.axis.Axis.set_url() \
function Example\n', fontweight="bold")

plt.show()
