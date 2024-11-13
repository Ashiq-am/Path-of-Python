# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()

ax1.minorticks_on()

np.random.seed(19680801)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

ax1.hist(x, 50, density = True, facecolor ='g',
		alpha = 0.65)

ax1.set_xlim(40, 160)
ax1.set_ylim(0, 0.03)
plt.grid(True)

ax1.minorticks_off()
fig.suptitle('matplotlib.axes.Axes.minorticks_off() function Example\n\n', fontweight ="bold")
plt.show()
