# Implementation of matplotlib function
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


f, ax = plt.subplots()
ax.scatter([1, 2, 3], [4, 5, 6])
ax.set_url('http://www.google.com')
f.canvas.print_figure('scatter.svg')

ax.text(1.5, 5.5, "URL : "
		+ str( ax.get_url()),
		fontweight ="bold")

f.suptitle('matplotlib.axes.Axes.get_url() function Example\n', fontweight ="bold")

plt.show()
