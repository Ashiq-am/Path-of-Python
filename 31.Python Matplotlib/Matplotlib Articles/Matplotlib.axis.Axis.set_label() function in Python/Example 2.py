# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

n = 100000
x = np.random.standard_normal(n)
y = 2 * np.random.standard_normal(n)
z = [1, 2, 3, 4]

fig, ax = plt.subplots()
hb = ax.hexbin(x, y,
               gridsize=50,
               bins='log',
               cmap='bone')

cb = fig.colorbar(hb, ax=ax)
cb.set_label('log')

fig.suptitle('matplotlib.axis.Axis.set_label() \
function Example\n', fontweight="bold")

plt.show()
