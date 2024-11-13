# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

val, res = 100, 15
x = np.sin(val + res * np.random.randn(10000)) - np.cos(val + res * np.random.randn(10000))

n, bins, patches = plt.hist(x, 200,
							density = True,
							facecolor ='g',
							alpha = 0.5)

plt.grid(True)

plt.title('matplotlib.pyplot.grid() function Example\n\n', fontweight ="bold")

plt.show()
