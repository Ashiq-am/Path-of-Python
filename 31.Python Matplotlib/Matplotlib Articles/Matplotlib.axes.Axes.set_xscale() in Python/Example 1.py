# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import EngFormatter

val = np.random.RandomState(19680801)
xs = np.logspace(1, 9, 100)
ys = (0.8 + 4 * val.uniform(size = 100)) * np.log10(xs)**2

fig, ax0 = plt.subplots()
ax0.set_xscale('log')
formatter0 = EngFormatter(unit ='Hz')
ax0.xaxis.set_major_formatter(formatter0)
ax0.plot(xs, ys)
ax0.set_xlabel('Frequency')

fig.suptitle('matplotlib.axes.Axes.set_xscale() function Example\n', fontweight ="bold")

plt.show()
