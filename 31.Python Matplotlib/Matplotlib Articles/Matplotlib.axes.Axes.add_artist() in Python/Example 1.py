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
					vmin =-4, vmax = 4,
					cmap ="Spectral")

legend1 = ax.legend(*scatter.legend_elements(num = 5),
					loc ="upper left",
					title ="Ranking")

ax.add_artist(legend1)

kw = dict(prop ="sizes", num = 5,
		color = scatter.cmap(0.7),
		fmt =" {x:.2f}",
		func = lambda s: np.sqrt(s/.3)/3)

legend2 = ax.legend(*scatter.legend_elements(**kw),
					loc ="lower right",
					title ="Size")

fig.suptitle('matplotlib.axes.Axes.add_artist() function Example\n\n', fontweight ="bold")
plt.show()
