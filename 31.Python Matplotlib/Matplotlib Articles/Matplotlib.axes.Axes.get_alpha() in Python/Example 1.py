# Implementation of matplotlib function
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
						density = 1,
						color ='green',
						alpha = 0.7)

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
	np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

ax.plot(bins, y, '--', color ='black')

ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')

w = ax.get_alpha()
ax.set_title("Alpha Value : "+str(w))

fig.suptitle('matplotlib.axes.Axes.get_alpha() function Example', fontweight ="bold")

plt.show()
