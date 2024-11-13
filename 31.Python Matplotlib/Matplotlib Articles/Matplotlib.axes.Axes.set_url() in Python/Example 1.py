# Implementation of matplotlib function
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

f, ax = plt.subplots()
s = ax.scatter([1, 2, 3], [4, 5, 6])
s.set_url('http://www.google.com')
f.canvas.print_figure('scatter.svg')

f.suptitle('matplotlib.axes.Axes.set_url() function Example\n', fontweight ="bold")

plt.show()
