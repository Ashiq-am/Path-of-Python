# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np

np.random.seed(19680801)
import matplotlib.pyplot as plt

volume = np.random.rayleigh(27, size=100)
amount = np.random.poisson(7, size=100)
ranking = np.random.normal(size=100)
price = np.random.uniform(1, 7, size=100)

fig, ax = plt.subplots()

scatter = ax.scatter(volume * 2,
                     amount ** 3,
                     c=ranking,
                     s=price ** 3,
                     vmin=-3,
                     vmax=3,
                     cmap="Spectral")
ax.yaxis.set_pickradius(25)
ax.xaxis.set_pickradius(5)
ax.grid()

fig.suptitle("""matplotlib.axis.Axis.set_pickradius() 
function Example\n""", fontweight="bold")

plt.show()
