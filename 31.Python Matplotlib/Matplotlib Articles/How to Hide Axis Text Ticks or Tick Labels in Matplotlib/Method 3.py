import numpy as np
import matplotlib.ticker as ticker

ax = plt.axes()

x = np.random.rand(100)
ax.plot(x, color='g')

ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())
