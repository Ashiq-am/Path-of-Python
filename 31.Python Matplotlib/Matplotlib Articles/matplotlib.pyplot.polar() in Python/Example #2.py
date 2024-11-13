# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np

from matplotlib.transforms import offset_copy

xs = np.arange(8)
ys = np.cos(xs ** 2)

fig = plt.figure(figsize=(5, 10))
ax = plt.subplot(1, 1, 1)

trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       y=6, units='dots')

for x, y in zip(xs, ys):
    plt.polar(x, y, 'go')
    plt.text(x, y, '% d, % d' % (int(x), int(y)),
             transform=trans_offset,
             horizontalalignment='center',
             verticalalignment='bottom')

plt.title('matplotlib.pyplot.polar() function Example',
          fontweight="bold")
plt.show()
