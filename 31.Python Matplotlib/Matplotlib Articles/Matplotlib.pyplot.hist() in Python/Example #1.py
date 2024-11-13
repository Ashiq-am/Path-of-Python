# Implementation of matplotlib function
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10**7)
mu = 121
sigma = 21
x = mu + sigma * np.random.randn(1000)

num_bins = 100

n, bins, patches = plt.hist(x, num_bins,
							density = 1,
							color ='green',
							alpha = 0.7)

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
	np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

plt.plot(bins, y, '--', color ='black')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.title('matplotlib.pyplot.hist() function Example\n\n',
		fontweight ="bold")

plt.show()
