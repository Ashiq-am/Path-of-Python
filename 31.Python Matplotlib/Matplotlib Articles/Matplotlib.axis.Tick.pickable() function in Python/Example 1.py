# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np

np.random.seed(19680801)
import matplotlib.pyplot as plt

volume = np.random.rayleigh(27, size=100)
amount = np.random.poisson(10, size=100)
ranking = np.random.normal(size=100)
price = np.random.uniform(1, 10, size=100)

fig, ax = plt.subplots()

scatter = ax.scatter(volume * 2, amount * 3,
                     c=ranking ** 3,
                     s=(price * 5) ** 2,
                     vmin=-4, vmax=4,
                     cmap="Spectral")

ax.text(60, 30, "Value return : "
        + str(Tick.pickable(ax)),
        fontweight="bold",
        fontsize=16)

fig.suptitle('matplotlib.axis.Tick.pickable() \
function Example', fontweight="bold")

plt.show()
