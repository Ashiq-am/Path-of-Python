# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

plt.minorticks_on()

np.random.seed(19680801)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

plt.hist(x, 150, density = True, facecolor ='g', alpha = 0.65)

plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)

plt.minorticks_off()
plt.title('matplotlib.pyplot.minorticks_off() function Example',
											fontweight ="bold")
plt.show()
