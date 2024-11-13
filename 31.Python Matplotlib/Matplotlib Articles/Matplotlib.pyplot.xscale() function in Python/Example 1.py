# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import EngFormatter

val = np.random.RandomState(19680801)
xs = np.logspace(1, 9, 100)
ys = (0.8 + 4 * val.uniform(size=100)) * np.log10(xs) ** 2

plt.xscale('log')
plt.plot(xs, ys)
plt.xlabel('Frequency')

plt.title('matplotlib.pyplot.xscale() \
function Example\n', fontweight="bold")

plt.show()
