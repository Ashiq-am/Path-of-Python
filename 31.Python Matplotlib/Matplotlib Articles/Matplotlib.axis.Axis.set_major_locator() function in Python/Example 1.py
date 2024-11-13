# Implementation of matplotlib function
from matplotlib.axis import Axis
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

Axis.set_major_locator(ax.xaxis, years)
ax.set_ylim((100, 300))

ax.format_xdata = mdates.DateFormatter('% m')
ax.grid(True)

fig.suptitle("Matplotlib.axis.Axis.set_major_locator()\n\
Function Example", fontsize=12, fontweight='bold')

plt.show()
