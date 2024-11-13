# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
rect = fig.patch
rect.set_facecolor('lightslategray')

ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightgoldenrodyellow')


for label in ax1.xaxis.get_ticklabels():
	label.set_color('green')
	label.set_rotation(25)
	label.set_fontsize(16)

for line in ax1.yaxis.get_ticklines():
	line.set_color('yellow')
	line.set_markersize(5)
	line.set_markeredgewidth(3)

fig.suptitle('matplotlib.figure.Figure.add_axes() function Example\n\n', fontweight ="bold")

plt.show()
