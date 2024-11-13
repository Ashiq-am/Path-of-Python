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
ax.plot('date', 'adj_close', data=data[:300], color="green")

ax.xaxis.set_major_locator(years)
ax.format_ydata = lambda x: '$% 1.2f' % x
ax.grid(True)

fig.autofmt_xdate()
fig.suptitle('matplotlib.axes.Axes.format_ydata() function Example', fontweight="bold")
plt.show()
