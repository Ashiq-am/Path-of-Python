# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('% Y')

with cbook.get_sample_data('goog.npz') as datafile:
	data = np.load(datafile)['price_data']

fig, ax = plt.subplots()
ax.plot('date', 'adj_close', data = data, color ="k")

ax.yaxis.set_major_locator(years)
ax.yaxis.set_major_formatter(years_fmt)
ax.yaxis.set_minor_locator(months)

ax.format_ydata = mdates.DateFormatter('% Y')
ax.grid(True)

fig.suptitle('matplotlib.axes.Axes.format_ydata() function Example', fontweight ="bold")
plt.show()
