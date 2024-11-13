# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

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

ax.grid()

print("Value return by get_pickradius() :",
      ax.yaxis.get_pickradius())

fig.suptitle("""matplotlib.axis.Axis.get_pickradius() 
function Example\n""", fontweight="bold")

plt.show()
