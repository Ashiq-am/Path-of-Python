# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('% Y')

with cbook.get_sample_data('goog.npz') as datafile:
    data = np.load(datafile)['price_data'].view(np.recarray)

fig, ax = plt.subplots()
ax.plot('date', 'adj_close', data=data, color="green")

ax.xaxis.set_major_locator(years)
ax.set_ylim((100, 300))

ax.format_xdata = mdates.DateFormatter('% m')
ax.grid(True)

fig.suptitle('matplotlib.axes.Axes.format_xdata() function\
Example', fontweight="bold")
plt.show()
