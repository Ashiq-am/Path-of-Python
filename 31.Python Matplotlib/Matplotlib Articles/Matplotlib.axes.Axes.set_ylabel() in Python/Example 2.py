# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

with cbook.get_sample_data('goog.npz') as datafile:
    price_data = np.load(datafile)['price_data'].view(np.recarray)

# get the most recent 250
# trading days
price_data = price_data[-250:]

delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

volume = (25 * price_data.volume[:-2] / price_data.volume[0]) ** (2.2)
close = (0.03 * price_data.close[:-2] / 0.03 * price_data.open[:-2]) ** 2

fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:],
           c=close, s=volume,
           alpha=0.5)

ax.set_ylabel(r'Y-axis contains $\Delta_{i+1}$ values',
              fontweight='bold')
ax.grid(True)
fig.suptitle('matplotlib.axes.Axes.set_ylabel() Examples\n',
             fontsize=14, fontweight='bold')
plt.show()
