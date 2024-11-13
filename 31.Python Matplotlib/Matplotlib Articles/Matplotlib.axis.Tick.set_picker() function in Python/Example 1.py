# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

volume = np.random.rayleigh(27, size=40)
amount = np.random.poisson(7, size=40)
ranking = np.random.normal(size=40)
price = np.random.uniform(1, 7, size=40)

fig, ax = plt.subplots()

scatter = ax.scatter(volume * 3,
                     amount ** 4,
                     c=ranking ** 4,
                     s=price ** 4,
                     vmin=-3,
                     vmax=3,
                     cmap="Spectral")

Tick.set_picker(ax, picker=4)

fig.suptitle('matplotlib.axis.Tick.set_picker() \
function Example', fontweight="bold")

plt.show()
