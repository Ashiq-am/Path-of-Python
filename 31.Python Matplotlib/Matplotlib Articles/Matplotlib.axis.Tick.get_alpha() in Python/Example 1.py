# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(10**7)
mu = 121
sigma = 21
x = mu + sigma * np.random.randn(1000)

num_bins = 100
fig, ax = plt.subplots()

n, bins, patches = ax.hist(x, num_bins,
						density=1,
						color='purple',
						alpha=0.5)

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
	np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

ax.plot(bins, y, '--', color='black')

ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')

w = Tick.get_alpha(ax)
ax.set_title("Alpha Value : "+str(w))

fig.suptitle("""matplotlib.axis.Tick.get_alpha()
function Example\n""", fontweight="bold")

plt.show()
