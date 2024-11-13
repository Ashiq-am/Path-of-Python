# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

n = 100000
x = np.random.standard_normal(n)
y = 12 * np.random.standard_normal(n)

fig, ax = plt.subplots()
ax.hexbin(x, y, gridsize = 50, cmap ='Greens')
ax.set_title('matplotlib.axes.Axes.hexbin() Example')
plt.show()
