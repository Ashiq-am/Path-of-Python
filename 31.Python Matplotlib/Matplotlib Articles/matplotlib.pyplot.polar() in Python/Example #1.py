# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np

from matplotlib.transforms import offset_copy

xs = np.arange(-2, 2)
ys = np.cos(xs**2)
plt.polar(xs, ys)

plt.title('matplotlib.pyplot.polar() function Example',
									fontweight ="bold")
plt.show()
