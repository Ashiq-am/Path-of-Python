# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(19680801)

volume = np.random.rayleigh(7, size=40)
amount = np.random.poisson(7, size=40)
ranking = np.random.normal(size=40)
price = np.random.uniform(1, 7, size=40)

fig, ax = plt.subplots()

scatter = ax.scatter(volume**3,
					amount**3,
					c=ranking**3,
					s=price ** 4,
					vmin=-3,
					vmax=3,
					cmap="Spectral")

ax.text(8, 8, "Value return : "
		+ str(Tick.get_picker(ax)),
		fontweight="bold",
		fontsize=18)

fig.suptitle("""matplotlib.axis.Tick.get_picker()
function Example\n""", fontweight="bold")

plt.show()
