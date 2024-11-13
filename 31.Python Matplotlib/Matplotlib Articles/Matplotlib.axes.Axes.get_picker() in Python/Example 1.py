# Implementation of matplotlib function
import numpy as np

np.random.seed(19680801)
import matplotlib.pyplot as plt

volume = np.random.rayleigh(7, size=40)
amount = np.random.poisson(7, size=40)
ranking = np.random.normal(size=40)
price = np.random.uniform(1, 7, size=40)

fig, ax = plt.subplots()

scatter = ax.scatter(volume,
                     amount,
                     c=ranking,
                     s=price * 3,
                     vmin=-3,
                     vmax=3,
                     cmap="Spectral")

legend1 = ax.legend(*scatter.legend_elements(num=5),
                    loc="upper left",
                    title="Ranking")

ax.add_artist(legend1)

ax.text(8, 8, "Value return : " + str(ax.get_picker()),
        fontweight="bold",
        fontsize=18)

fig.suptitle('matplotlib.axes.Axes.get_picker() function \
Example', fontweight="bold")

plt.show()
