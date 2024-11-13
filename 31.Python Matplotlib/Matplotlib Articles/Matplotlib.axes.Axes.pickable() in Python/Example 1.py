# Implementation of matplotlib function
import numpy as np
np.random.seed(19680801)
import matplotlib.pyplot as plt

volume = np.random.rayleigh(27, size = 40)
amount = np.random.poisson(10, size = 40)
ranking = np.random.normal(size = 40)
price = np.random.uniform(1, 10, size = 40)

fig, ax = plt.subplots()

scatter = ax.scatter(volume * 2, amount * 3,
					c = ranking * 3,
					s = 0.3*(price * 3)**2,
					vmin = -4, vmax = 4,
					cmap = "Spectral")

legend1 = ax.legend(*scatter.legend_elements(num = 5),
					loc ="upper left",
					title ="Ranking")

ax.add_artist(legend1)

ax.text(60, 30, "Value return : " + str(ax.pickable()),
		fontweight ="bold",
		fontsize = 18)

fig.suptitle('matplotlib.axes.Axes.pickable() function\
Example', fontweight ="bold")

plt.show()
