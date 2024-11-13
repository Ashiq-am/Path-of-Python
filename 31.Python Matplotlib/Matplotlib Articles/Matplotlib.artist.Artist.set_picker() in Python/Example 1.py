# Implementation of matplotlib function
from matplotlib.artist import Artist
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

volume = np.random.rayleigh(27, size=40)
amount = np.random.poisson(7, size=40)
ranking = np.random.normal(size=40)
price = np.random.uniform(1, 7, size=40)

fig, ax = plt.subplots()

scatter = ax.scatter(volume * 2,
                     amount ** 3,
                     c=ranking ** 3,
                     s=price ** 3,
                     vmin=-3,
                     vmax=3,
                     cmap="Spectral")

Artist.set_picker(ax, picker=4)

fig.suptitle('matplotlib.artist.Artist.set_picker()\
function Example', fontweight="bold")

plt.show()
