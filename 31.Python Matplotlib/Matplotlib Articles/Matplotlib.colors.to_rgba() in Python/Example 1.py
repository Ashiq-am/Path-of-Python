import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import colors as mcolors
import numpy as np

# simple example showing many
# lines in a single set of axes
x_axis = np.arange(100)

# Here are different sets of
# y to plot vs x
y_axis = x_axis[:50, np.newaxis] + x_axis[np.newaxis, :]

segements = np.zeros((50, 100, 2))
segements[:, :, 1] = y_axis
segements[:, :, 0] = x_axis

#some supported values to test
# masked array :
segements = np.ma.masked_where((segements > 50) & (segements < 60),
							segements)

# setting the plot limits.
figure, axes = plt.subplots()
axes.set_xlim(x_axis.min(), x_axis.max())
axes.set_ylim(y_axis.min(), y_axis.max())

# colors is sequence of rgba
# tuples and .rgba implementation
colors = [mcolors.to_rgba(c)
		for c in plt.rcParams['axes.prop_cycle'].by_key()['color']]

line_segments = LineCollection(segements,
							linewidths = (0.5, 1, 1.5, 2),
							colors = colors,
							linestyle = 'solid')

axes.add_collection(line_segments)
axes.set_title(' With masked arrays')
plt.show()
