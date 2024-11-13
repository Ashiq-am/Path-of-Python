# Implementation of matplotlib function

import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import drange
import numpy as np

date1 = datetime.datetime(2020, 4, 2)
date2 = datetime.datetime(2020, 4, 6)
delta = datetime.timedelta(hours=24)
dates = drange(date1, date2, delta)

y = np.arange(len(dates))

fig, ax = plt.subplots()
ax.plot_date(dates, y ** 2)

ax.set_title('matplotlib.axes.Axes.plot_date Example1')
plt.show()
